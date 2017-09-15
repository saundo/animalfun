import pandas as pd

class duck:
    """it's a duck! it's able to do the following:
    + eat - eats food cuz it's hungry
    + crap - it's a bodily function
    + die - that's what happens
    """
    animal = 'bird'
    def __init__(self, name):
        self.name = name
        self.status = 'Alive!'
        self.tummy = 'empty'
        self.wings = 'furry'

    def eat(self, food):
        if isinstance(food, str):
            print(food, 'tastes so good!')
            self.tummy = 'full of ' + food
        else:
            print('thats not food!')

    def crap(self, x):
        self.size = x * 2
        print('all good now')
        print('this big', str(self.size))
        self.tummy = 'empty'

    def die(self):
        if self.status == 'dead :(':
            print('what is dead may never die')
            return
        print('RIP mofo')
        print(str(self.size))
        self.status = 'dead :('

class chicken:
    """it's a chcken
    """
    animal = 'bird'
    def __init__(self, name):
        self.name = name
        self.fly = False

class cow:
    """it's a cow
    """
    animal = 'bovine'
    def __init__(self, name):
        self.name = name

    def moo(self, x):
        self.size = x * 2
        print('mooooooo')
        print('mooooooooooooo', str(self.size))
        self.tummy = 'empty'
        self.stink = True

    def run(self, speed):
        print('runs this fast', speed)

class dog:
    """it's a dog
    """
    animal = 'canine'
    def __init__(self, name):
        self.name = name
        self.bark = 'loud'
        self.react = 'weak'

class cat:
    """it's a cat
    """
    animal = 'feline'
    def __init__(self, name):
        self.name = name
        self.bark = None

    def meow(self, volume):
        self.volume = volume
        print('nice meow')




def kill(o):
    """to kill an animal - it's able to kill the following classes:
    + duck
    """
    if isinstance(o, duck):
        o.die()
    else:
        print("can't kill it.")