from datetime import datetime

brl = 1 / 2.43  # BRL到USD的货币兑换比价
print(brl)
print(format(brl, '0.4f'))  # 格式说明符是 '0.4f'。
# 格式说明符是 '0.2f'。代换字段中的 'rate' 子串是字段名称，与格式说明符无关，
# 但是它决定把 .format() 的哪个参数传给代换字段。
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

print(format(42, 'b'))
print(format(2 / 3, '.1%'))

now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))
