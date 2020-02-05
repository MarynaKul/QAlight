Europe = {'Austria': 'Vienna',
        'Belgium': 'Brussels',
        'Bulgaria': 'Sofia',
        'Denmark': 'Copenhagen'}

America = {'Brazil': 'Brasilia',
           'Canada': 'Ottawa',
           'USA': 'Washington'}

Africa = {'Egypt': 'Cairo',
          'Ethiopia': 'Addis Ababa',
          'Ghana': 'Accra',
          'Oman': 'Muscat'}

def worldList(a, b, c):
    world = dict(list(a.items()) + list(b.items()) + list(c.items()))
    print(world)
