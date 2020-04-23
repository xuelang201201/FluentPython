charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles  # lewis 是 charles 的别名。
print(lewis is charles)
print(id(charles), id(lewis))  # is 运算符和 id 函数确认了这一点。
lewis['balance'] = 950  # 向 lewis 中添加一个元素相当于向 charles 中添加一个元素。
print(charles)
