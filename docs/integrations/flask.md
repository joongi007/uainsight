# Flask Integration

uainsight provides straightforward integration with Flask through a middleware.

## Installation

First, ensure you have installed uainsight in your Flask project:

```bash
poetry add uainsight
```

or if you're using pip:

```bash
pip install uainsight
```

## Configuration

To use uainsight with Flask, you need to initialize the middleware with your Flask app:

```python
from flask import Flask
from uainsight.integrations.flask import FlaskUserAgentMiddleware

app = Flask(__name__)
FlaskUserAgentMiddleware(app)
```

## Usage

Once the middleware is initialized, you can access the parsed User-Agent information in your route handlers through the `request` object:

```python
from flask import request

@app.route('/')
def hello():
    ua = request.user_agent
    return f"You're using {ua.browser.name} {ua.browser.version} on {ua.os.name} {ua.os.version}"
```

## Advanced Usage

### Custom Middleware Configuration

If you need to customize the middleware, you can subclass it:

```python
from uainsight.integrations.flask import FlaskUserAgentMiddleware

class MyCustomMiddleware(FlaskUserAgentMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.ua_header = "X-My-User-Agent"  # Use a custom header

# Then use MyCustomMiddleware instead of FlaskUserAgentMiddleware
```

### Using with Flask-RESTful

If you're using Flask-RESTful, you can access the User-Agent information in your resources:

```python
from flask_restful import Resource

class MyResource(Resource):
    def get(self):
        ua = request.user_agent
        return {"browser": ua.browser.name, "os": ua.os.name}
```

Remember to initialize the FlaskUserAgentMiddleware before setting up your Flask-RESTful API.