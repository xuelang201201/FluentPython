from inspect import signature


def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    :param text: 文本
    :param max_len: 文本最大长度
    :return: 截断位置
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


# 提取关于函数参数的信息
print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

# 提取函数的签名
sig = signature(clip)
print(sig)
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
