'''属性和方法的访问控制：
公有（public）：可以从类的外部访问。
受保护（protected）：约定使用单下划线前缀 _ 表示，提醒使用者该属性或方法不应从类外部访问，但这只是一个约定，并不强制。
私有（private）：使用双下划线前缀 __ 表示，实际在类的外部不能直接访问。'''
    
class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
p = Person('krystal')
# 访问不到
# print(p.__name)
# 本质上
print(p._Person__name)
print(p.get_name()) 

class Dog:
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
d = Dog('小黑')
print(d._name)