from uainsight.utils import compile_regexes, is_bot


def test_compile_regexes():
    test_regexes = [
        ("Test1", r"test1\/([\d\w\.]+)"),
        ("Test2", r"test2\/([\d\w\.]+)"),
    ]
    compiled = compile_regexes(test_regexes)
    assert len(compiled) == 2
    assert compiled[0][0] == "Test1"
    assert compiled[1][0] == "Test2"
    assert compiled[0][1].search("test1/1.2.3").group(1) == "1.2.3"
    assert compiled[1][1].search("test2/4.5.6").group(1) == "4.5.6"


def test_is_bot():
    assert is_bot(
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    assert is_bot(
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    )
    assert not is_bot(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
