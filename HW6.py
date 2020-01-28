a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if c <= 0:
    print('Введите положительное число "с"')
else:
 while a <= b:
    a = a + c
    if a <= b:
     print('Значение a %s ' %a + 'Пока еще нет')
 else:
     print('Дождались! Финальный a %s' %a)

