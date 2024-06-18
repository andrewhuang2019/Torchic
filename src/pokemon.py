class Pokemon:

    def __init__(self, health, name, attack, sp_attack, defense, sp_defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.sp_attack = attack
        self.defense = defense
        self.sp_defense = sp_defense
    
    def get_attack(self):
        return self.attack
