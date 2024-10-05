import uvicorn
from fastapi import FastAPI, Request

from uainsight.integrations.fastapi import FastapiUserAgentMiddleware

app = FastAPI()
app.add_middleware(FastapiUserAgentMiddleware)


@app.get("/")
async def user_agent_info(request: Request):
    ua = request.state.user_agent
    return {
        "browser": f"{ua.browser.name} {ua.browser.version}",
        "os": f"{ua.os.name} {ua.os.version}",
        "device": ua.device,
        "is_mobile": ua.is_mobile,
        "is_tablet": ua.is_tablet,
        "is_desktop": ua.is_desktop,
        "is_bot": ua.is_bot,
    }


if __name__ == "__main__":
    uvicorn.run(app)
