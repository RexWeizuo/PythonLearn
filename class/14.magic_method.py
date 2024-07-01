'''特殊方法会在一些特殊情况下自动调用'''

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    '''尝试将对象转换为字符串时调用 (print函数)
    可以指定转换的结果'''
    def __str__(self):
        return f'Person{self.name, self.age}'
    
    '''对当前函数使用repr()函数时调用
    作用:指定对象在 交互模式 中直接输出的效果'''
    def __repr__(self) -> str:
        return 'hello call repr'
    
    '''返回比较的结果
    self和other相比'''
    def __gt__(self, other):
        return self.age > other.age
    
    '''可以通过bool来指定对象转换为布尔值的情况'''
    def __bool__(self):
        return self.age > 30

p1 = Person('sask', 31)
p2 = Person('krystal',30)

'''打印对象时，实际上打印的是__str__()的返回值'''
print(p1) # <__main__.Person object at 0x0000018483683810>
print(str(p1))
print(repr(p1))

print(p1 > p2)
print(bool(p2))