# 世界人口数量前10位国家的电话区号
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

d1 = dict(DIAL_CODES)  # 创建 d1 的时候，数据元组的顺序是按照国家的人口排序来决定的。
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))  # 创建 d2 的时候，数据元组的顺序是按照国家的电话区号来决定的。
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))  # 创建 d3 的时候，数据元组的顺序是按照国家名字的英文拼写来决定的。
print('d3:', d3.keys())
# assert ——— 断言，条件不成立时抛出异常
assert d1 == d2 and d2 == d3  # 这些字典是相等的，因为它们所包含的数据是一样的。
