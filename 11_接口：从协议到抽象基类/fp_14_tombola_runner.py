# TODO 有问题不知道怎么解决：AttributeError: 'weakref' object has no attribute '__name__'
# Tombola 子类的测试运行程序

import doctest
import _abc

from fp_08_tombola import Tombola

# 要测试的模块
# 导入包含 Tombola 真实子类和虚拟子类的模块，用于测试。
import fp_10_bingo
import fp_11_lotto
import fp_12_tombolist
import fp_13_drum

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    # __subclasses__() 返回的列表是内存中存在的直接子代。即便源码中用不到想测试的模块，也要将其导入，因为要把那些类载入内存。
    real_subclasses = Tombola.__subclasses__()
    # 把 _abc_registry（WeakSet 对象）转换成列表，这样方能与 __subclasses__() 的结果拼接起来。
    virtual_subclasses = list(_abc._get_dump(Tombola)[0])

    for cls in real_subclasses + virtual_subclasses:  # 迭代找到的各个子类，分别传给 test 函数。
        test(cls, verbose)


def test(cls, verbose=False):

    res = doctest.testfile(
        TEST_FILE,
        # 把 cls 参数（要测试的类）绑定到全局命名空间里的 ConcreteTombola 名称上，供 doctest 使用。
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    # 输出测试结果，包含类的名称、尝试运行的测试数量、失败的测试数量，以及 'OK' 或 'FAIL' 标记。
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == '__main__':
    import sys

    main(sys.argv)
