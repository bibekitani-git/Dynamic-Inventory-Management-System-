from inventory import Inventory
from product import Product

def run_phase_3_demo():
    print("\n## Phase 3: Hash Table + BST Demonstration ##\n")

    inventory = Inventory()

    p1 = Product("A100", "Laptop", 10, 999.99, "Electronics")
    p2 = Product("B200", "Keyboard", 20, 49.99, "Accessories")
    p3 = Product("C300", "Monitor", 5, 199.99, "Electronics")

    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)

    print("--- BST Range Query: $50 - $300 ---")
    results = inventory.get_products_in_price_range(50, 300)
    for r in results:
        print(r)

if __name__ == "__main__":
    run_phase_3_demo()
