import copy


class Man:
    def __init__(self, name, ids):
        self.name = name
        self.ids = ids


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
man = Man('tester', numbers)

man.ids = numbers
print(man.name)
print()
print('begin ok.')
count = 0

for item in man.ids:
    print('count:[%d]-number:[%d]' % (count, item))
    count += 1
print()
print('del now.')

count = 0
for item in man.ids:
    print('count:[%d]-number:[%d]' % (count, item))
    count += 1
    if item % 2 == 0:
        man.ids.remove(item)
    else:
        man.ids[item] = -1
        print('-1 !!!')


print()
print('del ok.')
count = 0
for item in man.ids:
    print('count:[%d]-number:[%d]' % (count, item))
    count += 1
print()

###
print("new for")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
man.ids = numbers
print(man.name)

print()
print('begin ok.')
count = 0
for item in man.ids:
    print('count:[%d]-number:[%d]' % (count, item))
    count += 1

print()
print('del now.')
count = 0
ids_copy = copy.deepcopy(man.ids)
for item in ids_copy:
    print('count:[%d]-number:[%d]' % (count, item))
    count += 1
    if item % 2 == 0:
        if (item in man.ids):
            man.ids.remove(item)
    else:
        if (item in man.ids):
            man.ids[man.ids.index(item)] = -1
            print('-1 !!!')


print()
print('del ok.')
count = 0
for item in man.ids:
    print('count:[%d]-number:[%d]' % (count, item))
    count += 1
print()
