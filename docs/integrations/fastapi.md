# FastAPI Integration

useragent_parser offers easy integration with FastAPI through a middleware.

## Installation

First, make sure you have installed useragent_parser in your FastAPI project:

```bash
poetry add useragent-parser
```

or if you're using pip:

```bash
pip install useragent-parser
```

## Configuration

To use useragent_parser with FastAPI, you need to add the middleware to your FastAPI application:

```python
from fastapi import FastAPI
from useragent_parser.integrations.fastapi import FastapiUserAgentMiddleware

app = FastAPI()
app.add_middleware(FastapiUserAgentMiddleware)
```

## Usage

Once the middleware is added, you can access the parsed User-Agent information in your route handlers through the `request.state` object:

```python
from fastapi import Request

@app.get("/")
async def root(request: Request):
    ua = request.state.user_agent
    return {"message": f"You're using {ua.browser.name} {ua.browser.version} on {ua.os.name} {ua.os.version}"}
```

## Advanced Usage

### Custom Middleware Configuration

If you need to customize the middleware, you can pass parameters when adding it:

```python
app.add_middleware(FastapiUserAgentMiddleware, ua_header="X-My-User-Agent")
```

### Dependency Injection

You can also create a dependency to easily inject the User-Agent information into your route handlers:

```python
from fastapi import Depends

def get_user_agent(request: Request):
    return request.state.user_agent

@app.get("/browser")
async def get_browser_info(ua: UserAgent = Depends(get_user_agent)):
    return {"browser": ua.browser.name, "version": ua.browser.version}
```

This approach allows you to directly access the User-Agent information without going through the request object.