from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.username == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product_name)

    def __repr__(self):
        result = []
        for info in self.products:
            result.append(f'{info}: {info.quantity}')

        return '\n'.join(result)
