from bank import value

def test_0():
    assert value("Hello Kramer") == 0

def test_20():
    assert value("heyy Kramer") == 20

def test_100():
    assert value("What's up Kramer") == 100

def test_uppercase():
    assert value("HELLO Kramer") == 0

def test_lowercase():
    assert value("hello Kramer") == 0

def main():
    test_0()
    test_20()
    test_100()
    test_uppercase()
    test_lowercase()

if __name__ == "__main__":
    main()
