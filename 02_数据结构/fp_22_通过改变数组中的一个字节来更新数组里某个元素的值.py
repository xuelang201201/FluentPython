import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)  # 利用含有5个短整型有符号整数的数组（类型码是'h'）创建一个memoryview
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')  # 创建一个 memv_oct，这一次是把 memv 里的内容转换成'B'类型，也就是无符号类型
print(memv_oct.tolist())  # 以列表的形式查看 memv_oct的内容
memv_oct[5] = 4  # 把位于位置 5 的字节赋值成 4
print(numbers)  # 因为把占2个字节的整数的高位字节改成了4，所以这个有符号整数的值就变成了1024
# array('h', [-2, -1, 1024, 1, 2])
