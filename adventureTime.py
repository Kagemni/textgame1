


class mobs:
    def __init__(self, name: str, health: int, attack: int, defense: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def damageTaken(self,damage: int) -> None:
        self.health -= damage
        
        if self.health <= 0:
            print (self.name, "has been slain")

    def damageDealt(self,target: int) -> None:
        print(self.name, "has attacked you for", self.attack, "damage.")
        target.take_damage(self.attack) #idk if this will work

""" 
class slime(mobs):

class zombie(mobs):


class ogre(mobs):


class dragon(mobs): """

class dungeonLevel:
    def __init__(self, floor: int, mobs: str) -> None:
        self.floor = floor
        self.mobs = mobs
    def getMobs(self):
        return self.mobs
    def get_level(self):
        return self.floor

class character:
    def __init__(self, profession: str, race: str, level: int, name: str) -> None:
        self.profession = profession
        self.race = race
        self.level = level
        self.name = name

class stats:
    def __init__(self, health: int, attack: int, defense: int) -> None:
        self.health = health
        self.attack = attack
        self.defense = defense

class adventurerSheet:
    def __init__(self, character: character, stats: stats ) -> None:
        self.character = character
        self.stats = stats
