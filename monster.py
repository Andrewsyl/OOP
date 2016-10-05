import random
from combat import Combat

COLOR = ('blue', 'green', 'black', 'orange')


class Slime:
    name = 'hat'
    height = 50


class Booger:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'steve')
        self.height = kwargs.get('height', 700)


class Monster(Combat):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Rambo')
        self.sound = kwargs.get('sound', 'Boo')
        self.color = random.choice(COLOR)
        self.hit_points = random.randint(1, 20)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def battlecry(self):
        return self.sound.upper()

    def __str__(self):
        return '%s %s : %s and %s and %s' % (self.name,
                                             self.battlecry(),
                                             self.__class__.__name__,
                                             self.color,
                                             self.hit_points
                                             )


class Goblin(Monster):
    hit_points = 5
    exp = 10


class Dragon(Monster):
    hit_points = 10
    exp = 15

class Troll(Monster):
    hit_points = 8
    exp = 11