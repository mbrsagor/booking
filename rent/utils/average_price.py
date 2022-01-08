def booking_average_price(num):
    price = 0

    for n in num:
        price = price + n

    avg = price / len(num)
    return avg
