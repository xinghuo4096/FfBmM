# python 使用for和 list的注意事项

## 现象

下面程序中的`print('-1 !!!')` **不会被执行**
当for对象是实例列表时问题比较明显

## 原因

python时动态执行，for循环条件判断变化时有问题。

## 解决

个人是用 copy.deepcopy 解决的

## 现象程序和输出

```python
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
```

输出结果：

``` text
tester

begin ok.
count:[0]-number:[0]
count:[1]-number:[1]
count:[2]-number:[2]
count:[3]-number:[3]
count:[4]-number:[4]
count:[5]-number:[5]
count:[6]-number:[6]
count:[7]-number:[7]
count:[8]-number:[8]
count:[9]-number:[9]
count:[10]-number:[10]

del now.
count:[0]-number:[0]
count:[1]-number:[2]
count:[2]-number:[4]
count:[3]-number:[6]
count:[4]-number:[8]
count:[5]-number:[10]

del ok.
count:[0]-number:[1]
count:[1]-number:[3]
count:[2]-number:[5]
count:[3]-number:[7]
count:[4]-number:[9]
```
