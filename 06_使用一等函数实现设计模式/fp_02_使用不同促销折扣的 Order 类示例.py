from fp_01_实现Order类支持插入式折扣策略 import *

joe = Customer('John Doe', 0)  # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),  # 有三个商品的购物车。
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))  # fidelityPromo 没给 joe 提供折扣。

print(Order(ann, cart, FidelityPromo()))  # ann 得到了 5% 折扣，因为她的积分超过 1000。

banana_cart = [LineItem('banana', 30, .5),  # banana_cart 中有 30 把香蕉和 10 个苹果。
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, BulkItemPromo()))  # BulkItemPromo 为 joe 购买的香蕉优惠了 1.50 美元。

long_order = [LineItem(str(item_code), 1, 1.0)  # long_order 中有 10 个不同的商品，每个商品的价格为 1.00 美元。
              for item_code in range(10)]

print(Order(joe, long_order, LargeOrderPromo()))  # LargeOrderPromo 为 joe 的整个订单提供了 7% 折扣。

print(Order(joe, cart, LargeOrderPromo()))
