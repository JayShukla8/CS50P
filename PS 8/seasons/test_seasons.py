from seasons import check_date
from seasons import convert

def test_check_date():
    assert check_date("2002-12-08") == ("2002", "12", "08")
    assert check_date("2002-13-08") == None
    assert check_date("2002-12-32") == None

def test_convert():
    assert convert(1234) == "One million, seven hundred seventy-six thousand, nine hundred sixty"
    assert convert(234) == "Three hundred thirty-six thousand, nine hundred sixty"

def main():
    test_check_date()
    test_convert()

if __name__ == "__main__":
    main()
