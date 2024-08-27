from working import convert
import pytest


def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 PM to 8 AM") == "12:00 to 08:00"
    assert convert("12 AM to 8 AM") == "00:00 to 08:00"
    assert convert("11:59 PM to 7:59 AM") == "23:59 to 07:59"


def test_edgecase():
    with pytest.raises(ValueError):
        convert("10:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("10:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM through 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def main():
    test_normal()
    test_edgecase()

if __name__ == "__main__":
    main()
