from monster import *
from combat import Combat


class Character(Combat):
    attack_limit = 10
    experience = 0
    base_hit_points = 10

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 4
        if roll > 4:
            roll = random.randint(1, 3)
        else:
            roll = False
        return roll

    def weapon_choice(self):
        weapon = raw_input('Weapon ([S]word, [A]xe, [B]ow, [St]taff): ').lower()
        if weapon == 's':
            return 'Sword'
        elif weapon == 'a':
            return 'Axe'
        elif weapon == 'b':
            return 'Bow'
        elif weapon == 'St':
            return 'Staff'
        else:
            self.weapon_choice()

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
        self.hit_points -= 1
        return self.hit_points
