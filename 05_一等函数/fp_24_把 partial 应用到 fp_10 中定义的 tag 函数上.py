from tagger import tag
from functools import partial

print(tag)
# out: <function tag at 0x0000026196BDBCA0>  从 tagger.py 中导入 tag 函数，查看它的 ID。

# 使用 tag 创建 picture 函数，把第一个定位参数固定为 'img'，把 cls 关键字参数固定为 'pic-frame'。
picture = partial(tag, 'img', cls='pic-frame')

print(picture(src='wumpus.jpeg'))
# out: <img class="pic-frame" src="wumpus.jpeg" />  # picture 的行为符合预期。

print(picture)
# partial() 返回一个 functools.partial 对象。
# out: functools.partial(<function tag at 0x000001CF92D2BCA0>, 'img', cls='pic-frame')

print(picture.func)  # functools.partial 对象提供了访问原函数和固定参数的属性。
# out: <function tag at 0x000002060CB7BCA0>

print(picture.args)
print(picture.keywords)
