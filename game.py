from monster import Goblin, Dragon, Troll
from character import Character
import random
from combat import *
import sys,os


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
            return self.monsters.pop()
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
            player_attack = self.player.attack()
            if player_attack != False:
                print "You hit the monster and did " + str(player_attack) + " damage"
                self.monster.hit_points -= player_attack
            else:
                print "Your attack missed"
            print "The {} has {} hit points".format(self.monster.__class__.__name__, self.monster.hit_points)
        elif choice == 'rest':
            self.player.rest()
            print self.player.hit_points


    def clean_up(self):
        if self.monster.hit_points <= 0:
            print "You killed that monster"
            self.player.experience += self.monster.experience
            print self.player.experience
            choice = raw_input("Choose a new Monster?: ")
            if choice == 'yes':
                self.get_monster()
            else:
                print "Thanks for playing"
                sys.exit()

    def __init__(self):
        self.setup()

        while self.player.hit_points > 0 or (self.monster.hit_points > 0 and self.monster):
            self.monster_turn()
            self.player_turn()
            self.clean_up()


        else:
            print "You loose"
            choice = raw_input("Play again?: ")
            if choice == 'no':
                print "Loser"
                sys.exit()


Game()