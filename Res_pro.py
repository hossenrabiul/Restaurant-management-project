from abc import ABC
class User(ABC):
    def __init__(self, name, phone, email) -> None:
        self.name = name
        self.phone = phone
        self.email = email

class Admin(User):
    def __init__(self, name, phone, email) -> None:
        super().__init__(name, phone, email)
        

    def add_employee(self, restourant, employee):
        restourant.add_employee(employee)
    
    def show_employee(self, restaurant):
        restaurant.show_employee()
    
    def add_new_item(self, restaurnat, item):
        restaurnat.menu.add_item(item)

    def del_item(self, restaurant, item):
        restaurant.menu.del_item(item)

    def show_item(self, restaurant):
        restaurant.menu.show_item()

class Restaurant:
    def __init__(self, name) -> None:
        self.name = name
        self.employees = []
        self.menu = Menu()
        
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def show_employee(self):
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email)

class Menu:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def del_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
        else:
            print("Not Found")

    def show_item(self):
        for item in self.items:
            print(item.name, item.price, item.quantity)

        
class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item_to_cart(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
            

    def del_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print('item not found')


    def total_price(self):

        return sum(item.price * quantity for item, quantity in self.items.items())


class Food:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer(User):
    def __init__(self, name, phone, email) -> None:
        super().__init__(name, phone, email)
        self.cart = Order()

    def show_item(self, restaurant):
        restaurant.menu.show_item()

    def add_to_cart(self, restaurant, item, quantity):
        item = restaurant.menu.find_item(item)
        if item:
            if item.quantity >= quantity:
                item.quantity -= quantity
                self.cart.add_item_to_cart(item, quantity)
            else:
                print("Quantity Is Not Available !")
        else:
            print("Item Is Not Available !")
    def view_cart(self):
        if self.cart.items is not None:
            for item, quantity in self.cart.items.items():
                print(item.name, item.price, quantity)
        else:
            print("Your cart is empty !")

    def del_item_from_cart(self, item):
        self.cart.del_item(item)


    def paybill(self, amount):
        if self.cart.total_price <= amount:
            print("Bill Paid successfully !")
        else:
            print("you can't buy these product with this amount of money,Provide more money !")

class Employee:
    def __init__(self, name, phone, email, age):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

admin = Admin('seh', 344, 'she@gmail.com')
mamar_res = Restaurant('mamrt_res')
customer = Customer("ami", 234, 'ami@gmail.com')
def Admin_class():
    print("Enter YOur Choice ")
    while True:
        print("1. Add Employee : ")
        print("2. show Employee : ")
        print("3. add item : ")
        print("4. delete item : ")
        print("5. show item : ")
        print("    Exit : ")

        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            emp = Employee('rakib', 345, 'rakib@gamil.com', 25)
            admin.add_employee(mamar_res, emp)
        elif ch == 2:
            admin.show_employee(mamar_res)
        elif ch == 3:
            name = input("Enter item name : ")
            price = int(input("Enter item price : "))
            quan = int(input("Enter item Quantity : "))
            item = Food(name, price, quan)
            mamar_res.menu.add_item(item)
        elif ch == 4:
            name = input("Enter item name")
            mamar_res.menu.del_item(name)
        elif ch == 5:
            mamar_res.menu.show_item()
        else:
            break

def Customer_class():
    print("Choice : ")
    while True:
        print("1. show item : ")
        print("2. add to cart : ")
        print("3. view cart : ")
        print("4. del item from cart : ")
        print("    Exit : ")
    
        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            mamar_res.menu.show_item()
        elif ch == 2:
            name = input("Enter item name : ")
            quan = int(input("Enter item quantity : "))
            customer.add_to_cart(mamar_res, name, quan)

        elif ch == 3:
            customer.view_cart()

        elif ch == 4:
            name = input("Enter item name : ")
            # quan = int(input("Enter item quantity : "))
            customer.del_item_from_cart(name)
        else:
            break

while True:
    print("Here is your choice : ")
    print("1. Admin")
    print("2. Customer")
    print("   break   ")
    ch = int(input("Enter Your Choice : "))
    
    if ch == 1:
        Admin_class()
    elif ch == 2:
        Customer_class()
    else:
        break
        
        