import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/2") == 100
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat/2")
    with pytest.raises(ValueError):
        convert("2/dog")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def main():
    test_convert()
    test_gauge()

if __name__ == "__main__":
    main()
