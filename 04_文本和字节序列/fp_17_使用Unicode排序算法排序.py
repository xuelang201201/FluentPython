# 使用 pyuca.Collator.sort_key 方法
import pyuca

coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)

fruits = ['苹果', '香蕉', '西瓜', '梨', '葡萄', '甘蔗']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)
