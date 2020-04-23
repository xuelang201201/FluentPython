# 集合的本质是许多唯一对象的聚集。因此，集合可以用于去重。
my_list = ['spam', 'spam', 'eggs', 'spam']
print(set(my_list))
print(list(set(my_list)))

"""
例如，我们有一个电子邮件地址的集合（haystack），还要维护一个较小
的电子邮件地址集合（needles），然后求出 needles 中有多少地址同时
也出现在了 haystack 里。借助集合操作，我们只需要一行代码就可以了。
"""
# needles 的元素在 haystack 里出现的次数，两个变量都是 set 类型
# found = len(needles & haystack)

# 如果不使用交集操作的话，代码可能就变成了：
# needles 的元素在 haystack 里出现的次数（作用和上面相同）
# found = 0
# for n in needles:
#     if n in haystack:
#         found += 1

# needles 的元素在 haystack 里出现的次数，这次的代码可以用在任何可迭代对象上
# found = len(set(needles) & set(haystack))
# 另一种写法：
# found = len(set(needles).intersection(haystack))
