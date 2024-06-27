class Pokemon:

    def __init__(self, name, health, attack, defense, sp_attack, sp_defense, speed, moveset):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.moveset = moveset

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense
    
    def get_sp_attack(self):
        return self.sp_attack
    
    def get_sp_defense(self):
        return self.sp_defense

    def get_speed(self):
        return self.speed
    
    def get_moveset(self):
        return self.moveset
    
    def set_name(self, name):
        self.name = name
    
    def set_health(self, health):
        self.health = health
    
    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_sp_attack(self, sp_attack):
        self.sp_attack = sp_attack

    def set_sp_defense(self, sp_defense):
        self.sp_defense = sp_defense

    def set_speed(self, speed):
        self.speed = speed

    def set_moveset(self, moveset):
        self.moveset = moveset