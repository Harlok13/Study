"""Чек об оплате в магазине"""
import json
from datetime import datetime
from textwrap import fill

path = "D:\\Notepad ++\\py_files\\checkout\\external_p\\"
payment_with_card = 1
loyalty_card_apply = 1

with open(path + "shop_info.json", encoding="utf-8") as shop_info:
    shop_details = json.load(shop_info)

with open(path + "goods.json", encoding="utf-8") as goods_in:
    goods = json.load(goods_in)


def get_f_vat(vat):
    return f"НДС {vat}%"


def get_actual_price(p_before_d, discount):
    return p_before_d - discount


def get_f_amount(amount):
    if isinstance(amount, int):
        return f"{amount}шт"
    if isinstance(amount, float):
        return f"{amount:.3f}кг"


def get_total_line(price, amount):
    return float(price * amount)


def do_payment_cash(total_in):
    accepted = 0
    while accepted < total_in:
        try:
            accepted = float(input("How much accepted? -> "))
        except ValueError:
            print("incorrect input")
    change = accepted - total_in

    return accepted, change


def do_payment_card(payable_amount):
    with open(path + "transaction_info.json", encoding="utf-8") as transaction_info:
        card_payment_details = json.load(transaction_info)
    card_payment_details["paid_amount"] = f"{payable_amount:.2f}"
    card_payment_details["transaction_dt"] = datetime.now()

    return card_payment_details


def calculate_stickers(total):
    new_stickers_amount = int(total // 200)
    if total > 400:
        return new_stickers_amount * 2
    return new_stickers_amount


def calculate_loyalty_points(total):
    return int(total * 0.05)


print(f"{'КАССОВЫЙ ЧЕК':^56}")
print(f"{'Цена до скидки':^16}{'Скидка':^10}{'Цена':>10}{'Кол-во':^10}{'Итого':>10}")

total = {"discount": 0, "total": 0, "vat": {10: 0, 20: 0}}

for i in goods:
    print(i[0])
    vat = get_f_vat(i[1])
    p_before_d = i[2]
    discount = f"{i[3]:10.2f}" if i[3] else f"{'':10}"
    price = get_actual_price(p_before_d, i[3])
    amount = get_f_amount(i[4])
    total_line = get_total_line(price, i[4])

    print(f"{vat:<8}{p_before_d:>8.2f}{discount}{price:10.2f}{amount:>10}{total_line:10.2f}")

    total["discount"] += i[3] * i[4]
    total["total"] += total_line
    total["vat"][i[1]] += total_line * i[1] / (100 + i[1])

total_discount = total.get("discount")
subtotal = total.get("total") + total_discount
vat_10, vat_20 = total.get("vat").get(10), total.get("vat").get(20)

if payment_with_card:
    card_payment_details = do_payment_card(total.get("total"))
    #    if not card_payment_details.get("success"):
    #        print("Transaction failed")
    rounding = cash = accepted = change = 0
    non_cash = total_in = total.get("total")
else:
    non_cash = 0
    rounding = round((subtotal - total_discount) - int(subtotal - total_discount), 2)
    total_in = subtotal - total_discount - rounding
    accepted, change = do_payment_cash(total_in)
    cash = accepted - change

dt_now = datetime.now().strftime("%d.%m.%y %H:%M")

print("-" * 56)
print(f"""{'СКИДКА:':<14}{total_discount:>13.2f}  {'ПОДЫТОГ:':<14}{subtotal:>13.2f}
{'ОКРУГЛЕНИЕ:':<14}{rounding:>13.2f}  {'ИТОГ:':<14}{total_in:>13.2f}
{'НАЛИЧНЫМИ:':<14}{cash:>13.2f}  {'ПРИНЯТО:':<14}{accepted:>13.2f}
{'БЕЗНАЛИЧНЫМИ:':<14}{non_cash:>13.2f}  {'СДАЧА:':<14}{change:>13.2f}""")
print("-" * 56)
print(f"{'Сумма НДС 20%:':<14}{vat_20:>13.2f}  {'Сумма НДС 10%:':<14}{vat_10:>13.2f}")
print("-" * 56)

print(shop_details.get("shop_name"))
print(
    f"{'ИНН:' + shop_details.get('inn'):16}{'СНО:' + shop_details.get('sno'):>10}{'Код:' + shop_details.get('code'):>30}")
print(fill(shop_details.get('address'), 56))
print(f"Кассир:{shop_details.get('cashier_name')}, {shop_details.get('cashier_pos')}")
print(f"{dt_now:>56}")
print(f"{'Касса: ' + shop_details.get('cash_number'):16}{'кассир':>36}")
print(f"{'ПРИХОД':>56}")
print(f"Место расчетов:{shop_details.get('place')}")
print("-" * 56)

print(f"""Сайт ФНС:
www.nalog.gov.ru
РН ККТ:{shop_details.get('rn_kkt')}
ФП:{shop_details.get('fp')}
ФН:{shop_details.get('fn')}
ЗН ККТ:{shop_details.get('zn_kkt')}
ФД:{shop_details.get('fd')}
KM?""")
print()
print()
print("*На артикул не предоставляется скидка")

if payment_with_card:
    print("." * 56)
    print(f"{card_payment_details.get('transaction_dt').strftime('%d.%m.%y')}       "
          f"{card_payment_details.get('transaction_dt').strftime('%H:%M')}      "
          f"{'T:' + card_payment_details.get('t')}      "
          f"{'M:' + card_payment_details.get('m')}"
          )
    print(
        f"{'KA:' + card_payment_details.get('ka'):<15}{'RRN:' + card_payment_details.get('rrn'):^26}{'ЧЕК ' + card_payment_details.get('check'):>15}")
    print(
        f"{card_payment_details.get('sys'):>23}{card_payment_details.get('card_num'):^13}{'AID:' + card_payment_details.get('aid'):>20}")
    print(
        f"{card_payment_details.get('acquier'):^16}{'Оплата   ' + 'ОДОБРЕНО' if card_payment_details.get('success') else 'ОТКАЗАНО':^40}")
    print("Клиент:")
    print(
        f"{'Сумма(Руб):' + card_payment_details.get('paid_amount'):20}{'Комиссия за операцию ' + card_payment_details.get('fee') + ' Руб':>36}")
    if card_payment_details.get('pin_entered'):
        print(f"{'Введен ПИН-код':^56}")
        print(f"{card_payment_details.get('id'):^56}")

if loyalty_card_apply:
    with open(path + "loyalty_extra_info.txt", encoding="utf-8") as l_extra_info:
        loyalty_txt = l_extra_info.readlines()
    print("." * 56)
    for line in loyalty_txt:
        print(f"{line.strip():^56}")
    print("." * 56)

    with open(path + "loyalty_card_data.json", encoding="utf-8") as loyalty_in:
        loyalty_card_details = json.load(loyalty_in)
    print(f"Баланс наклеек: {loyalty_card_details.get('stickers_amount')}")
    print(f"Начислено наклеек: {calculate_stickers(total_in)}")
    print(f"Карта лояльности: {'**** ' * 3 + loyalty_card_details.get('card_num')[-4:]}")
    print(f"Общий баланс: {loyalty_card_details.get('loyalty_points_amount')}")
    print(f"Начислено баллов: {calculate_loyalty_points(total_in)}")
    print("Баллы станут доступны в течение суток")
    print(f"Списано баллов: {loyalty_card_details.get('loyalty_points_used')}")
