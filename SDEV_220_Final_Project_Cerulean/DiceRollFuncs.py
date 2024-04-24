"""
DiceRollFuncs
Elizabeth Baker
Python 3.12.2 10APR2024
This is a collection of dice rolling functions that will be used in the D&D Character sheet for Cerulean group's final project.
"""
def generate_abilities():
    """Generate stats for character abilities"""
    import random
    abl = 0 #holds number of abilities
    abilities = [] #empty list to hold abilities
    while abl < 6:
        roll = 0 #each individual roll
        Rolls = 0 #holds total roll for abilities
        while roll < 3:
            Rolls = Rolls + random.randint(1,6)
            roll += 1
        abl += 1
        abilities.append(Rolls)
    return abilities

#ensure generate_abilities() works as expected:
abilities_list = generate_abilities()
print(abilities_list)
