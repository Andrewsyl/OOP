from monster import Goblin, Dragon, Troll
from character import Character
import random
from combat import *


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Dragon(),
            Troll()
        ]
        self.monster = self.get_monster()

    def get_monster(self):
        try:
            return random.choice(self.monsters)
        except IndexError:
            return None

    def monster_turn(self):
        self.monster_attack = random.randint(0, 1)
        if self.monster_attack == 1:
            print 'Monster Attacks'
            self.player.dodge()
            if self.player.dodge() == True:
                print "You dodged the attack!"
            else:
                print "Monster hit you!"
                self.player.hit()
            print self.player.hit_points
        else:
            print "Monster didn't attack"

    def player_turn(self):
        choice = raw_input('Attack or rest: ').lower()
        if choice == 'attack':
            self.player.attack()
            if self.player.attack() == True:
                print "You hit the monster and did " + str(self.player.attack()) + " damage"
                self.monster.hit_points -= self.player.attack()
            else:
                print "Your attack missed"
            print self.monster.__class__.__name__
            print self.monster.hit_points
        elif choice == 'rest':
            self.player.rest()
            print self.player.hit_points

    def __init__(self):
        self.setup()

        while self.player.hit_points > 0 or self.monster.hit_points > 0:
            self.monster_turn()
            self.player_turn()
            if self.player.hit_points > 0:
                print "You killed that monster"
                self.get_monster()
            else:
                print "You loose"

jon = Game()