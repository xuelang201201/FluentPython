from fp_03_1_实用函数实现策略模式 import *
from fp_03_2_选择最佳策略简单的方式 import *
from fp_03_3_内省模块的全局命名空间构建promos列表 import *
from fp_03_4_内省单独的promotions模块构建promos列表 import *

joe = Customer('John Doe', 0)  # 与示例fp_01一样的测试固件
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, fidelity_promo))  # 为了把折扣策略应用到 Order 示例上，只需把促销函数作为参数传入。
print(Order(ann, cart, fidelity_promo))
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, bulk_item_promo))  # 这个测试和下一个测试使用不同的促销函数。
long_order = [LineItem(str(item_code), 1, 1.0)
              for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))

# 选择最佳策略：简单的方式
# best_promo 函数计算所有折扣，并返回额度最大的
print("最佳策略：")
print(Order(joe, long_order, best_promo))  # best_promo 为顾客 joe 选择 larger_order_promo。
print(Order(joe, banana_cart, best_promo))  # 订购大量香蕉时，joe 使用 bulk_item_promo 提供的折扣。
print(Order(ann, cart, best_promo))  # 在一个简单的购物车中，best_promo 为忠实顾客 ann 提供 fidelity_promo 优惠的折扣。
