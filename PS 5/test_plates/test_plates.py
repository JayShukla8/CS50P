from plates import is_valid

def test_len():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AA3456") == True
    assert is_valid("AA34567") == False

def test_1():
    assert is_valid("22") == False
    assert is_valid("A2") == False
    assert is_valid("AA") == True

def test_2():
    assert is_valid("AAA23") == True
    assert is_valid("AA23A") == False

def test_3():
    assert is_valid("AA23") == True
    assert is_valid("AA03") == False

def test_4():
    assert is_valid("AA23") == True
    assert is_valid("AA_23") == False
    assert is_valid("AA.23") == False
    assert is_valid("AA'23") == False


def main():
    test_len()
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == "__main__":
    main()
