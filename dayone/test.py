import random

print(random.randint(1,5))


def add(x, y):
    return x + y


class Father():
    # 双下划线开始，结束的函数和属性，都是系统已经定义好的特殊属性和方法
    # 特殊方法：在特定场景自动调用
    # __init__用来初始化对象的属性，因此在创建对象时自动调用
    def __init__(self, name):
        print('__init__', id(self))
        # self代表当前对象
        self._name = name

    def __del__(self):
        # 此方法会在对象销毁时自动执行
        print('__del__')

    def _show(self):
        print('name', self._name)


f = Father('徐志强')
print(f, id(f))
f._show()


# 默认子类可以调用父类的属性和方法
# python 属性和方法如果是单下划线表示保护，双下划线表示私有（子类不可调用）
class Son(Father):
    def __init__(self, name, age):
        print('__init__', id(self))
        # self代表当前对象
        super().__init__(name)
        self.age = age

    def _show(self):
        print(f'name:{self._name},age:{self.age}')


s = Son('强仔', 18)
s._show()
