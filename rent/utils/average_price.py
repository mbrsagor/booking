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

    try:
        avg = price / len(num)
        return avg
    except Exception as ex:
        print(str(ex))
        return str(ex)

# https://www.youtube.com/watch?v=xyUIhluXF_Y
