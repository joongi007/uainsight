# Welcome to uainsight

uainsight is a powerful and flexible Python package for parsing and analyzing User-Agent strings. The name "uainsight" combines "UA" (User Agent) with "insight," reflecting our goal to provide deep understanding and analysis of User-Agent data. It offers seamless integration with popular web frameworks like FastAPI, Django, and Flask.

## What does uainsight mean?

- **UA**: Stands for User Agent, the core focus of our package.
- **insight**: Represents the deep analysis and understanding we provide for User-Agent strings.

Together, uainsight embodies our mission to offer comprehensive, insightful analysis of User-Agent data, going beyond simple parsing to provide valuable insights for web developers and analysts.

## Key Features

- Accurate parsing of User-Agent strings
- Extraction of browser, operating system, and device information
- Bot detection capabilities
- Easy integration with FastAPI, Django, and Flask
- Insightful analysis of User-Agent trends and patterns

## Quick Start

```python
from uainsight import parse_user_agent

ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
ua = parse_user_agent(ua_string)

print(f"Browser: {ua.browser.name} {ua.browser.version}")
print(f"OS: {ua.os.name} {ua.os.version}")
print(f"Device: {ua.device}")
```

## Next Steps

- [Installation Guide](installation.md): Learn how to install uainsight
- [Usage Guide](usage.md): Explore the basic and advanced usage of uainsight
- [API Reference](api.md): Detailed information about uainsight's classes and methods
- Framework Integrations:
    - [Django Integration](integrations/django.md)
    - [FastAPI Integration](integrations/fastapi.md)
    - [Flask Integration](integrations/flask.md)

## Contributing

We welcome contributions! Please see our [Contributing Guide](contributing.md) for more details.

## License

uainsight is released under the MIT License. See the [LICENSE](https://github.com/joongi007/uainsight/blob/main/LICENSE) file for more details.