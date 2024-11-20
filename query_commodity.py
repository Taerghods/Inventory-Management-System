from orm_table_commodity import PostgresConnection

table_inventory = PostgresConnection.create_table(
    "Inventory",
    '''inventory_id SERIAL PRIMARY KEY,  
              name VARCHAR(255) NOT NULL,  
              quantity INT NOT NULL,
              price INT NOT NULL,
              type VARCHAR(50) NOT NULL, 
              weight FLOAT,
              dimensions VARCHAR(255),
              file_size FLOAT,
              download_link VARCHAR(255),
              date_added TIMESTAMP DEFAULT now() ''')

'''q1: Insert new items into the database.'''
insert_inventory = PostgresConnection.insert("Inventory",
                                             ['name', 'quantity', 'price', 'type', 'weight', 'dimensions', 'file_size', 'download_link'],
                                             [('Laptop', 10, 50000, 'PhysicalItem', 2.5, '30x20x2', None, None),
                                                  ('Smartphone', 15, 40000, 'PhysicalItem', 0.3, '15x7x0.8', None, None),
                                                  ('Headphones', 25, 7500, 'PhysicalItem', 0.2, '15x15x5', None, None),
                                                  ('Smartwatch', 30, 12500, 'PhysicalItem', 0.5, '4x4x1', None, None),
                                                  ('Tablet', 20, 25000, 'PhysicalItem', 0.8, '25x15x1', None, None),
                                                  ('Software License', 25, 199.99, 'DigitalItem', 200.5, None, None, None),
                                                  ('E-book', 100, 5, 'DigitalItem', None, None, None, None),
                                                  ('Online Course', 200, 1500, 'DigitalItem', None, None, None, 'http://example.com/course'),
                                                  ('Music Album', 150, 800, 'DigitalItem', None, None, None, 'http://example.com/music'),
                                                  ('Video Game', 75, 3000, 'DigitalItem', None, None, None, 'http://example.com/game')])

print('''q2: Update the stock quantity of an item.''')
q2 = PostgresConnection.update("Inventory", "inventory_id", 1, price=50000)

print('''q3: Retrieve all items in the inventory.''')
q3 = PostgresConnection.select_all("Inventory")

print('''q4: Find items with stock quantities less than 20.''')
q4 = PostgresConnection.select("SELECT * FROM Inventory WHERE quantity < 20")

print('''q5: Get the total value of all items in stock by multiplying price and quantity then summing the results''')
q5 = PostgresConnection.select("SELECT sum(quantity * price) FROM Inventory")

print('''q6: Find items by their type''')
q6 = PostgresConnection.select("SELECT * FROM Inventory WHERE type='PhysicalItem'")

print('''q7: Get the average price of all items in the inventory.''')
q7 = PostgresConnection.select("SELECT avg(price) FROM Inventory")

print('''q8: Delete an item from the inventory by its id.''')
# q8 = PostgresConnection.delete("Inventory", "inventory_id",10)

print('''q9: Update the price of an item based on a given id and new price.''')
q9 = PostgresConnection.update("Inventory", "inventory_id", 2, price=45000)

print('''q10: Retrieve items that have been in stock for the longest time''')
q10 = PostgresConnection.select("SELECT name, date_added FROM Inventory order by date_added asc limit 10")
