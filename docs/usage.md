# Usage Guide

This guide provides an overview of how to use useragent_parser in your Python projects.

## Basic Usage

### Parsing a User-Agent String

The most common use case is parsing a User-Agent string:

```python
from useragent_parser import parse_user_agent

ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
ua = parse_user_agent(ua_string)

print(f"Browser: {ua.browser.name} {ua.browser.version}")
print(f"OS: {ua.os.name} {ua.os.version}")
print(f"Device: {ua.device}")
```

### Checking for Mobile Devices

You can easily check if a User-Agent string belongs to a mobile device:

```python
if ua.is_mobile:
    print("This is a mobile device")
else:
    print("This is not a mobile device")
```

### Bot Detection

useragent_parser can help you identify if a User-Agent string belongs to a bot:

```python
if ua.is_bot:
    print("This User-Agent belongs to a bot")
else:
    print("This User-Agent does not belong to a bot")
```

## Advanced Usage

### Using the UserAgentParser Class

For more control over the parsing process, you can use the `UserAgentParser` class directly:

```python
from useragent_parser import UserAgentParser

parser = UserAgentParser()
ua = parser.parse("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1")

print(f"Browser Family: {ua.browser.family}")
print(f"OS: {ua.os.name} {ua.os.version}")
print(f"Is Touch Capable: {ua.is_touch_capable}")
```

### Handling Unknown User-Agents

When encountering an unknown User-Agent, useragent_parser will still provide as much information as it can:

```python
ua = parse_user_agent("Unknown/1.0")
print(f"Browser: {ua.browser.name or 'Unknown'}")
print(f"OS: {ua.os.name or 'Unknown'}")
```

For more examples, check the examples folder.

## Best Practices

- Always handle the case where certain attributes might be None or empty strings.
- Use the `is_bot` attribute to filter out bot traffic in your analytics or rate limiting logic.
- Remember that User-Agent strings can be spoofed, so don't rely on them for security-critical decisions.

## Next Steps

- Check out the [API Reference](api.md) for a complete list of attributes and methods.
- Learn how to integrate useragent_parser with popular web frameworks:
    - [Django Integration](integrations/django.md)
    - [FastAPI Integration](integrations/fastapi.md)
    - [Flask Integration](integrations/flask.md)
