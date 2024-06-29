class Dog:
    def __init__(self, name: str, age: int, gender: str, height: int) -> None:
        self.name = name 
        self.age = age
        self.gender = gender
        self.height = height
    
    def bark(self):
        print(f'{self.name} bark!')
    
    def bite(self):
        print(f'{self.name} bite')
        
    def run(self):
        print(f'{self.name} run')

dog1 = Dog('mary', 10, 'female', 150)
dog2 = Dog('Jack', 20, 'male', 90)

dog1.bark()
dog2.bite()