from uainsight import parse_user_agent

# Sample User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
]

for ua_string in user_agents:
    ua = parse_user_agent(ua_string)
    print(f"User-Agent: {ua_string}")
    print(f"Browser: {ua.browser.name} {ua.browser.version}")
    print(f"OS: {ua.os.name} {ua.os.version}")
    print(f"Device: {ua.device}")
    print(f"Is Mobile: {ua.is_mobile}")
    print(f"Is Tablet: {ua.is_tablet}")
    print(f"Is Desktop: {ua.is_desktop}")
    print(f"Is Bot: {ua.is_bot}")
    print("---")
