from django.conf import settings
from django.test import RequestFactory
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from flask import Flask

from useragent_parser.integrations.django import DjangoUserAgentMiddleware
from useragent_parser.integrations.fastapi import FastapiUserAgentMiddleware
from useragent_parser.integrations.flask import FlaskUserAgentMiddleware

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"


def test_fastapi_middleware():
    app = FastAPI()
    app.add_middleware(FastapiUserAgentMiddleware)

    @app.get("/")
    async def root(request: Request):
        ua = request.state.user_agent
        return {"browser": ua.browser.name}

    client = TestClient(app)
    response = client.get("/", headers={"User-Agent": USER_AGENT})

    assert response.status_code == 200
    assert response.json() == {"browser": "Chrome"}

    @app.get("/debug")
    async def debug(request: Request):
        return {"user_agent": str(getattr(request.state, "user_agent", "Not found"))}

    debug_response = client.get("/debug", headers={"User-Agent": USER_AGENT})
    print(f"Debug response: {debug_response.json()}")


def test_django_middleware():
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY="test_secret_key",
            MIDDLEWARE=["useragent_parser.integrations.django.UserAgentMiddleware"],
        )

    factory = RequestFactory()
    request = factory.get("/", HTTP_USER_AGENT=USER_AGENT)

    middleware = DjangoUserAgentMiddleware(lambda r: None)
    middleware(request)

    assert hasattr(request, "user_agent")
    assert request.user_agent.browser.name == "Chrome"


def test_flask_middleware():
    app = Flask(__name__)
    FlaskUserAgentMiddleware(app)

    @app.route("/")
    def hello():
        from flask import request

        ua = request.user_agent
        return f"Hello {ua.browser.name} user!"

    client = app.test_client()
    response = client.get("/", headers={"User-Agent": USER_AGENT})

    assert response.status_code == 200
    assert "Hello Chrome user!" in response.data.decode()
