class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def run(self):
        print('animal run')
    
    def sleep(self):
        print('animal sleep')
    
    def bark(self):
        print('animal bark')

'''通过继承子类可以获取到其父类的属性和方法'''
class Dog(Animal):
    '''方法重写(overwrite)'''
    def bark(self):
        print('wangwangwang')
        
class Hashiqi(Dog):
    def fansha(self):
        print('你礼貌吗')

# 魔术方法init也被继承
d = Dog('x')
h = Hashiqi('y')

d.run()
d.sleep()
'''同名方法如果是通过子类实例调用，会调用子类方法'''
d.bark() # wangwangwang
print(isinstance(d, Animal))
'''优先找子类->父类->祖父类->...->object'''
h.bark() # wangwangwang
h.run()
print(issubclass(Hashiqi, Animal))

'''obeject是所有类的父类
   所有对象都是object的实例'''
print(isinstance(print, object))

