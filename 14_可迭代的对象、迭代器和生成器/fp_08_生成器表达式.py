# 先在列表推导中使用 gen_AB 生成器函数，然后在生成器表达式中使用
def gen_AB():  # <1>gen_AB 函数与 fp_06 中的一样。
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


# <2>列表推导迫切地迭代 gen_AB() 函数生成的生成器对象产出的元素：'A' 和 'B'。注意，
# 下面的输出是 start、continue 和 end.。
res1 = [x * 3 for x in gen_AB()]
# start
# continue
# end.
for i in res1:  # <3>这个 for 循环迭代列表推导生成的 res1 列表。
    print('-->', i)
# --> AAA
# --> BBB
# <4>把生成器表达式返回的值赋值给 res2。只需调用 gen_AB() 函数，虽然调用时会返回一个生成器，但是这里并不使用。
res2 = (x * 3 for x in gen_AB())
print(res2)  # <5>res2 是一个生成器对象。
# <generator object <genexpr> at 0x7f8eb41a2740>
# <6>只有 for 循环迭代 res2 时，gen_AB 函数的定义体才会正真执行。for 循环每次迭代时会隐式调用 next(res2)，
# 前进到 gen_AB 函数中的下一个 yield 语句。注意，gen_AB 函数的输出与 for 循环中 print 函数的输出夹杂在一起。
for i in res2:
    print('-->', i)
# start
# --> AAA
# continue
# --> BBB
# end.
