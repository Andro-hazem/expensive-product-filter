from api_client import fetch_products
from analyzer import filter_expensive_products
from file_writer import save_products_to_csv, save_products_to_json,save_products_to_file
import logging
import argparse

parser = argparse.ArgumentParser(description="Filter expensive products from API")
parser.add_argument("--price",default=500,type=float,help="Price limit to filter products")
parser.add_argument("--url",default="https://dummyjson.com/products?limit=0",help="API URL")
args = parser.parse_args()

print("Price limit:", args.price)
print("URL:", args.url)

URL = args.url
PRICE_LIMIT = args.price

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(),logging.FileHandler("automation_log.txt")]
)

def main():
    products = fetch_products(URL)
    expensive = filter_expensive_products(products, PRICE_LIMIT)

    logging.info(f"Total products: {len(products)}")
    logging.info(f"Expensive products (> {PRICE_LIMIT}): {len(expensive)}")

    # save as CSV
    save_products_to_csv(expensive)
    logging.info("Results saved to expensive_products.csv")

    # save as JSON
    save_products_to_json(expensive)
    logging.info("Results saved to expensive_products.json")

if __name__ == "__main__":
    main()
