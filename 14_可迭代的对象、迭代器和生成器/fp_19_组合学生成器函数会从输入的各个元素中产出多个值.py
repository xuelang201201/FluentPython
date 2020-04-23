import itertools

# 'ABC' 中每两个元素（len()==2）的各个组合；在生成的元组中，元素的顺序无关紧要（可以视作集合）。
print(list(itertools.combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
# 'ABC' 中每两个元素（len()==2）的各种组合，包含相同元素的组合。
print(list(itertools.combinations_with_replacement('ABC', 2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(list(itertools.permutations('ABC', 2)))  # 'ABC' 中每两个元素（len()==2）的各种组合，包括相同元素的组合。
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(list(itertools.product('ABC', repeat=2)))  # 'ABC' 和 'ABC'（repeat=2 的效果）的笛卡儿积。
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
