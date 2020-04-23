# 外面的列表其实包含3个指向同一个列表的引用。当我们不做修改的时候，看起来都还好。
weird_board = [['_'] * 3] * 3
print(weird_board)
# 一旦我们试图标记第1行第2列的元素，就立马暴露了列表内的3个引用指向同一个对象的事实。
weird_board[1][2] = '0'
print(weird_board)

# 等同于
row = ['_'] * 3
board = []
for i in range(3):
    # 追加同一行对象（row）3次到游戏板（board）。
    board.append(row)
print(board)
