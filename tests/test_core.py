import pytest

from uainsight.core import (
    UserAgentParser,
    parse_user_agent,
)


@pytest.fixture
def parser():
    return UserAgentParser()


def test_parse_chrome_on_windows(parser):
    ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    result = parser.parse(ua_string)
    assert result.browser.name == "Chrome"
    assert result.browser.version == "91.0.4472.124"
    assert result.browser.family == "Chromium"
    assert result.os.name == "Windows 10"
    assert result.os.edition == "Pro 64-bit"
    assert result.device == "Desktop"
    assert result.is_desktop
    assert not result.is_mobile
    assert not result.is_bot


def test_parse_firefox_on_mac():
    ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"
    result = parse_user_agent(ua_string)
    assert result.browser.name == "Firefox"
    assert result.browser.version == "89.0"
    assert result.browser.family == ""
    assert result.os.name == "macOS"
    assert result.device == "Desktop"
    assert result.is_desktop
    assert not result.is_mobile
    assert not result.is_bot


def test_parse_mobile_chrome_on_android(parser):
    ua_string = "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
    result = parser.parse(ua_string)
    assert result.browser.name == "Chrome"
    assert result.os.name == "Android"
    assert result.os.version == "10"
    assert result.device == "Mobile"
    assert result.is_mobile
    assert not result.is_desktop
    assert not result.is_bot


def test_parse_smart_tv():
    ua_string = "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36"
    result = parse_user_agent(ua_string)
    assert result.is_smart_tv
    assert result.device == "Smart TV"
    assert not result.is_mobile
    assert not result.is_desktop


def test_parse_game_console():
    ua_string = "Mozilla/5.0 (PlayStation; PlayStation 4/8.03) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15"
    result = parse_user_agent(ua_string)
    assert result.is_console
    assert result.console_type == "PlayStation"
    assert result.device == "Game Console"
    assert not result.is_mobile
    assert not result.is_desktop


def test_parse_ereader():
    ua_string = "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"
    result = parse_user_agent(ua_string)
    assert result.is_ereader
    assert result.device == "E-reader"
    assert not result.is_mobile
    assert not result.is_desktop


def test_parse_webview():
    ua_string = "Mozilla/5.0 (Linux; Android 10; SM-A505FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36"
    result = parse_user_agent(ua_string)
    assert result.is_web_view
    assert result.web_view_type == "WebView"
    assert result.is_mobile
    assert not result.is_desktop


def test_parse_facebook_app():
    ua_string = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"
    result = parse_user_agent(ua_string)
    assert result.is_web_view
    assert result.web_view_type == "Facebook"
    assert result.is_mobile
    assert not result.is_desktop


def test_parse_yabrowser():
    ua_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 YaBrowser/21.6.1.274 Yowser/2.5 Safari/537.36"
    result = parse_user_agent(ua_string)
    assert result.browser.name == "YaBrowser"
    assert result.browser.version == "21.6.1.274"
    assert result.os.name == "Windows 10"
    assert result.device == "Desktop"


def test_parse_epiphany():
    ua_string = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/602.1 (KHTML, like Gecko) Version/9.0 Safari/602.1 Epiphany/3.20.3"
    result = parse_user_agent(ua_string)
    assert result.browser.name == "Epiphany"
    assert result.browser.version == "3.20.3"
    assert result.os.name == "Linux"
    assert result.device == "Desktop"


def test_empty_user_agent(parser):
    result = parser.parse("")
    assert result is None or result.browser.name == "Unknown"


def test_very_long_user_agent(parser):
    long_ua = (
        "Mozilla/5.0 " * 1000
        + "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    result = parser.parse(long_ua)
    assert result is not None
    assert result.browser.name == "Chrome"


def test_malformed_user_agent(parser):
    malformed_ua = "This is not a valid user agent string"
    result = parser.parse(malformed_ua)
    assert result is None or result.browser.name == "Unknown"


def test_future_chrome_version(parser):
    future_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/999.0.0.0 Safari/537.36"
    result = parser.parse(future_ua)
    assert result.browser.name == "Chrome"
    assert result.browser.version == "999.0.0.0"


def test_future_windows_version(parser):
    future_ua = "Mozilla/5.0 (Windows NT 20.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    result = parser.parse(future_ua)
    assert "Windows" in result.os.name
    assert result.os.version == "20.0"


@pytest.mark.parametrize("locale", ["en_US", "fr_FR", "ja_JP", "ar_SA"])
def test_localized_user_agent(parser, locale):
    localized_ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0 {locale}"
    result = parser.parse(localized_ua)
    assert result.browser.name == "Firefox"
    assert result.os.name == "Windows 10"


def test_performance(parser):
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
        "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    ]

    import random
    import time

    extended_ua_list = ua_list * 1000
    random.seed(42)
    random.shuffle(extended_ua_list)

    start_time = time.time()
    for ua in extended_ua_list:
        parser.parse(ua)
    end_time = time.time()

    elapsed_time = end_time - start_time
    assert elapsed_time < 1.0
