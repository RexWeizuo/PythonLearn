class Person:
    '''特殊方法 魔术方法
       创建实例对象时,init初始化方法自动调用
       1. 特殊方法什么时候调用(在实例对象创建以后立刻执行)
       2. 特殊方法有什么作用(通过self给新建的实例对象初始化属性)
    '''
    
    def __init__(self, name):
        # print('init方法执行了')
        self.name = name
    
    def say_hello(self):
        print(f'hello, {self.name}')

'''p1 = Person()的运行流程
    1. 创建变量p1
    2. 内存中创建一个新对象
    3. 特殊方法init(self)执行(它会在实例对象创建以后立刻执行)
    4. 将对象id赋值给变量'''
p1 = Person(name = 'we')
p2 = Person('ss')
# p1.name = 'we'
# p2.name = 'ss'
'''手动给对象添加name属性太繁琐'''

p2.say_hello()
# p1.__init__()

