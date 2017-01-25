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

    def weapon_choice(self):
        weapon = raw_input('Weapon ([S]word, [A]xe, [B]ow, [St]taff): ').lower()
        if weapon == 's':
            print "You chose the Sword!"
            return 'sword'
        elif weapon == 'a':
            print "You chose the Axe!"
            return 'axe'
        elif weapon == 'b':
            print "You chose the Bow!"
            return 'bow'
        elif weapon == 'St':
            print "You chose the Staff!"
            return 'staff'
        else:
            self.weapon_choice()

    def level_up(self):
        if self.level == 2:
            pass
        elif self.experience > 20 and self.experience < 50:
            self.level = 2
            print "You have reached level " + str(self.level)

    def __init__(self, **kwargs):
        self.name = raw_input('Name: ')
        self.weapon = self.weapon_choice()
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def hit(self):
        self.hit_points -= random.choice(range(5))
        return self.hit_points
