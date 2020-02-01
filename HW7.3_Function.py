import random
def myList(length, maxValue):
    myList1 = [random.randint(0, maxValue) for x in range(length)]
    myList2 = [random.randint(0, maxValue) for y in range(length)]
    merge_lists = []
    print(myList1)
    print(myList2)
    for x in myList1:
        if x in merge_lists:
            continue
        for y in myList2:
            if x == y:
                 merge_lists.append(x)
                 break
    print(merge_lists)