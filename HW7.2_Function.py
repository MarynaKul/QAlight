import random
def myList(length, maxValue):
    a = [random.randint(0, maxValue) for x in range(length)]
    for x in range(length):
        if x > 7:
         print(a[x])


