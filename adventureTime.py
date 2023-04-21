


class mobs():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def damageTaken(self,damage):
        self.health -= damage
        
        if self.health <= 0:
            print (self.name, "has been slain")

    def damageDealt(self,attack):
        print(self.name, "has attacked you for", self.attack, "damage.")
        target.take_damage(self.attack)

class slime(mobs):

class zombie(mobs):


class ogre(mobs):


class dragon(mobs):


