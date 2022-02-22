class ProductIterator:
    def __init__(self, list_products):
        self.products_list = list_products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_products):
            raise StopIteration()
        temp_product = self.list_products[self.index]
        self.index += 1
        return temp_product
