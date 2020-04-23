# WeakValueDictionary 简介
# Cheese 有个 kind 属性和标准的字符串表示形式


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind
