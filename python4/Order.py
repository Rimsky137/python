    class Order:
        def __init__(self, Customer):
            self.customer = Customer
            self.list_products = {}

        def add_product(self, product):
            self.list_products[product] = product.price
            return self.list_products

        def summa(self):
            sum = 0
            for i in self.list_products.keys():
                sum = sum + self.list_products[i]
            return sum

        def __str__(self):
            return "Клиент {}, Сумма {}".format(self.customer, self.summa())

     def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.products_list):
                return self.products_list[index]
            else:
                raise IndexError()

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.list_products) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            temp_product_list = []
            if start < 0 and stop >= len(self.list_products):
                raise IndexError()
            for i in range(start, stop, step):
                temp_list_products.append(self.list_products[i])
            return temp_list_products

        raise TypeError

    def __len__(self):
        return len(list_products)

    def __iter__(self):
        return Productiterator.ProductIterator(self.list_products)
