from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_custom():
    assert hello("Alice") == "hello, Alice"
    assert hello("Bob") == "hello, Bob"
    assert hello("") == "hello, "
