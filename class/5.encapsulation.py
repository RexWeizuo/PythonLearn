'''封装指的是隐藏对象中一些不希望被外部访问的属性和方法(只读)
    1. 将对象的属性名修改为一个外部不知道的名字
    2. 提供getter(获取指定属性)和setter(设置指定属性)使外部可以访问到属性'''
    
class Dog:
    def __init__(self, name: str, age: int) -> None:
        # self.name = name 
        self.hidden_name = name
        self.hidden_age = age
    
    def bark(self):
        print(f'{self.hidden_name} bark!')
        
    def get_name(self):
        return self.hidden_name
    
    def set_name(self, name):
        self.hidden_name = name
        
    def get_age(self):
        return self.hidden_age
    
    def set_age(self, age):
        '''使用setter方法增加其他处理(比如数据验证): 检查age是否是正数'''
        if age > 0:
            self.hidden_age = age
            
d = Dog('旺财', 8)
d.name = '小黑'
d.set_name('小红')

d.bark()
print(d.get_name())

d.get_age()
d.set_age(-10)

class Rectangle:
    def __init__(self, width, height) -> None:
        self.hidden_width = width
        self.hidden_height = height
        
    def get_width(self):
        return self.hidden_width
    
    def get_height(self):
        return self.hidden_height
    
    def set_width(self, width):
        self.hidden_width = width
        
    def set_height(self, height):
        self.hidden_height = height
        
    # 获取矩形面积的方法
    def get_area(self):
        return self.hidden_height * self.hidden_width
    
r = Rectangle(5,2)
r.set_height(10)
r.set_width(20)

print(r.get_area())
