def calculate():
    import sys
    print('Input your number: ')
    a = int(sys.stdin.readline())
    summ = 0
    for i in str(a):
        summ = summ + int(i)
        continue
    print('Sum of Numerals: ', summ)