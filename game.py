from monster import Goblin, Dragon, Troll
from character import Character
from combat import *
import sys


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Dragon(),
            Troll()
        ]
        self.monster = self.monsters.pop()

    def get_monster(self):
        try:
            self.monster = self.monsters.pop()
            print "A %s appears" % str(self.monster.__class__.__name__)
            print self.monster.battlecry()
            return self.monster
        except IndexError:
            print "\n****************\nThere are no more monsters.\n You saved the village!"
            sys.exit()

    def monster_turn(self):
        self.monster.monster_go(player=self.player, monster=self.monster)

    def player_turn(self):
        self.player.player_go(player=self.player, monster=self.monster)

    def clean_up(self):
        if self.monster.hit_points <= 0:
            print "You killed the %s" % str(self.monster.__class__.__name__)
            self.player.experience += self.monster.experience
            print "You gained %s experience points" % str(self.monster.experience)
            print "Your experience is %s" % str(self.player.experience)
            self.player.level_up()
            choice = raw_input("Choose a new Monster?: ")
            if choice == 'yes':
                self.get_monster()
            else:
                print "Thanks for playing"
                sys.exit()

    def __init__(self):
        self.setup()

        while self.player.hit_points > 0:
            self.monster_turn()
            self.player_turn()
            self.clean_up()

        print "You loose"
        choice = raw_input("Play again?: ")
        if choice == 'no':
            print "Loser"
            sys.exit()


Game()
