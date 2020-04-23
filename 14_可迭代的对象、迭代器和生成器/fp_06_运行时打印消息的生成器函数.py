def gen_AB():  # <1>定义生成器函数的方式与普通的函数无异，只不过要使用 yield 关键字。
    print('start')
    yield 'A'  # <2>在 for 循环中第一次隐式调用 next() 函数时(<5>)，会打印 'start'，然后停在第一个 yield 语句，生成值 'A'。
    print('continue')
    yield 'B'  # <3>在 for 循环中第二次隐式调用 next() 函数是，会打印 'continue'，然后停在第二个 yield 语句，生成值 'B'。
    # <4>第三次调用 next() 函数时，会打印 'end.'，然后到达函数定义体的末尾，导致生成器对象抛出 StopIteration 异常。
    print('end.')


for c in gen_AB():  # <5>迭代时，for 机制的作用与 g = iter(gen_AB()) 一样，用于获取生成器对象，然后每次迭代时调用 next(g)。
    print('-->', c)  # <6>循环块打印 --> 和 next(g) 返回的值。但是，生成器函数中的 print 函数输出结果之后才会看到这个输出。

# start  <7>'start' 是生成器函数定义体中 print('start') 输出的结果。
# --> A  <8>生成器函数定义体中的 yield 'A' 语句会生成值 A，提供给 for 循环使用，而 A 会赋值给变量 c，最终输出 --> A。
# <9>第二次调用 next(g)，继续迭代，生成器函数定义体中的代码由 yield 'A' 前进到 yield 'B'。文本 continue 是
# 由生成器函数定义体中的第二个 print 函数输出的。
# continue
# --> B  <10>yield 'B' 语句生成值 B，提供给 for 循环使用，而 B 会赋值给变量 c，所以循环打印出 --> B。
# end.  <11>第三次调用 next(it)，继续迭代，前进到生成器函数的末尾。文本 end. 是由生成器函数定义体中的第三个 print 函数输出的。
# <12>到达生成器函数定义体的末尾时，生成器对象抛出 StopIteration 异常。for 机制会捕获异常，因此循环终止时没有报错。
