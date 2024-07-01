'''程序运行过程中产生的垃圾(没用的东西)会影响程序的运行性能
   垃圾对象从内存中删除'''
class A:
    def __init__(self) -> None:
        self.name = 'A类'
    
    '''del方法会在对象被垃圾回收前调用'''
    def __del__(self):
        print('A()对象被删除了',self)

a = A()
print(a.name)

'''此时没有任何变量对A()对象进行引用就是垃圾了'''
a = None
input('回车键退出。。')

'''python自动的垃圾回收机制'''