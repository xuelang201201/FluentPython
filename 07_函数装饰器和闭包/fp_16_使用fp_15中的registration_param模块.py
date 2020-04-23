from fp_15_registration_param import *
# out: running register(active=False)->decorate(<function f1 at 0x000001AB31807940>)
#      running register(active=True)->decorate(<function f2 at 0x000001AB318079D0>)

print(registry)  # 导入这个模块时，f2 在 registry 中。
# out: {<function f2 at 0x000001AB318079D0>}

print(register()(f3))  # register() 表达式返回 decorate，然后把它应用到 f3 上。
# out: running register(active=True)->decorate(<function f3 at 0x000001AB318078B0>)
#      <function f3 at 0x000001AB318078B0>

print(registry)  # 前一行把 f3 添加到 registry 中。
# out: {<function f3 at 0x000001AB318078B0>, <function f2 at 0x000001AB318079D0>}

print(register(active=False)(f2))  # 这次调用从 registry 中删除 f2。
# out: running register(active=False)->decorate(<function f2 at 0x000001AB318079D0>)
#      <function f2 at 0x000001AB318079D0>

print(registry)  # 确认 registry 中只有 f3。
# out: {<function f3 at 0x000001AB318078B0>}
