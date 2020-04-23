registry = []  # registry保存被 @register 装饰的函数引用。


def register(func):  # register 的参数是一个函数。
    print("running register(%s)" % func)  # 为了演示，显示被装饰的函数。
    registry.append(func)  # 把 func 存入 registry。
    return func  # 返回func：必须返回函数；这里返回的函数与通过参数传入的一样。


@register  # f1 和 f2 被 @register 装饰。
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():  # f3 没有装饰。
    print("running f3()")


def main():  # main 显示 registry，然后调用 f1()、f2() 和 f3()。
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()  # 只有把 registration.py 当作脚本运行时才调用 main()。
