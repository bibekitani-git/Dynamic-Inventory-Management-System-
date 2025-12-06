# File: inventory.py
from product import Product

class Inventory:
    """Manages the inventory using a Hash Table (Python Dictionary) 
    for O(1) average time complexity operations."""
    
    def __init__(self):
        # The core data structure: Key: SKU (str), Value: Product object
        self.products = {} 

    # --- Core O(1) Operations ---

    def add_product(self, product):
        """Inserts a new product into the Hash Table."""
        if not isinstance(product, Product):
            raise TypeError("Input must be a Product object.")
            
        if product.sku in self.products:
            # Handle collision/duplicate SKU
            return False, f"Error: Product with SKU {product.sku} already exists."
        
        self.products[product.sku] = product
        return True, f"Success: Product {product.sku} added."

    def find_product(self, sku):
        """Searches for a product by SKU."""
        # Direct key lookup using .get() for O(1) average time
        return self.products.get(sku, None)

    def update_quantity(self, sku, new_quantity):
        """Updates the quantity of an existing product."""
        product = self.find_product(sku)
        
        if product:
            # Check for non-negative quantity
            if new_quantity >= 0:
                product.quantity = new_quantity
                return True, f"Success: Quantity for {sku} updated to {new_quantity}."
            return False, "Error: Quantity cannot be negative."
            
        return False, f"Error: Product with SKU {sku} not found."

    def delete_product(self, sku):
        """Removes a product from the Hash Table."""
        if sku in self.products:
            del self.products[sku]
            return True, f"Success: Product {sku} deleted."
        return False, f"Error: Product with SKU {sku} not found."

    # --- PoC Utility Function ---
    
    def get_inventory_count(self):
        """Returns the total number of items in the inventory."""
        return len(self.products)