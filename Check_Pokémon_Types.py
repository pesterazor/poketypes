import pytest

types_matrix = [[1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.0, 0.5, 1.0, 1.0, 1.0,
                 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [2.0, 1.0, 0.5, 0.5, 1.0, 2.0, 0.5, 0.0, 2.0, 1.0, 1.0, 1.0,
                 1.0, 0.5, 2.0, 1.0, 2.0, 0.5],
                [1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 2.0,
                 0.5, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 0.0, 1.0, 1.0, 2.0,
                 1.0, 1.0, 1.0, 1.0, 1.0, 2.0],
                [1.0, 1.0, 0.0, 2.0, 1.0, 2.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5,
                 2.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                [1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0,
                 1.0, 1.0, 2.0, 1.0, 1.0, 1.0],
                [1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 2.0,
                 1.0, 2.0, 1.0, 1.0, 2.0, 0.5],
                [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0,
                 1.0, 2.0, 1.0, 1.0, 0.5, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0,
                 0.5, 1.0, 2.0, 1.0, 1.0, 2.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 0.5, 0.5, 2.0,
                 1.0, 1.0, 2.0, 0.5, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 0.5,
                 1.0, 1.0, 1.0, 0.5, 1.0, 1.0],
                [1.0, 1.0, 0.5, 0.5, 2.0, 2.0, 0.5, 1.0, 0.5, 0.5, 2.0, 0.5,
                 1.0, 1.0, 1.0, 0.5, 1.0, 1.0],
                [1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5,
                 0.5, 1.0, 1.0, 0.5, 1.0, 1.0],
                [1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0,
                 1.0, 0.5, 1.0, 1.0, 0.0, 1.0],
                [1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 2.0,
                 1.0, 1.0, 0.5, 2.0, 1.0, 1.0],
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0,
                 1.0, 1.0, 1.0, 2.0, 1.0, 0.0],
                [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0,
                 1.0, 2.0, 1.0, 1.0, 0.5, 0.5],
                [1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0,
                 1.0, 1.0, 1.0, 2.0, 2.0, 1.0]]

types = ["normal", "fighting", "flying", "poison", "ground", "rock", "bug",
         "ghost", "steel", "fire", "water", "grass", "electric", "psychic",
         "ice", "dragon", "dark", "fairy"]


def typesMultFactor(attackType, defendType):
    return types_matrix[types.index(attackType)][types.index(defendType)]


while True:
    i = 0  # tracks errors
    try:
        req = input("Insert the opponent type/s (e.g. flying, steel):\n>>> ")
        req = req.replace(", ", ",").lower()
        req = req.split(",")
        if len(req) == 1:
            i = 1
            test = types.index(str(req[0]))
        else:
            i = 1
            test = types.index(str(req[0]))
            i = 2
            test = test * types.index(str(req[1]))
        break
    except ValueError:
        if i == 1:
            print("Sorry, I cannot understand the 1st type. Try again!\n")
        elif i == 2:
            print("Sorry, I cannot understand the 2nd type. Try again!\n")

noDamage = []
vLowDamage = []
lowDamage = []
normDamage = []
highDamage = []
quadDamage = []

i = 0
if len(req) == 1:
    for i in range(18):
        damage = typesMultFactor(types[i], req[0])
        if damage == 2.0:
            highDamage = highDamage + [types[i]]
        elif damage == 1.0:
            normDamage = normDamage + [types[i]]
        elif damage == 0.5:
            lowDamage = lowDamage + [types[i]]
        else:
            noDamage = noDamage + [types[i]]
        i = i + 1
else:
    for i in range(18):
        damage = typesMultFactor(
            types[i], req[0]) * typesMultFactor(types[i], req[1])
        if damage == 4.0:
            quadDamage = quadDamage + [types[i]]
        elif damage == 2.0:
            highDamage = highDamage + [types[i]]
        elif damage == 1.0:
            normDamage = normDamage + [types[i]]
        elif damage == 0.5:
            lowDamage = lowDamage + [types[i]]
        elif damage == 0.25:
            vLowDamage = vLowDamage + [types[i]]
        else:
            noDamage = noDamage + [types[i]]
        i = i + 1

print("")
if quadDamage != []:
    print("#" * 10 + " 4x damage " + "#" * 10)
    for t in quadDamage:
        print("- " + str(t))
    print("")
if highDamage != []:
    print("#" * 10 + " 2x damage " + "#" * 10)
    for t in highDamage:
        print("- " + str(t))
    print("")
if normDamage != []:
    print("#" * 10 + " 1x damage " + "#" * 10)
    for t in normDamage:
        print("- " + str(t))
    print("")
if lowDamage != []:
    print("#" * 9 + " 0.5x damage " + "#" * 9)
    for t in lowDamage:
        print("- " + str(t))
    print("")
if vLowDamage != []:
    print("#" * 8 + " 0.25x damage " + "#" * 9)
    for t in vLowDamage:
        print("- " + str(t))
    print("")
if noDamage != []:
    print("#" * 10 + " No damage " + "#" * 10)
    for t in noDamage:
        print("- " + str(t))
    print("")

input()
