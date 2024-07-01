class A(object):
    '''多个父类中有同名的方法，会优先用()中的第一个父类的方法
       前面父类的方法会覆盖后面'''
    def test(self):
        print('AAA')
        
class B(object):
    def test(self):
        print('B中的test方法')
        
    def test2(self):
        print('BBB')

'''多重继承,子类继承所有父类的属性和方法
但应该尽量避免多重继承，会使代码过于复杂'''
class C(A, B):
    pass

'''类名.__bases__这个属性用来获取当前类所有父类'''
print(C.__bases__) # (<class '__main__.A'>, <class '__main__.B'>)
c = C()
c.test()
c.test2()