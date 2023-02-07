"""Мое решение на задачу"""

def sum_of_pay(s: str) -> int:  # '2 2 2 2 2 2 2 3 3 3 3 3'
    all_product = list(map(int, s.split()))
    price_of_1 = set(all_product)
    dict_of_count_goods = {product: all_product.count(product) for product in price_of_1}  # {2: 7, 3: 5}
    d = dict_of_count_goods
    total_cost = [divmod(d.get(product), 3) + (product,) for product in price_of_1]  # [(2, 1, 2), (1, 2, 3)]
    return sum((discount * (price * 2) + non_discount * price for discount, non_discount, price in total_cost))


s1 = '2 2 2 2 2 2 2 3 3 3 3 3'
s2 = '2 3 2 3 2 2 3 2 3 2 2 3'
s3 = '10000'
s4 = '1 2 3 1 2 3 1 2 3'
s5 = '10000 10000 10000 10000 10000 10000'
s6 = '300 100 200 300 200 300'

if __name__ == '__main__':
    assert sum_of_pay(s1) == 22
    assert sum_of_pay(s2) == 22
    assert sum_of_pay(s3) == 10_000
    assert sum_of_pay(s4) == 12
    assert sum_of_pay(s5) == 40_000
    assert sum_of_pay(s6) == 1_100
    print(sum_of_pay(s1))
