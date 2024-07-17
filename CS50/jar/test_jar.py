from jar import Jar

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    thrown = False
    try:
        jar = Jar(-1)
    except:
        thrown = True
    assert thrown == True

def test_str():
    jar = Jar(1000)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(4)
    assert jar.size == 4
    thrown = False
    try:
        jar.deposit(6)
    except:
        thrown = True
    assert thrown == True


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    thrown = False
    try:
        jar.withdraw(4)
    except:
        thrown = True
    assert thrown == True
