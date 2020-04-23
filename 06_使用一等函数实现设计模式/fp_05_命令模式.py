# MacroCommand 的各个实例都在内部存储着命令模式
class MacroCommand:
    """一个执行一组命令的命令"""

    def __init__(self, commands):
        # 使用 commands 参数构建一个列表，这样能确保参数是可迭代对象，还能在各个 MacroCommand 实例中保存各个命令引用的副本。
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:  # 调用 MacroCommand 实例时，self.commands 中的各个命令依序执行。
            command()
