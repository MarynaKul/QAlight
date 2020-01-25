import random
listN = [random.randint(0, 1000) for x in range(10)]
print(listN)

del listN[9]
print(listN)