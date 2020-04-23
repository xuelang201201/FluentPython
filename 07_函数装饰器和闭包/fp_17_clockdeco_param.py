# 参数化 clock 装饰器
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):  # clock 是参数化装饰器工厂函数。
    def decorate(func):  # decorate 是真正的装饰器。
        def clocked(*_args):  # clocked 包装被装饰的函数。
            t0 = time.time()
            _result = func(*_args)  # _result 是被装饰的函数返回的真正结果。
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # _args 是 clocked 的参数，args 是用于显示的字符串。
            result = repr(_result)  # result 是 _result 的字符串表示形式，用于显示。
            print(fmt.format(**locals()))  # 这里是使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量。
            return _result  # clocked 会取代被装饰的函数，因此它应该返回被装饰的函数返回的值。

        return clocked  # decorate 返回 clocked。

    return decorate  # clock 返回 decorate。


if __name__ == '__main__':

    @clock()  # 在这个模块中测试，不传入参数调用 clock()，因此应用的装饰器使用默认的格式 str。
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)
