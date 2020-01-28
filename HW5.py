a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if a < b:
    print('Да ну!')
elif a > b:
    print('Свершилось!')
elif a == b and c == 0:
    print('Это может длиться бесконечно...Попробуйте другое "с"')
else:
   if a == b:
    print('А если так?')
    print('a + c(%s)' %c)
    a = a + c
    print('b - c(%s)' %c)
    b = b - c
    if a < b:
     print('Да ну!')
    else:
     print('Свершилось!')