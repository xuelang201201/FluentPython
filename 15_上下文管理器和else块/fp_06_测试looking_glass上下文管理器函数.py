from fp_05_mirror_gen import looking_glass

with looking_glass() as what:  # <1> 与示例 fp_03 唯一的不同是上下文管理器的名字：LookingGlass 变成了 looking_glass。
    print('Alice, Kitty and Snowdrop')
    print(what)
# pordwonS dna yttiK ,ecilA
# YKCOWREBBAJ
print(what)
# JABBERWOCKY
