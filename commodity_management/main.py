
class Item:
     def __init__(self, id, name, quantity, price):
         self.id = id
         self.name = name
         self.quantity = quantity
         self.price = price

class PhysicalItem(Item):
    def __init__(self, id, name, quantity, price, weight, dimension):
        super().__init__(id, name, quantity, price)
        self.weight = weight
        self.dimension = dimension

    def update_stock(self):
        pass

        # for i in

    def get_info(self):
        pass



class DigitalItem(Item):
    def __init__(self, id, name, quantity, price, file_size, download_link):
        super().__init__(id, name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def update_stock(self):
        pass

    def get_info(self):
        pass
