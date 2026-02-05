def filter_expensive_products(products, price_limit):
    filtered = [p for p in products if p["price"] > price_limit]
    # Sort by price ascending
    filtered.sort(key=lambda x: x["price"])
    return filtered

