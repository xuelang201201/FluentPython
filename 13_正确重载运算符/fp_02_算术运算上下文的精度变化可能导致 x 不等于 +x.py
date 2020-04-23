import decimal
ctx = decimal.getcontext()  # <1> 获取当前全局算数运算的上下文引用。
ctx.prec = 40  # <2> 把算术运算上下文的精度设为 40。
one_third = decimal.Decimal('1') / decimal.Decimal('3')  # <3> 使用当前精度计算 1/3。
print(one_third)  # <4> 查看结果，小数点后有 40 个数字。
# 0.3333333333333333333333333333333333333333
print(one_third == +one_third)  # <5> one_third == +one_third 返回 True。
# True
ctx.prec = 28  # <6> 把精度降低为 28，这是 Python 为 Decimal 算术运算设定的默认精度。
print(one_third == +one_third)  # <7> 现在，one_third == +one_third 返回 False。
# False
print(+one_third)  # <8> 查看 +one_third，小数点后有 28 个数字。
# 0.3333333333333333333333333333
