# 建立一个包含3个列表的列表，被包含的3个列表各自有3个元素。打印出这个嵌套列表。
board = [['_'] * 3 for i in range(3)]
print(board)
# 把第1行第2列的元素标记为 X，再打印出这个列表。
board[1][2] = 'X'
print(board)

# 等同于
board = []
for i in range(3):
    # 每次迭代中都新建了一个列表，作为新的一行（row）追加到游戏板（board）。
    row = ['_'] * 3
    board.append(row)
print(board)
board[2][0] = 'X'
# 正如我们所期待的，只有第2行的元素被修改。
print(board)

