# File: demonstration.py
from inventory import Inventory
from product import Product

def run_poc_demonstration():
    """Runs the proof of concept demonstration script."""
    inventory = Inventory()

    print("## Phase 2: Proof of Concept Demonstration ##\n")

    # --- Test Case 1: Initial Insertion (O(1)) ---
    print("--- 1. Initial Insertion (Testing O(1) Add) ---")
    p1 = Product("LAP1001", "Gaming Laptop", 15, 1200.00, "Electronics")
    p2 = Product("MOU2003", "Wireless Mouse", 50, 25.50, "Accessories")
    
    success, message = inventory.add_product(p1)
    print(f"Adding P1: {message}")
    success, message = inventory.add_product(p2)
    print(f"Adding P2: {message}")
    print(f"Current Inventory Count: {inventory.get_inventory_count()}\n")

    # --- Test Case 2: Successful Search (Testing O(1) Find) ---
    print("--- 2. Successful Search (Testing O(1) Find) ---")
    found_p1 = inventory.find_product("LAP1001")
    if found_p1:
        print(f"Found Product: {found_p1}")
    else:
        print("Error: Product LAP1001 not found.")
    
    # --- Test Case 3: Edge Case (Non-Existent SKU) ---
    print("\n--- 3. Edge Case: Searching for Non-Existent SKU ---")
    not_found = inventory.find_product("TAB5000")
    print(f"Search for TAB5000 Result: {'Found' if not_found else 'Not Found'}")

    # --- Test Case 4: Update Operation (Testing O(1) Update) ---
    print("\n--- 4. Update Operation (Testing O(1) Update) ---")
    success, message = inventory.update_quantity("LAP1001", 10)
    print(f"Update Result: {message}")
    print(f"Updated Product: {inventory.find_product('LAP1001')}")

    # --- Test Case 5: Edge Case (Duplicate Insertion) ---
    print("\n--- 5. Edge Case: Duplicate Insertion ---")
    p_duplicate = Product("LAP1001", "Laptop Duplicate", 1, 1.00, "Electronics")
    success, message = inventory.add_product(p_duplicate)
    print(f"Duplicate Add Result: {message}")

    # --- Test Case 6: Deletion (Testing O(1) Delete) ---
    print("\n--- 6. Deletion Operation (Testing O(1) Delete) ---")
    success, message = inventory.delete_product("MOU2003")
    print(f"Deletion Result: {message}")
    print(f"Current Inventory Count after deletion: {inventory.get_inventory_count()}")
    
if __name__ == "__main__":
    run_poc_demonstration()