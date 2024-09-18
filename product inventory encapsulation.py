# Product Inventory Encapsulation

class Product:
    def __init__(self, name):
        self.__name = name  # Encapsulated the name
        self.__price = 0
        self.__quantity = 0
        
    def update_quantity(self):
        try:
            self.__quantity = int(input("Enter the quantity: "))
        except ValueError:
            return "Invalid quantity. Please enter an integer value."
        return f"Quantity updated to: {self.__quantity}"
    
    def update_price(self):
        try:
            self.__price = float(input("Enter the price: "))
        except ValueError:
            return "Invalid price. Please enter a valid number."
        return f"Total price for all units: {self.__quantity * self.__price:.2f}"
    
    def get_product_info(self):
        return f"Product name: {self.__name}, Price per unit: {self.__price:.2f}, Quantity: {self.__quantity}"
    

# Create a Product object and test the methods
product1 = Product(input("Enter the name of product: "))

# Update the quantity
print(product1.update_quantity())

# Update the price
print(product1.update_price())

# Get the product info
print(product1.get_product_info())
