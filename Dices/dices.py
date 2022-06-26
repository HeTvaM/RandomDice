from Stuff.abstract import Dice

class Default(Dice):
    def __init__(self):
        super().__init__(
            x,y, type,
            dmg, duration, effect
        )

    def attack(self):
        self.time += 1
        if self.time >= self.duration:
            self.time = 0
            return self.dmg

        return 0

    def do_ability(self): pass
