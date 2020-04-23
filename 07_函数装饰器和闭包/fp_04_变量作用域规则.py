# 一个函数，读取一个局部变量和一个全局变量
# def f1(a):
#     print(a)
#     print(b)


# print(f1(3))
# 3
# Traceback (most recent call last):
#   File "E:/Python/Code/Fluent Python/07_函数装饰器和闭包/fp_04_变量作用域规则.py", line 7, in <module>
#     print(f1(3))
#   File "E:/Python/Code/Fluent Python/07_函数装饰器和闭包/fp_04_变量作用域规则.py", line 4, in f1
#     print(b)
# NameError: name 'b' is not defined


# 如果先给全局变量 b 赋值，然后再调用 f1，那么就不会出错：
# b = 6
# print(f1(3))
# 3
# 6


# b 是局部变量，因为在函数的定义体中给它赋值了
# b = 6


# def f2(a):
#     print(a)
#     print(b)
#     b = 9


# print(f2(3))
# 3
# Traceback (most recent call last):
#   File "E:/Python/Code/Fluent Python/07_函数装饰器和闭包/fp_04_变量作用域规则.py", line 29, in <module>
#     print(f2(3))
#   File "E:/Python/Code/Fluent Python/07_函数装饰器和闭包/fp_04_变量作用域规则.py", line 25, in f2
#     print(b)
# UnboundLocalError: local variable 'b' referenced before assignment


b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


print(f3(3))
# 3
# 6
print(b)
# 9

print(f3(3))
# 3
# 9
b = 30
print(b)
# 30
