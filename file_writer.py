import csv
import json
def save_products_to_file(products, filename="expensive_products.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for p in products:
            f.write(f"{p['title']} - {p['price']}\n")



def save_products_to_csv(products, filename="expensive_products.csv"):
    if not products:
        print("No products to save.")
        return
    keys = products[0].keys()  # get all keys from first product
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)


def save_products_to_json(products, filename="expensive_products.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

