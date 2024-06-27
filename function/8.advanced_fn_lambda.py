l = [1,2,3,4,5,6,7,8,9,10]
"""函数作为参数 匿名函数 filter map sort"""

# 查找偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False

# 查找大于5的数
def fn3(i):
    return i > 5

# 根据不同规则查找
def fn(func, lst):
    
    new_lst = []
    
    for i in lst:
        # 太妙了，在这里直接把fn2函数内容传了进来
        if func(i):
            new_lst.append(i)
    return new_lst

# 传入不同的函数作为参数
print(fn(fn2, l))
print(list(filter(fn3, l)))


# 匿名函数一般作为参数使用
# lambda函数（参数列表：返回值），函数创建另一种方式
def fn5(a, b):
    return a + b

# (lambda a,b : a+b)(10,20)
fn6 = lambda a,b : a+b
filter(fn6, l)

# 迭代器在这里先不提
filter(lambda i : i % 3, l)

# map()对可迭代对象中所有元素做指定操作，并将其添加到一个新对象中返回
r = map(lambda i: i+1, l)

str_list = ['a', 's', 'gg', 'fff']
# sort 关键词参数key
# key需要函数作为参数，sort会以函数的返回值来比较大小
str_list.sort(key=len)
str_list.sort(key=int)

# sorted可以对任意序列进行排序，不影响原来对象，返回新对象(新的list)
sorted(l, key=int)

'''匿名函数用处
    1. 排序'''
# 一组学生的名字和成绩
students = [("Alice", 85), ("Bob", 75), ("Charlie", 95)]
# 按成绩排序
sorted_students = sorted(students, key=lambda student: student[1])
sorted_students = students.sort(key=lambda student: student[1])
print(sorted_students)


'''2.map数据处理'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


'''3.过滤'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


'''4.pandas数据分析'''
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 75, 95]}
df = pd.DataFrame(data)
# 使用匿名函数增加一个新列，判断成绩是否及格
df['Passed'] = df['Score'].apply(lambda x: x >= 80)
print(df)


