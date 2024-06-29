class Person:
    # 类中定义的变量，将会成为所有实例的公共属性
    a = 10
    b = 20
    
    # 类中定义的函数称为方法，所有实例都可以访问
    # 方法默认传递一个参数(调用方法的对象本身)，所以方法中至少要定义一个形参
    def say_hello(self):
        print(f'hello, {self.name}')

p1 = Person()
p2 = Person()
p1.name = 'sfa'
p2.name = 'gew'

# print(p1.a)
p1.say_hello()
p2.say_hello()

'''属性和方法查找流程
当调用一个对象的属性时，解析器会先在当前对象中寻找是否有该属性
    有则直接返回当前对象属性值
    没有则去当前对象类对象中寻找，返回类对象属性值'''

