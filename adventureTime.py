



def damageTaken(damage: int, armorValue: int, health: int, name : str) -> None:
        effectiveArmor = armorValue * (1 - (0.0008 * armorValue))
        damageReduction = effectiveArmor / (100 + effectiveArmor)
        totalDamage = damage * (1- damageReduction)
        self.health -= totalDamage

        if health <= 0:
            print (name, "has been slain")


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

    def damageTaken(self, damage: int) -> None:
        damageTaken(damage, self.defense, self.health, character.name)


class adventurerSheet:
    def __init__(self, character: character, stats: stats ) -> None:
        self.character = character
        self.stats = stats

    def damageDealt(self, target: mobs) -> None:
        damage = self.stats.damageDealt()
        target.damageTaken(damage)
        print ("You have dealt", damage, "damage to", target.name)


    
    


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
        damageTaken(damage, self.defense, self.health, self.name)

    def damage(self) -> int:
     return self.attack - (adventurerSheet.stats.defense)
        

    def damageDealt(self, target: adventurerSheet) -> None:
        damage = self.damage()
        target.stats.damageTaken(damage)
        print(self.name, "has attacked you for", self.attack, "damage.")
        target.stats.health-= self.attack #idk if this will work
""" 
class slime(mobs):
class zombie(mobs):
class ogre(mobs):
class dragon(mobs): 
"""

def main():

    dialogue = str ("You are a level 0 adventurer, who has recently embarked on your journey \nto clear a rookie dungeon. Select your Name, Race, and Proffession")
    print(dialogue)
    name = input("Choose your character's Name\n")
    race = input("Choose your character's Race\n")
    profession = input("Choose your character's Profession\n")

    health = 100
    attack = 10
    defense = 10

    charStats = stats(health, attack, defense)
    charDetails = character(profession,race, 0, name, 0)
    character1 = adventurerSheet(charDetails, charStats)

    slime1 = mobs("slime", 50,10,10,10)

    while character1.stats.health > 0 and slime1.health > 0:
        character1.damageDealt(slime1)
        slime1.damageDealt(character1)
   
    if character1.stats.health > 0:
        print("You win!")
    else:
        print("You lose!")


main()