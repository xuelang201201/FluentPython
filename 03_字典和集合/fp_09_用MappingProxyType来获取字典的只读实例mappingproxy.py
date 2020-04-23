from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])  # d 中的内容可以通过 d_proxy 看到。
# d_proxy[2] = 'x'  # 但是通过 d_proxy 并不能做任何修改。
d[2] = 'B'
print(d_proxy)  # d_proxy 是动态的，也就是说对 d 所做的任何改动都会反馈到它上面。
print(d_proxy[2])
