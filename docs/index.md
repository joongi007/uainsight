# Welcome to useragent_parser

useragent-parser is a powerful and flexible Python package for parsing and analyzing User-Agent strings. It offers seamless integration with popular web frameworks like FastAPI, Django, and Flask.

## Key Features

- Accurate parsing of User-Agent strings
- Extraction of browser, operating system, and device information
- Bot detection capabilities
- Easy integration with FastAPI, Django, and Flask

## Quick Start

```python
from useragent_parser import parse_user_agent

ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
ua = parse_user_agent(ua_string)

print(f"Browser: {ua.browser.name} {ua.browser.version}")
print(f"OS: {ua.os.name} {ua.os.version}")
print(f"Device: {ua.device}")
```

## Next Steps

- [Installation Guide](installation.md): Learn how to install useragent_parser
- [Usage Guide](usage.md): Explore the basic and advanced usage of useragent_parser
- [API Reference](api.md): Detailed information about useragent_parser's classes and methods
- Framework Integrations:
    - [Django Integration](integrations/django.md)
    - [FastAPI Integration](integrations/fastapi.md)
    - [Flask Integration](integrations/flask.md)

## Contributing

We welcome contributions! Please see our [Contributing Guide](contributing.md) for more details.

## License

useragent_parser is released under the MIT License. See the [LICENSE](https://github.com/joongi007/useragent-parser/blob/main/LICENSE) file for more details.