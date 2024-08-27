from twttr import shorten

def test_lowercase():
    assert shorten("harry potter") == "hrry pttr"

def test_uppercase():
    assert shorten("HARRY POTTER") == "HRRY PTTR"

def test_mix():
    assert shorten("HArrY PotteR") == "HrrY PttR"

def test_numbers():
    assert shorten("Number 4, Privet Drive") == "Nmbr 4, Prvt Drv"

def test_punctuation():
    assert shorten("Adieu, adieu, to you, and you, and you.") == "d, d, t y, nd y, nd y."

def main():
    test_lowercase()
    test_uppercase()
    test_mix()
    test_numbers()
    test_punctuation()

if __name__ == "__main__":
    main()
