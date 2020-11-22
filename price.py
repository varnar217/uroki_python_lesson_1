def format_price(price):
    try:
        err=int(price)
        return f"Цена: {err} руб."
    except ValueError:
        return u'dont type int'

a=(format_price(56.24))
print(a)
