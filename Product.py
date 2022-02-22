Class Product:

    def __init__(self, name, price, description, length, width,):
        self.name = name
        self.price = price
        self.description = description
        self.length = length
        self.width = width
    def __str__(self):
        return "name = {}, price = {}, description = {}, length = {}, width = {}".format(self.name, self.price, self.description, self.length, self.width)
