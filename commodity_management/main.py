from orm_table_commodity import PostgresConnection
from abc import ABC, abstractmethod
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S %p',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('inventory.log')
    ]
)
logger = logging.getLogger(__name__)


class Item(ABC):
    def __init__(self, inventory_id, name, quantity, price):
        self.inventory_id = inventory_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.insert_item()

    def insert_item(self):
        try:
            PostgresConnection.insert("Inventory", ['inventory_id', 'name', 'quantity', 'price'],
                                          [self.inventory_id, self.name, self.quantity, self.price])
            logger.info(f"Insert (id:{self.inventory_id}) successful")
        except Exception as e:
            logger.error("Error inserting item. e")


    def get_info(self):
        return f"ID: {self.inventory_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"
        # return PostgresConnection.select_all("Inventory")

    @abstractmethod
    def update_stock(self, quantity_change):
        pass


class PhysicalItem(Item):
    def __init__(self, inventory_id, name, quantity, price, weight, dimension):
        super().__init__(inventory_id, name, quantity, price)
        self.weight = weight
        self.dimension = dimension

    def update_stock(self, quantity_change):
        self.quantity += quantity_change
        logger.info(f"Update quantity for (id:{self.inventory_id}) successful")

    def get_info(self):
        return super().get_info() + f", Weight: {self.weight}, Dimension: {self.dimension}"

class DigitalItem(Item):
    def __init__(self, inventory_id, name, quantity, price, file_size, download_link):
        super().__init__(inventory_id, name, quantity, price)
        self.file_size = file_size
        self.download_link = download_link

    def update_stock(self, quantity_change):
        self.quantity += quantity_change
        logger.info(f"Update quantity for (id:{self.inventory_id}) successful")

    def get_info(self):
        return super().get_info() + f", File Size: {self.file_size}, Download Link: {self.download_link}"




if __name__ == "__main__":
    physical_item = PhysicalItem(11, 'Laptop', 50, 99, 2.5, (35, 25, 2))
    digital_item = DigitalItem(12, 'E-book', 100, 10, 5, 'www.example.com/download/ebook')

    print(physical_item.get_info())
    print(digital_item.get_info())

    physical_item.update_stock(10)  # Add 10 units
    digital_item.update_stock(-5)  # Remove 5 units

    print(physical_item.get_info())
    print(digital_item.get_info())
