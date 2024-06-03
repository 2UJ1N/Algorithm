def solution(price, money, count):
    pay = price * (count * (count + 1)) // 2
    return pay - money if pay >= money else 0