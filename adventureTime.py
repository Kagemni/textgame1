



def damageTaken(damage: int, armorValue: int, health: int, name : str) -> None:
        effectiveArmor = armorValue * (1 - (0.0008 * armorValue))
        damageReduction = effectiveArmor / (100 + effectiveArmor)
        totalDamage = damage * (1- damageReduction)
        health -= totalDamage

        if health <= 0:
            print (name, "has been slain")


class mobs:
    def __init__(self, name: str, health: int, attack: int, defense: int, experience: int) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience = experience
    
    def experienceGiven(self, characterLevel: int) -> int:
        return self.experience - (self.experience * characterLevel * 0.1)

    def damageTaken(self, damage: int) -> None:
        damageTaken(damage, self.defense, self.health)

    def damage(self) -> int:
     return self.attack - stats.defense
        

    def damageDealt(self, target: int) -> None:
        print(self.name, "has attacked you for", self.attack, "damage.")
        target.takeDamage(self.attack) #idk if this will work
""" 
class slime(mobs):
class zombie(mobs):
class ogre(mobs):
class dragon(mobs): 
"""
class dungeonLevel:
    def __init__(self, floor: int, mobs: str) -> None:
        self.floor = floor
        self.mobs = mobs
    def getMobs(self):
        return self.mobs
    def getLevel(self):
        return self.floor

class character:
    def __init__(self, profession: str, race: str, level: int, name: str, experienceLevel: int) -> None:
        self.profession = profession
        self.race = race
        self.level = level
        self.name = name
        self.experienceLevel = experienceLevel

class stats:
    def __init__(self, health: int, attack: int, defense: int) -> None:
        self.health = health
        self.attack = attack
        self.defense = defense

    def damageDealt(self) -> int:
        return self.attack - (mobs.defense)

class adventurerSheet:
    def __init__(self, character: character, stats: stats ) -> None:
        self.character = character
        self.stats = stats
