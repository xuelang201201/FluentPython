"""
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5),
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermelon', 5, 5.0)]
    >>> Order(joe, cart, fidelity)
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, fidelity)
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5),
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, bulk_item)
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(item_code), 1, 1.0)
    ...               for item_code in range(10)]
    >>> Order(joe, long_order, large_order)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, cart, large_order)
    <Order total: 42.00 due: 42.00>
# BEGIN STRATEGY_BEST_TESTS
    >>> Order(joe, long_order, best_promo)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, banana_cart, best_promo)
    <Order total: 30.00 due: 28.50>
    >>> Order(ann, cart, best_promo)
    <Order total: 42.00 due: 39.90>
# END STRATEGY_BEST_TESTS
"""

from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


promos = []  # promos列表起初是空的。


def promotion(promo_func):  # promotion 把 promo_func 添加到 promos 列表中，然后原封不动地将其返回。
    promos.append(promo_func)
    return promo_func


@promotion  # 被 @promotion 装饰的函数都会添加到 promos 列表中。
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):  # best_promos 无需修改，因为它依赖 promos 列表。
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)
