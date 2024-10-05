# Django Integration

uainsight provides seamless integration with Django through a middleware.

## Installation

First, ensure you have installed uainsight in your Django project:

```bash
poetry add uainsight
```

or if you're using pip:

```bash
pip install uainsight
```

## Configuration

Add the uainsight middleware to your Django project by editing the `MIDDLEWARE` setting in your `settings.py` file:

```python
MIDDLEWARE = [
    # ... other middleware
    'uainsight.integrations.django.DjangoUserAgentMiddleware',
]
```

## Usage

Once the middleware is added, you can access the parsed User-Agent information in your views through the `request` object:

```python
def my_view(request):
    ua = request.user_agent
    return HttpResponse(f"You're using {ua.browser.name} {ua.browser.version} on {ua.os.name} {ua.os.version}")
```

## Advanced Usage

### Custom Middleware Configuration

If you need to customize the middleware, you can create your own subclass:

```python
from uainsight.integrations.django import DjangoUserAgentMiddleware

class MyCustomMiddleware(DjangoUserAgentMiddleware):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.ua_header = "HTTP_X_MY_USER_AGENT"  # Use a custom header

# Then use MyCustomMiddleware in your MIDDLEWARE setting
```

### Accessing User-Agent in Templates

You can also access the User-Agent information in your Django templates:

```html
<p>You're using {{ request.user_agent.browser.name }} on {{ request.user_agent.os.name }}</p>
```

Remember to ensure that the `request` object is available in your template context.