class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
# Gizmo id: 4301489152  # 输出的 Gizmo id: ... 是创建 Gizmo 实例会抛出异常。
# y = Gizmo() * 10  # 在乘法运算中使用 Gizmo 实例会抛出异常。
# Gizmo id: 4301489432  # 这里表明，在尝试求积之前其实会创建一个新的 Gizmo 实例。
# Traceback (most recent call last):
#   File "<stdin>", line 8, in <module>
#     y = Gizmo() * 10
# TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'

print(dir())  # 但是，肯定不会创建变量 y，因为在对赋值语句的右边进行求值时抛出了异常。
# ['Gizmo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'x']
