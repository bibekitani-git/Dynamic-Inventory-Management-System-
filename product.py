# File: product.py

class Product:
    """Represents a product in the inventory with its key attributes."""
    
    def __init__(self, sku, name, quantity, price, category):
        # SKU is the unique identifier
        self.sku = sku          
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def __str__(self):
        # Human-readable string representation
        return (f"| SKU: {self.sku} | Name: {self.name:<20} | "
                f"Qty: {self.quantity:^5} | Price: ${self.price:>8.2f} |")