class Product:
    _total_products = 0 

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product._total_products += 1  

    def display_info(self):
        return f"Product: {self.name}, Price: {self.price}, Total Products: {Product._total_products}"
    @classmethod
    def get_total_products(cls):
        return cls._total_products


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period 

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Warranty: {self.warranty_period} months"


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size  

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Size: {self.size}"


# Приклад використання
if __name__ == "__main__":
   
    laptop = ElectronicProduct("Laptop", 1500, 24)
    tshirt = ClothingProduct("T-Shirt", 25, "L")
    phone = ElectronicProduct("Smartphone", 800, 12)

    print(laptop.display_info())
    print(tshirt.display_info())
    print(phone.display_info())

    print(f"\nTotal products created: {Product.get_total_products()}")
