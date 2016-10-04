from monster import Goblin, Booger
from character import Character
import random
from combat import *


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Booger(),
        ]
        self.monster = self.get_monster()

    def get_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        self.monster_attack = random.randint(0, 1)
        if self.monster_attack == 1:
            print 'yo'
            self.player.hit()
            print self.player.hit_points
        else:
            print 'no'

    def __init__(self):
        self.setup()

        while self.player.hit_points > 0:
            # print self.player
            self.monster_turn()
            # self.player_turn()

        if self.player.hit_points:
            print "You win"
        else:
            print "You loose"
