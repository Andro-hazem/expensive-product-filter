def filter_expensive_products(products, price_limit):
    return [p for p in products if p["price"] > price_limit]
