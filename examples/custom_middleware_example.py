# Usage with WSGI application
from wsgiref.simple_server import make_server

from useragent_parser import UserAgentParser
from useragent_parser.core import UserAgent


class CustomUserAgentMiddleware:
    def __init__(self, app):
        self.app = app
        self.ua_parser = UserAgentParser()

    def __call__(self, environ, start_response):
        ua_string = environ.get("HTTP_USER_AGENT", "")
        parsed_ua: UserAgent = self.ua_parser.parse(ua_string)
        environ["user_agent"] = parsed_ua
        return self.app(environ, start_response)


def application(environ, start_response):
    ua = environ["user_agent"]
    status = "200 OK"
    headers = [("Content-type", "text/plain; charset=utf-8")]
    start_response(status, headers)

    response = f"""
    Browser: {ua.browser.name} {ua.browser.version}
    OS: {ua.os.name} {ua.os.version}
    Device: {ua.device}
    Is Mobile: {ua.is_mobile}
    Is Tablet: {ua.is_tablet}
    Is Desktop: {ua.is_desktop}
    Is Bot: {ua.is_bot}
    """

    return [response.encode("utf-8")]


app = CustomUserAgentMiddleware(application)

if __name__ == "__main__":
    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
