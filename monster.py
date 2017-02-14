import random
from combat import Combat

COLOR = ('blue', 'green', 'black', 'orange')
NOISES = ('boo', 'tweet', 'oink', 'moo', 'help', 'don\'\t hurt me')


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
        self.sound = kwargs.get('sound', random.choice(NOISES))
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

    def monster_go(self, player, monster):
        monster_attack = random.randint(0, 5)
        if monster_attack > 2:
            print str(monster.__class__.__name__) + ' Attacks'
            player.dodge()
            if player.dodge() == True:
                print "You dodged the attack!"
            else:
                print "Monster hit you!"
                player.hit()
            print "You have " + str(player.hit_points) + " HP"
        else:
            print "Monster didn't attack"


class Goblin(Monster):
    hit_points = 5
    experience = 10


class Dragon(Monster):
    hit_points = 10
    experience = 15


class Troll(Monster):
    hit_points = 8
    experience = 11
