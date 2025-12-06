# File: performance_tests.py
import random
import time
from inventory import Inventory
from product import Product

def generate_products(n):
    products = []
    for i in range(n):
        sku = f"SKU{i:06d}"
        price = random.uniform(1, 2000)
        qty = random.randint(0, 200)
        products.append(Product(sku, f"Item{i}", qty, price, "General"))
    return products

def measure_insert_time(n):
    inventory = Inventory()
    products = generate_products(n)
    start = time.perf_counter()
    for p in products:
        inventory.add_product(p)
    end = time.perf_counter()
    return (end - start) / n

def measure_scan_time(n):
    inventory = Inventory()
    for p in generate_products(n):
        inventory.add_product(p)
    start = time.perf_counter()
    for p in inventory.products.values():
        x = p.price
    end = time.perf_counter()
    return end - start

def measure_bst_range(n):
    inventory = Inventory()
    for p in generate_products(n):
        inventory.add_product(p)
    start = time.perf_counter()
    inventory.get_products_in_price_range(100, 500)
    end = time.perf_counter()
    return end - start

def stress_test():
    n = 100000
    r = 10000
    inventory = Inventory()
    for p in generate_products(n):
        inventory.add_product(p)

    skus = list(inventory.products.keys())

    start = time.perf_counter()
    for i in range(r):
        inventory.find_product(random.choice(skus))
    end = time.perf_counter()

    return end - start, (end - start) / r

def run_all_tests():
    sizes = [100, 1000, 10000, 100000]
    print("N | Insert(ms) | Scan(ms) | BST Range(ms)")
    for n in sizes:
        ins = measure_insert_time(n) * 1000
        scan = measure_scan_time(n) * 1000
        bst = measure_bst_range(n) * 1000
        print(f"{n} | {ins:.5f} | {scan:.5f} | {bst:.5f}")

    total, avg = stress_test()
    print("\n--- Stress Test (100k items, 10k finds) ---")
    print(f"Total Time (s): {total:.5f}")
    print(f"Avg Search Time (us): {avg*1e6:.3f}")

if __name__ == "__main__":
    run_all_tests()
