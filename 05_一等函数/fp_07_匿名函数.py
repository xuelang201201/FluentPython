# 使用 lambda 表达式反转拼写，然后依此给单词列表排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))
