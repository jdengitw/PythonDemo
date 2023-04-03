class PrefixMetaclass(type):

    def __new__(cls, name, bases, attrs):
        # 给所有属性和方法前面加上前缀 my_
        _attrs = (('my_' + name, value) for name, value in attrs.items())
        _attrs = dict((name, value) for name, value in _attrs)  # 转化为字典
        _attrs['echo'] = lambda self, phrase: phrase  # 增加了一个 echo 方法
        return type.__new__(cls, name, bases, _attrs)  # 返回创建后的类


class Animal(object):

    def __init__(self, name):
        self.name = name.upper()
        self.__name = name  # private
        self._age = 0

    def greet(self):
        print('Hello, I am %s.' % self.name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if val < 0:
            self._age = 0
        elif val > 100:
            self._age = 100
        else:
            self._age = val


class Dog(Animal):

    def greet(self):
        print(super().greet())
        print('WangWang.., I am %s. ' % self.name)


class Cat(Animal):
    Name = 'kitty'

    def greet(self):
        print('MiaoMiao.., I am %s' % self.name)

    @classmethod
    def CGreet(cls):
        print('MiaoMiao.., I am %s' % cls.Name)

    @staticmethod
    def SGreet():
        print('MiaoMiao.., I am %s' % Cat.Name)


def hello(animal):
    animal.greet()


animal = Animal('animal')
print(type(animal))
print(dir(animal))
animal.name
dog = Dog('dog')
cat = Cat('cat')

animal.greet()
dog.greet()
cat.greet()
Cat.SGreet()
Cat.CGreet()

animal.age = -1
print(animal.age)
""" d = {'name': 'ethan', 'age': 20}
print(d.keys())
print(d.values())
for k, v in d.items():
    print('%s: %s' % (k, v))
d.pop('name')
print(d.keys())
d['name'] = 'Jason'
print(d.keys()) """
""" students = [{
    'name': 'john',
    'score': 'B',
    'age': 15
}, {
    'name': 'jane',
    'score': 'A',
    'age': 12
}, {
    'name': 'dave',
    'score': 'B',
    'age': 10
}, {
    'name': 'ethan',
    'score': 'C',
    'age': 20
}, {
    'name': 'peter',
    'score': 'B',
    'age': 20
}, {
    'name': 'mike',
    'score': 'C',
    'age': 16
}]
a=sorted(students, key=lambda stu: (stu['score'], -stu['age']))
print(a) """
""" s1 = set(['.mp3', '.mp4', '.rmvb', '.mp3'])  # 使用 set()，接收一个列表
print(s1)
s2 = set(['.mkv', '.mp4', '.mkv', '.mp3'])  # 使用 set()，接收一个列表
s3 = s1 | s2
print(s3)
print(s3.issuperset(s2)) """

table = str.maketrans('aeiou', '12345')
motto = 'to be or not to be, that is a question'
print(motto.translate(table))
""" try:
    x = input('Enter x: ')
    y = input('Enter y: ')
    print(int(x) / int(y))
    print(x / y)
except ZeroDivisionError as e:
    print('Error:', e)
except TypeError as e:
    print('TypeError:', e)
except BaseException as e:
    print('BaseException:', e)
finally:
    print('Done') """

import base64

with open('cover.png', 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data)  # 使用 base64 编码
    print(base64_data)
with open('cover_copy.png', 'wb') as f:
    f.write(base64.b64decode(base64_data, altchars=None, validate=False))
