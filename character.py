from monster import *
from combat import Combat


class Character(Combat):
    attack_limit = 10
    experience = 0
    base_hit_points = 10
    level = 1

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 4
        if roll > 4:
            roll = random.randint(1, 9)
        else:
            roll = False
        return roll

    def character_choice(self):
        character = raw_input('Select your player: \nSoldier\nArcher\nPlumber\n:').lower()
        if character in ("soldier", 'archer', 'plumber'):
            return character
        else:
            self.character_choice()

    def weapon_choice(self):
        if self.character == 'plumber':
            weapon = raw_input('Weapon (Plunger, Lunchbox, Fork): ').lower()
        elif self.character == 'soldier':
            weapon = raw_input('Weapon (M4 Carbine, Grenade Launcher, Apple): ').lower()
        else:
            weapon = raw_input('Weapon (Sword, Axe, Bow, Staff): ').lower()
            if weapon in ('sword', 'axe', 'bow', 'staff', 'Plunger', 'Lunchbox', 'Fork'):
                print 'You chose the %s' % weapon.title()
            else:
                self.weapon_choice()
        print 'You chose the ' + weapon.title()
        return weapon

    def level_up(self):
        if (20 < self.experience < 50) and self.level != 2:
            self.level = 2
            print "You have reached level %s" % str(self.level)

    def player_go(self, player, monster):
        choice = raw_input('Attack or rest: ').lower()
        if choice == 'attack':
            player_attack = player.attack()
            if player_attack:
                if player.level == 2:
                    player_attack += 50
                print "You hit the monster and did %s damage" % str(player_attack)
                monster.hit_points -= player_attack
            else:
                print "Your attack missed"
            if monster.hit_points < 0:
                monster.hit_points = 0
            if monster.hit_points > 0:
                print "The {} has {} hit points".format(monster.__class__.__name__, monster.hit_points)
        elif choice == 'rest':
            player.rest()
            print player.hit_points

    def __init__(self, **kwargs):
        self.name = raw_input('Name: ')
        self.character = self.character_choice()
        self.weapon = self.weapon_choice()
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def hit(self):
        self.hit_points -= random.choice(range(5))
        if self.hit_points < 0:
            self.hit_points = 0
        return self.hit_points
