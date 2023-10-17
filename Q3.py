import tkinter as tk

class StoreGUI:
    def __init__(self, root):
        self.root = root
        self.cart = []
        self.products = {"Product1": 15.99, "Product2": 29.99, "Product3": 9.99}
        
        self.label = tk.Label(root, text="Welcome to Our Store")
        self.label.pack()
        
        self.product_listbox = tk.Listbox(root)
        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product} - ${self.products[product]}")
        self.product_listbox.pack()
        
        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()
        
        self.cart_label = tk.Label(root, text="Cart:")
        self.cart_label.pack()
        
        self.cart_listbox = tk.Listbox(root)
        self.cart_listbox.pack()
        
        self.calculate_button = tk.Button(root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()
        
        self.total_label = tk.Label(root, text="Total: $0.00")
        self.total_label.pack()

    def add_to_cart(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        self.cart.append(selected_product)
        self.cart_listbox.insert(tk.END, selected_product)

    def calculate_total(self):
        total = sum(self.products[product.split(" - ")[0]] for product in self.cart)
        self.total_label.config(text=f"Total: ${total:.2f}")

# Example usage
root = tk.Tk()
app = StoreGUI(root)
root.mainloop()
