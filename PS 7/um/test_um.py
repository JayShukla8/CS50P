from um import count

def test_1():
    assert count("um...") == 1
    assert count("I, um, want a, um, nevermind...") == 2
    assert count("um?") == 1


def test_2():
    assert count("yumyum") == 0
    assert count("umma") == 0
    assert count("I think, um, i will have a, um, a yummy bowl of maggi") == 2


def test_3():
    assert count("Um?") == 1
    assert count("HEY, UM, please speak politely.") == 1
    assert count("Yummy") == 0


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
