# 没有指向对象的引用时，监视对象生命结束时的情形
import weakref

s1 = {1, 2, 3}
s2 = s1  # s1 和 s2 是别名，指向同一个集合，{1, 2, 3}。


def bye():  # 这个函数一定不能是要销毁的对象的绑定方法，否则会有一个指向对象的引用。
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)  # 在 s1 引用的对象上注册 bye 回调。
print(ender.alive)  # 调用 finalize 对象之前，.alive 属性的值为 True。
del s1
print(ender.alive)  # 如前所述，del 不删除对象，而是删除对象的引用。
# 重新绑定最后一个引用 s2，让 {1, 2, 3} 无法获取。对象被销毁了，调用了 bye 回调，ender.alive 的值变成了 False。
s2 = 'spam'
print(ender.alive)
