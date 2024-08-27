import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-2)
    jar1 = Jar(15)
    assert jar1.capacity == 15

def test_str():
    jar1 = Jar(15)
    assert str(jar1) == ""
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    jar1.withdraw(2)
    assert str(jar1) == "🍪🍪🍪"

def test_deposit():
    jar1 = Jar(15)
    jar1.deposit(5)
    assert jar1.size == 5
    jar1.deposit(10)
    assert jar1.size == 15
    with pytest.raises(ValueError):
        jar1.deposit(1)

def test_withdraw():
    jar1 = Jar(15)
    jar1.deposit(15)
    jar1.withdraw(5)
    assert jar1.size == 10
    jar1.withdraw(10)
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar1.withdraw(1)

def main():
    test_init()
    test_str()
    test_deposit()

if __name__ == "__main__":
    main()
