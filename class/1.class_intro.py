a = int(10)
b = str('hello')
print(a, type(a))
print(b, type(b))

# 定义自己的类
class MyClass():
    pass

# 使用Myclass创建一个对象, mc是Myclass类的实例
mc = MyClass()

# <__main__.MyClass object at 0x000001FF488FEF90> 对象就是‘内存’
# <class '__main__.MyClass'> 
print(mc, type(mc))

# isinstance()用来检查一个对象是否是一个类的实例
print(isinstance(mc, MyClass))

# class 'type'
print(id(MyClass), type(MyClass))