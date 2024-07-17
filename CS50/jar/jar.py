class Jar:
    def __init__(self, capacity=12):
        if not (capacity >= 0 and isinstance(capacity, int)):
            raise ValueError("Impossible capacity!")
        else:
            self._capacity=capacity
            self._cookies = 0
    def __str__(self):
        return self._cookies*"🍪"
    def deposit(self, n):
        if self._cookies+n <= self._capacity:
            self._cookies=self._cookies+n
        else:
            raise ValueError("Too many cookies to fit in the jar!")
    def withdraw(self, n):
        if self._cookies-n >= 0:
            self._cookies=self._cookies-n
        else:
            raise ValueError("Too many cookies asked to be withdrawn!")
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
    @property
    def size(self):
        return self._cookies
"""
def main():
    cookie_jar = Jar(5)
    #cookie_jar = Jar(-1)
    cookie_jar.deposit(4)
    #cookie_jar.deposit(6)
    cookie_jar.withdraw(2)
    #cookie_jar.withdraw(5)
    print(cookie_jar.capacity)
    print(cookie_jar.size) 
    print(str(cookie_jar))  

if __name__ == "__main__":
    main()
"""