# Order 类和使用函数实现的折扣策略
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


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
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)  # 计算折扣只需调用 self.promotion() 函数。
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 没有抽象类。

def fidelity_promo(order):  # 各个策略都是函数。
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


# 选择最佳策略：简单的方式
# best_promo 迭代一个函数列表，并找出折扣额度最大的
promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # promos 列出以函数实现的各个策略。


def best_promo(order):  # 与其他几个 *_promo 函数一样，best_promo 函数的参数是一个 Order 实例。
    # 使用生成器表达式把 order 传给 promos 列表中的各个函数，返回计算出的最大折扣额度。
    return max(promo(order) for promo in promos)
