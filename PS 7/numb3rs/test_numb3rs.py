import pytest
from numb3rs import validate

def test_range():
    assert validate("0.0.0.0") == True
    assert validate("128.128.128.128") == True
    assert validate("0.0.0.256") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False

def test_string():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3") == False
    assert validate("cat") == False

def main():
    test_range()
    test_string()

if __name__ == "__main__":
    main()
