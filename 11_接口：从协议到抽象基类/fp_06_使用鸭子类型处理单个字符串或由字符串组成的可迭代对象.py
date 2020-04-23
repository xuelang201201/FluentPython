# 这段代码摘自示例 21-2。
def record_factory(cls_name, field_names):
    try:  # 假设是单个字符串（EAFP 风格，即 “取得原谅比获得许可容易”）。
        field_names = field_names.replace(',', ' ').split()  # 把逗号替换成空格，然后拆分成名称列表。
    except AttributeError:  # 抱歉，field_names 看起来不像是字符串……没有 .replace 方法，或者返回值不能使用 .split 方法拆分。
        pass  # 假设已经是由名称组成的可迭代对象了。
    field_names = tuple(field_names)  # 为了确保的确是可迭代对象，也为了保存一份副本，使用所得值创建一个元组。
