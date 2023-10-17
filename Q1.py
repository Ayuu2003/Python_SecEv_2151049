class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        self.inventory[item_name] = {"quantity": quantity, "price": price}

    def update_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]["quantity"] = quantity
            self.inventory[item_name]["price"] = price

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]

    def generate_report(self):
        for item, details in self.inventory.items():
            print(f"Item: {item}, Quantity: {details['quantity']}, Price: {details['price']}")

# Example usage
inventory = Inventory()
inventory.add_item("Product1", 10, 15.99)
inventory.add_item("Product2", 20, 29.99)
inventory.update_item("Product1", 5, 12.99)
inventory.remove_item("Product2")
inventory.generate_report()
