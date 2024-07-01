class A:
    count = 10
    
    def __init__(self) -> None:
        '''实例属性，通过实例对象添加的属性'''
        self.name = 'sask'
    
    '''实例方法: 在类中定义, 以self作为第一个参数的方法''' 
    def test(self):
        print('This is a test method', self)
        
    '''类方法:在类内部使用@classmethod修饰的方法
    cls(当前类对象A)也会被自动传递'''
    @classmethod
    def test_2(cls):
        print('This is a class method', cls)
        print(cls.count)
        
    '''静态方法 @staticmethod
    静态方法不需要指定任何默认参数, 静态方法可以通过类和实例调用
    静态方法基本上当前类无关的方法(像函数), 只是保存到当前类中的函数'''
    @staticmethod
    def test_3():
        print('this is staticmethod')
    
a = A()
'''通过实例对象添加的属性属于实例属性'''
a.count = 0
'''类属性可以通过类或者类的实例访问到
但是类属性只能通过类对象修改，无法通过实例对象修改'''
print(A.count)
print(a.count)

print(a.name)
'''实例属性只能通过实例对象来访问，类对象无法访问修改'''
# print(A.name)

'''实例方法通过实例调用, 自动传self参数'''
a.test()
'''实例方法通过类调用, 必须手动传self参数'''
A.test(a)

A.test_2()
'''类方法可以通过类调用，也可以通过实例调用，没有区别'''
a.test_2()

A.test_3()
a.test_3()