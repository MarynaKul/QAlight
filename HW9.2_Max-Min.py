import operator
my_dict = {'a': 645, 'b': 3987, 'c': 93, 'd': 111, 'e': 646, 'f': 20}
new_dict = dict(sorted(my_dict.items(), key = operator.itemgetter(1), reverse=True)[:3])
for key in new_dict:
  print(key)
