# File: inventory.py
from product import Product
from bst import BST

class Inventory:
    """Hybrid structure: Hash Table (O1) + BST for price-range queries (O log N)."""

    def __init__(self):
        self.products = {} 
        self.price_tree = BST()   # NEW

    # --- Core Phase 2 O(1) Operations ---

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Input must be a Product object.")
            
        if product.sku in self.products:
            return False, f"Error: Product with SKU {product.sku} already exists."

        self.products[product.sku] = product
        self.price_tree.insert(product)   # NEW
        return True, f"Success: Product {product.sku} added."

    def find_product(self, sku):
        return self.products.get(sku, None)

    def update_quantity(self, sku, new_quantity):
        product = self.find_product(sku)
        
        if product:
            if new_quantity >= 0:
                product.quantity = new_quantity
                return True, f"Success: Quantity for {sku} updated to {new_quantity}."
            return False, "Error: Quantity cannot be negative."
        return False, f"Error: Product with SKU {sku} not found."

    def delete_product(self, sku):
        if sku in self.products:
            product = self.products[sku]
            self.price_tree.delete(product)   # NEW
            del self.products[sku]
            return True, f"Success: Product {sku} deleted."
        return False, f"Error: Product with SKU {sku} not found."

    # NEW: O(logN) price-range search
    def get_products_in_price_range(self, low, high):
        return self.price_tree.get_range(low, high)

    def get_inventory_count(self):
        return len(self.products)
