class Animal:
    def __init__(self, name) -> None:
        self._name = name
    
    def run(self):
        print('animal run')
    
    def sleep(self):
        print('animal sleep')
    
    def bark(self):
        print('animal bark')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    

class Dog(Animal):
    '''重写特殊方法init'''
    def __init__(self, name, age) -> None:
        '''父类中初始化了name,子类初始化了age
        希望子类调用父类__init__初始化父类中定义的属性'''
        # 耦合写法
        # Animal.__init__(self, name)
        '''super()可以获取当前类的父类,通过super返回对象父类方法时,不需要传递self'''
        super().__init__(name)
        self._age = age
        
    def bark(self):
        print('wangwangwang')
        
    def run(self):
        print('dog run')
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def name(self, age):
        self._age = age
        
d = Dog('a', 10)
d.name = 'b'
d.age = 15 
    