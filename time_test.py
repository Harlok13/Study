import datetime
import time




def test_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

# @test_time
# def sum_of_pay(s: str) -> int:  # '2 2 2 2 2 2 2 3 3 3 3 3'
#     all_product = list(map(int, s.split()))
#     price_of_1 = set(all_product)
#     dict_of_count_goods = {product: all_product.count(product) for product in price_of_1}  # {2: 7, 3: 5}
#     d = dict_of_count_goods
#     total_cost = [divmod(d.get(product), 3) + (product,) for product in price_of_1]  # [(2, 1, 2), (1, 2, 3)]
#     res_sum = 0
#     for discount, non_discount, price in total_cost:
#         res_sum += discount * (price * 2) + non_discount * price
#     return res_sum

@test_time
def sum_of_pay(s: str) -> int:  # '2 2 2 2 2 2 2 3 3 3 3 3'
    all_product = list(map(int, s.split()))
    price_of_1 = set(all_product)
    dict_of_count_goods = {product: all_product.count(product) for product in price_of_1}  # {2: 7, 3: 5}
    d = dict_of_count_goods
    total_cost = [divmod(d.get(product), 3) + (product,) for product in price_of_1]  # [(2, 1, 2), (1, 2, 3)]
    return sum((discount * (price * 2) + non_discount * price for discount, non_discount, price in total_cost))


if __name__ == '__main__':
    sum_of_pay('2 3 2 3 2 2 3 2 3 2 2 3')
