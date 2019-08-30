import random

class Spell():
    def __init__(self, name, cost,dmg,stype):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.stype = stype


    def gen_spell_dmg(self):
        low = self.dmg - 15
        high = self.dmg + 10
        return random.randrange(low,high)

