from re import compile

from uainsight import UserAgentParser


class CustomUserAgentParser(UserAgentParser):
    def __init__(self):
        super().__init__()
        # Add custom browser detection
        self._browser_regexes.append(
            ("MyCustomBrowser", compile(r"MyCustomBrowser\/([\d\w\.]+)"))
        )

    def _get_device(self, user_agent_lower_string: str) -> str:
        # Custom device detection logic
        if "mycustomdevice" in user_agent_lower_string:
            return "Custom Device"
        return super()._get_device(user_agent_lower_string)


# Use the custom parser
custom_parser = CustomUserAgentParser()

# Sample User-Agent string
ua_string = "MyCustomBrowser/1.0 (MycustomDevice; Android 10)"

ua = custom_parser.parse(ua_string)
print(ua.browser)
print(f"User-Agent: {ua_string}")
print(f"Browser: {ua.browser.name} {ua.browser.version}")
print(f"OS: {ua.os.name} {ua.os.version}")
print(f"Device: {ua.device}")
