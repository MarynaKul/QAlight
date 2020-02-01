import random
def myList(length, maxValue):
    myList1 = [random.randint(0, maxValue) for x in range(length)]
    print(myList1)