'''
    希望在计算前打印开始计算，计算结束后打印结束计算
    OCP原则:open close 对已有函数只能做扩展不能做修改
'''


# 无参数函数扩展
def fn():
    print("function fn")
    
# def fn2():
#     print("start")
#     fn()
#     print("end")

# fn2()


# 有参数函数扩展
def add(a, b):
    r = a + b
    return r

# def new_add(a,b):
#     print("start")
#     r = add(a, b)
#     print("end")
#     return r
    
# r = new_add(1, 45)
# print(r)


''' 对每一个函数扩展都要手动创建新函数，下为更简便方法
    把要扩展的函数对象作为参数传递
    类似begin_end()这种函数被称为装饰器'''
def begin_end(old_fn):
    def new_fn(*args, **kwargs):
        print('start')
        r = old_fn(*args, **kwargs)
        print('end')
        return r
    return new_fn

f1 = begin_end(fn)
f2 = begin_end(add)
# print(f2(1,2))

# @begin_end
# def say_hello():
#     print("hello")
    
# say_hello()

@begin_end
def mul(a, b):
    print(a*b)

mul(3,4)

'''带参数的装饰器
如果需要向装饰器传递参数，可以再封装一层函数。'''
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


'''实际应用示例
    1.日志记录'''
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(3, 5)

'''权限验证'''
def requires_permission(func):
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        if user != 'admin':
            print("Permission denied")
            return
        return func(*args, **kwargs)
    return wrapper

@requires_permission
def delete_file(filename, user):
    print(f"{filename} has been deleted.")

delete_file("test.txt", user="admin")
delete_file("test.txt", user="guest")


'''缓存'''
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


