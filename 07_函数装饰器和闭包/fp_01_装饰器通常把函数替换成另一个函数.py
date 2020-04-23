def deco(func):
    def inner():
        print("running inner()")

    return inner  # deco 返回 inner 函数对象。


@deco
def target():  # 使用 deco 装饰 target。
    print("running target()")


print(target())  # 调用被装饰的 target 其实会运行 inner。
print(target)  # 审查对象，发现 target 现在是 inner 的引用。
