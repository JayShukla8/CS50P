class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Invalid capacity!")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
            return '🍪'*(self.cookies)

    def deposit(self, n):
        if (self.cookies + n) > self._capacity:
            raise ValueError("Exceeds capacity!")
        else:
            self.cookies = self.cookies + n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError("There are fewer cookies than those asked to be removed!")
        else:
            self.cookies = self.cookies - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies

jar1 = Jar(15)
jar1.deposit(4)
print(jar1)
jar1.withdraw(2)
print(jar1)
