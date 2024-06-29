class Person:
    def __init__(self, name: str, age:int) -> None:
        self._name = name
        self._age = age
    
    '''将get方法转换为对象的属性
    使用property装饰的方法,必须和属性名一样'''
    @property
    # getter方法不写get
    def name(self):
        return self._name
    
    '''setter方法装饰器:@属性名.setter'''
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    # getter方法不写get
    def age(self):
        return self._age
    
    '''setter方法装饰器:@属性名.setter'''
    @age.setter
    def age(self, age):
        self._age = age
        
p = Person('sask', 10)
p.name = 'fenfenko'
p.age = 28

'''加了property装饰器以后,可以像调用属性一样使用get方法'''
print(p.name, p.age)