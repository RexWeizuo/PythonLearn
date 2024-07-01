'''一个对象可以以不同的形态去呈现'''
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal: Animal):
    print(animal.speak())

# 创建 Dog 和 Cat 类的实例
dog = Dog()
cat = Cat()

# 调用相同的方法，但表现不同
'''函数的通用性提高'''
'''虽然调用的是同一个方法 speak()，但由于多态的存在，
函数会根据传入对象的实际类型调用相应的实现。'''
make_animal_speak(dog)  # 输出: Woof!
make_animal_speak(cat)  # 输出: Meow!

class A:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
class B:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

class C:
    pass
        
a = A('krystal')
b = B('sask')
c = C()

'''只要对象中有name属性,它就可以作为参数传递
该函数不会考虑对象的类型,只要有name属性即可'''
def say_hello(obj):
    print(f'hello{obj.name}')
   
def say_hello2(obj, A):
    '''做类型检查, 只有obj是A类型的对象时才可以正常使用
    其他类型的对象都无法使用该函数, 违反了多态'''
    if isinstance(obj, A):
        print(f'hello{obj.name}')
    
say_hello(a)
say_hello(b)
# say_hello(c)

'''如果一个东西，走路像鸭子，叫声像鸭子，那就当它是鸭子
   我们只考虑对象的属性和方法'''
   
'''len可以获取列表和字符串的长度
因为这些对象中都具有特殊方法__len__
不需要考虑参数的具体类型'''
l = [1,2,3]
s = 'hello'
print(len(l))
print(len(s))

from abc import ABC, abstractmethod

'''抽象基类 Payment:
使用 ABC 模块定义一个抽象基类 Payment，并定义了一个抽象方法 pay。所有继承 Payment 的子类都必须实现这个方法。'''
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

'''具体支付方式类：
CreditCardPayment、PayPalPayment 和 CryptoPayment 类继承自 Payment，并实现了 pay 方法。
每个类有自己的支付处理逻辑。'''
# 信用卡支付类
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")

# PayPal 支付类
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# 加密货币支付类
class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Processing cryptocurrency payment of ${amount}")

'''支付处理函数 process_payment：
该函数接受一个 Payment 对象和支付金额 amount。调用传入对象的 pay 方法来处理支付。'''
def process_payment(payment: Payment, amount):
    payment.pay(amount)

'''创建不同支付方式的实例，并使用 process_payment 函数处理支付。
无论传入的是哪种支付方式，process_payment 函数都可以正确调用相应的 pay 方法。'''
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
crypto_payment = CryptoPayment()

# 处理不同类型的支付
process_payment(credit_card_payment, 100.0)  # 输出: Processing credit card payment of $100.0
process_payment(paypal_payment, 200.0)       # 输出: Processing PayPal payment of $200.0
process_payment(crypto_payment, 300.0)       # 输出: Processing cryptocurrency payment of $300.0

'''
灵活性：
新增支付方式时，只需添加新的支付类并实现 pay 方法，而无需修改现有的代码。

代码复用：
process_payment 函数可以处理任何实现了 Payment 接口的支付方式，避免了重复代码。

易于维护：
每种支付方式的实现都独立封装在各自的类中，修改某一种支付方式的实现不会影响其他支付方式。

通过这个例子，我们可以看到多态的实际应用如何使代码更加灵活、可扩展和易于维护。无论我们需要添加多少种支付方式，都只需实现 Payment 接口即可，
这大大提高了系统的可扩展性和可维护性。'''