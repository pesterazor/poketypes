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


req = "flying,Steel"
#req = input("Insert the opponent type/s (e.g. flying, steel):\n>>> ")
req = req.replace(", ", ",").lower()
req = req.split(",")
assert (len(req) == 1) or (len(req) == 2)

noDamage = []
vLowDamage = []
lowDamage = []
normDamage = []
highDamage = []
quadDamage = []
i = 0
if len(req) == 1:
    for t in types_matrix:
        damage = t[types.index(str(req[0]))]
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
    for t in types_matrix:
        damage = t[types.index(str(req[0]))] * t[types.index(str(req[0]))]
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

print(lowDamage)
print(normDamage)
print(highDamage)
print(quadDamage)
input()
