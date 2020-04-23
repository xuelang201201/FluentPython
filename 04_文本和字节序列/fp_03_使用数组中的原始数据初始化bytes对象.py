import array

numbers = array.array('h', [-2, -1, 0, 1, 2])  # 指定类型代码 h，创建一个短整数（16位）数组。
octets = bytes(numbers)  # octets 保存组成 numbers 的字节序列的副本。
print(octets)
# b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'  这些是表示那 5 个短整数的 10 个字节。
