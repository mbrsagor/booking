"""
total = 0


def booking_average_price(numbers):
    total = sum(numbers)
    total = int(total)
    return total / len(numbers)
"""


def booking_average_price(num):
    price = 0

    for n in num:
        price = price + n

    avg = price / len(num)
    return avg
