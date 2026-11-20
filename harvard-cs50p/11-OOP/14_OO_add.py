class Vault:
    def __init__(self, gold=0, silver=0):
        self.gold = gold
        self.silver = silver

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        return Vault(gold, silver)


v1 = Vault(100, 50)
v2 = Vault(200, 30)

total = v1 + v2

print(total.gold)
print(total.silver)