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
            print "A " + str(self.monster.__class__.__name__) + " appears"
            print self.monster.battlecry()
            return self.monster
        except IndexError:
            print "There are no more monsters.\n You saved the village!"
            sys.exit()

    def monster_turn(self):
        self.monster_attack = random.randint(0, 5)
        if self.monster_attack > 2:
            print str(self.monster.__class__.__name__) + ' Attacks'
            self.player.dodge()
            if self.player.dodge() == True:
                print "You dodged the attack!"
            else:
                print "Monster hit you!"
                self.player.hit()
            print "You have " + str(self.player.hit_points) + " HP"
        else:
            print "Monster didn't attack"

    def player_turn(self):
        self.player.player_go(player=self.player, monster=self.monster)

    def clean_up(self):
        if self.monster.hit_points <= 0:
            print "You killed that monster"
            self.player.experience += self.monster.experience
            print "You gained " + str(self.monster.experience) + " experience points"
            print "Your experience is " + str(self.player.experience)
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
