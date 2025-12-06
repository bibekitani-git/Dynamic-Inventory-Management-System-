# File: bst.py

class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree keyed by product.price for O(log N) range queries."""

    def __init__(self):
        self.root = None

    def insert(self, product):
        """Insert product into BST."""
        self.root = self._insert_recursive(self.root, product)

    def _insert_recursive(self, node, product):
        if not node:
            return BSTNode(product)
        if product.price < node.product.price:
            node.left = self._insert_recursive(node.left, product)
        else:
            node.right = self._insert_recursive(node.right, product)
        return node

    def delete(self, product):
        """Delete product by price."""
        self.root = self._delete_recursive(self.root, product)

    def _delete_recursive(self, node, product):
        if not node:
            return None

        if product.price < node.product.price:
            node.left = self._delete_recursive(node.left, product)
        elif product.price > node.product.price:
            node.right = self._delete_recursive(node.right, product)
        else:
            # Node found
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Replace with successor
            successor = self._get_min(node.right)
            node.product = successor.product
            node.right = self._delete_recursive(node.right, successor.product)

        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def get_range(self, low_price, high_price):
        """Return all products in price range."""
        result = []
        self._range_search(self.root, low_price, high_price, result)
        return result

    def _range_search(self, node, low, high, result):
        if not node:
            return
        if low <= node.product.price <= high:
            result.append(node.product)
        if node.product.price >= low:
            self._range_search(node.left, low, high, result)
        if node.product.price <= high:
            self._range_search(node.right, low, high, result)
