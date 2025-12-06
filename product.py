# File: product.py

class Product:
    """Represents a product in the inventory with its key attributes."""

    def __init__(self, sku, name, quantity, price, category):
        self.sku = sku          
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def __str__(self):
        return (f"| SKU: {self.sku} | Name: {self.name:<20} | "
                f"Qty: {self.quantity:^5} | Price: ${self.price:>8.2f} |")

    # NEW: Needed for BST comparisons (compare by price)
    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.sku == other.sku
