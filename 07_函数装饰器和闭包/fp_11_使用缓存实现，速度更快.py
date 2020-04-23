import functools

from fp_08_使用clock装饰器 import clock


@functools.lru_cache()  # 注意，必须像常规函数那样调用 lru_cache。这一行中有一对括号：@functools.lru_cache()。可以接收参数。
@clock  # 这里叠放了装饰器：@lru_cache() 应用到 @clock 返回的函数上。
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
