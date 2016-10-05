import random


class Combat:
    attack_limit = 6
    dodge_limit = 6

    def dodge(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4

    def attack(self):
        roll = random.randint(1, self.dodge_limit)
        if roll > 4:
            return random.randint(1, 3)
        else:
            return roll
