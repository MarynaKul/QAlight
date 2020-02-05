def calculate(inputSec):
    days = int(inputSec//86400)
    hours = int((inputSec - days*86400)//3600)
    mins = int(((inputSec - days*86400) - hours*3600)//60)
    sec = int(((inputSec - days*86400) - hours*3600) - mins*60)
    a = str(str(days) + ' days: ' + str(hours) + ' h: ' + str(mins) + ' m: ' + str(sec) + ' s ')
    print(a)
