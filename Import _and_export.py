import csv
import os

PRODUCTS_FILE = 'products.csv'
BILL_FILE = 'bill.csv'

# Create files with headers if they don't exist
if not os.path.exists(PRODUCTS_FILE):
    with open(PRODUCTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Price', 'Stock'])

if not os.path.exists(BILL_FILE):
    with open(BILL_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Product', 'Price', 'Quantity', 'Total'])

def check():
    person = input("Who are you (owner/dealer/customer)? ").lower()
    if person == "owner":
        return Owner()
    elif person == "dealer":
        return Dealer()
    elif person == "customer":
        return Customer()
    else:
        print("Invalid role.")
        return None

class ProductManager:
    @staticmethod
    def read_all():
        if not os.path.exists(PRODUCTS_FILE):
            return []
        with open(PRODUCTS_FILE, newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            return [[row[0], float(row[1]), int(row[2])] for row in reader]

    @staticmethod
    def write_all(products):
        with open(PRODUCTS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Price', 'Stock'])  # Write header
            writer.writerows(products)

class Owner:
    def menu(self):
        while True:
            print("\nOwner Menu:\n1. Create\n2. Update\n3. Delete\n4. Read\n5. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.create_product()
            elif choice == '2':
                self.update_product()
            elif choice == '3':
                self.delete_product()
            elif choice == '4':
                self.read_products()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")

    def create_product(self):
        name = input("Product name: ")
        try:
            price = float(input("Price: "))
            stock = int(input("Stock: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return
        products = ProductManager.read_all()
        products.append([name, price, stock])
        ProductManager.write_all(products)
        print("Product added.")

    def update_product(self):
        products = ProductManager.read_all()
        name = input("Enter product name to update: ")
        found = False
        for product in products:
            if product[0].lower() == name.lower():
                new_name = input("Enter new product name (or press Enter to keep the same): ")
                if new_name.strip() != "":
                    product[0] = new_name
                try:
                    product[1] = float(input("New price: "))
                    product[2] = int(input("New stock: "))
                except ValueError:
                    print("Invalid input.")
                    return
                found = True
                break
        if found:
            ProductManager.write_all(products)
            print("Product updated.")
        else:
            print("Product not found.")

    def delete_product(self):
        products = ProductManager.read_all()
        name = input("Enter product name to delete: ")
        new_products = [p for p in products if p[0].lower() != name.lower()]
        if len(new_products) == len(products):
            print("Product not found.")
        else:
            ProductManager.write_all(new_products)
            print("Product deleted.")

    def read_products(self):
        products = ProductManager.read_all()
        if not products:
            print("No products found.")
            return
        print("\nAvailable Products:")
        for p in products:
            print(f"Name: {p[0]}, Price: Rs.{p[1]}, Stock: {p[2]}")

class Dealer:
    def input_data(self):
        name = input("Product name to add/update: ")
        try:
            stock = int(input("Stock to add: "))
        except ValueError:
            print("Invalid stock input.")
            return

        products = ProductManager.read_all()
        found = False

        for product in products:
            if product[0].lower() == name.lower():
                product[2] += stock
                found = True
                break

        if not found:
            try:
                price = float(input("New product price: "))
            except ValueError:
                print("Invalid price.")
                return
            products.append([name, price, stock])
            print("New product added.")
        else:
            print("Stock updated for existing product.")

        ProductManager.write_all(products)

class Customer:
    def view_and_buy(self):
        products = ProductManager.read_all()
        if not products:
            print("No products available.")
            return
        print("\nAvailable Products:")
        for i, p in enumerate(products):
            print(f"{i+1}. {p[0]} - Rs.{p[1]} (Stock: {p[2]})")
        try:
            choice = int(input("Select product number to buy: ")) - 1
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid input.")
            return
        if 0 <= choice < len(products):
            product = products[choice]
            if quantity <= product[2]:
                total = product[1] * quantity
                product[2] -= quantity
                ProductManager.write_all(products)
                self._generate_bill(product[0], product[1], quantity, total)
                print(f"Purchased {quantity} x {product[0]} for Rs.{total}")
            else:
                print("Not enough stock.")
        else:
            print("Invalid product number.")

    def _generate_bill(self, name, price, qty, total):
        with open(BILL_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, price, qty, total])

# Main interaction
user = check()
if isinstance(user, Owner):
    user.menu()
elif isinstance(user, Dealer):
    user.input_data()
elif isinstance(user, Customer):
    user.view_and_buy()
