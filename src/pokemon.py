class Pokemon:

    def __init__(self, health, name, attack, sp_attack, defense, sp_defense, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.sp_attack = sp_attack
        self.defense = defense
        self.sp_defense = sp_defense
        self.moveset = moveset

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_sp_attack(self):
        return self.sp_attack

    def get_defense(self):
        return self.defense
    
    def get_sp_defense(self):
        return self.sp_defense
    
    def get_moveset(self):
        return self.moveset