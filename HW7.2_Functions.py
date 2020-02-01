import random
def myList(length, maxValue):
    a = [random.randint(0, maxValue) for x in range(length)]
    for x in a:
        if x > 7:
         print(x)