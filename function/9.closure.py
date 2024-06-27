'''闭包满足条件
    1. 函数嵌套
    2. 内部函数作为返回值返回
    3. 内部函数用到外部函数变量'''

def fn():
    a = 10
    def inner():
        print(1, a)
        
    # 内部函数作为返回值
    return inner

# inner函数总是能访问到fn函数内部的变量(闭包)
fn()()

# 用例 求多个数平均值
nums = []
def get_avg(n):
    nums.append(n)
    return sum(nums)/len(nums)

print(get_avg(10))
print(get_avg(20))
nums = []
print(get_avg(50))

# 要保证nums数组不被别人改动, 放在函数内
def make_get_avg():
    nums = []
    def get_avg(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return get_avg

averager = make_get_avg()

print(averager(10))
print(averager(20))
print(averager(50))
