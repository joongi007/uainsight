# API Reference

## UserAgentParser

```python
class UserAgentParser:
    def __init__(self):
        # Initialize the parser

    def parse(self, user_agent_string: str) -> UserAgent:
        """
        Parse a User-Agent string and return a UserAgent object.

        Args:
            user_agent_string (str): The User-Agent string to parse

        Returns:
            UserAgent: An object containing parsed User-Agent information
        """
```

## parse_user_agent

```python
def parse_user_agent(user_agent_string: str) -> UserAgent:
    """
    Parse a User-Agent string and return a UserAgent object.

    This is a convenience function that creates a UserAgentParser instance
    and calls its parse method.

    Args:
        user_agent_string (str): The User-Agent string to parse

    Returns:
        UserAgent: An object containing parsed User-Agent information
    """
```

## UserAgent

```python
@dataclass
class UserAgent:
    browser: Browser
    os: OperatingSystem
    device: str
    is_bot: bool
    is_mobile: bool
    is_tablet: bool
    is_desktop: bool
    is_touch_capable: bool
    is_pc: bool
    is_web_view: bool
    web_view_type: str
    is_smart_tv: bool
    is_console: bool
    console_type: str
    is_ereader: bool
    raw: str
```

## Browser

```
@dataclass
class Browser:
    name: str
    version: str
    family: str = ""
```

## OperatingSystem

```python
@dataclass
class OperatingSystem:
    name: str
    version: str
    edition: str = ""
```