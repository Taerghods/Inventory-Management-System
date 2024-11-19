# commodity management system

## [Description:](https://github.com/markdown-it/markdown-it-sub)
### design an inventory  commodity management system that can perform various operations such as adding new items, updating stock, and generating reports.

## [The text of the queries:](https://github.com/markdown-it/markdown-it-sub)
### The system should include the following features:
1.  Create a base class named Item with the following attributes: id, name, quantity, and price.
2.  Create two subclasses that inherit from Item:
   - a. PhysicalItem: for physical items that include additional attributes like weight and dimensions.
   - b. DigitalItem: for digital items that include additional attributes like file_size and download_link.

3. Each subclass should implement methods to:
   - a. Update stock (update_stock).
   - b. Get item information (get_info).

4. Use Polymorphism to unify the stock update process for all types of items.
5. Implement a logging system to track changes in stock and log relevant details of each update.
6. Implement a PostgreSQL database with a table named inventory that includes the columns: id, name, quantity, price, type, and additional attributes specific to each item type.
7. Write several queries to:
   - a. Insert new items into the database.
   - b. Update the stock quantity of an item.
   - c. Retrieve all items in the inventory.
   - d. Find items with stock quantities less than a specified threshold (e.g., less than 10).
   - e. Get the total value of all items in stock by multiplying price and quantity for each item and summing the results.
   - f. Find items by their type (e.g., list all PhysicalItems or DigitalItems).
   - g. Get the average price of all items in the inventory.
   - h. Delete an item from the inventory by its id.
   - i. Update the price of an item based on a given id and new price.
   - j. Retrieve items that have been in stock for the longest time (this would require an additional field for date added or last modified).
