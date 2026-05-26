from abc import ABC , abstractmethod

class OutOfStockError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class MenuItem(ABC):
    def __init__(self,name,price,quantity):

        if price <=0:
            raise ValueError("price must be positive")
        
        if quantity<0:
            raise ValueError("Quantity can not be negative")
        
        self.name=name
        self.price=price
        self.quantity=quantity


    def __str__(self):
        return(f"Name: {self.name}|"
              f"Price: {self.price}|"
              f"Quantity: {self.quantity}")

    @abstractmethod
    def prepare(self):
        pass


class VegItem(MenuItem):
    def __init__(self,name,price,quantity,calories):
        super().__init__(name,price,quantity)
        self.calories=calories
    def prepare(self):
        print("Cooking veg food....")


class NonVegItem(MenuItem):
    def __init__(self,name,price,quantity,protein):
        super().__init__(name,price,quantity)
        self.protein=protein
    def prepare(self):
        print("Heating no-veg food.....")


class Beverage(MenuItem):
    def __init__(self,name,price,quantity,volume_ml):
        super().__init__(name,price,quantity)
        self.volume_ml=volume_ml

    def prepare(self):
        print("Pouring the beverage.....")

class Customer:
    def __init__(self,name,wallet_balance):
        if wallet_balance <0:
            raise ValueError("Balance can not be negative")
        
        self.name=name
        self.wallet_balance=wallet_balance
        self.cart=[]

    def add_to_cart(self,item):
        if item in self.cart:
            raise ValueError("Item already in cart")
        self.cart.append(item)

        print(f"{item.name} added to cart")

    def view_cart(self):
        if len(self.cart)==0:
            print("The cart is empty")

            return
        
        for item in self.cart:
            print(item)

    def __str__(self):
        return (f"User : {self.name} |"
                f"Balance : {self.wallet_balance} |")
    
class Restaurant:
    def __init__(self):
        self.menu_items=[]
        self.customers=[]

    def add_item(self,new_item):
        self.menu_items.append(new_item)
    
    def add_customer(self,new_customer):
        self.customers.append(new_customer)

    def show_menu(self):
        for item in self.menu_items:
            print(f"{item.name}||Rs.{item.price}")

    def place_order(self,customer):
                if len(customer.cart)==0:
                    raise ValueError("Cart is empty")
                
                total=0
                for item in customer.cart:
                    if item.quantity==0:
                        raise OutOfStockError(f"{item.name} is out of stock")
                    total+=item.price

                if customer.wallet_balance<total:
                    raise InsufficientBalanceError("The balance is insufficient")
                print("The order was successful!!!")
                customer.wallet_balance-=total
                item.quantity-=1
                customer.cart.clear()


restaurant=Restaurant()

v1 = VegItem(
    "Paneer Pizza",
    250,
    5,
    700
)

n1 = NonVegItem(
    "Chicken Burger",
    180,
    3,
    35
)

b1 = Beverage(
    "Coke",
    50,
    10,
    500
)

restaurant.add_item(v1)
restaurant.add_item(n1)
restaurant.add_item(b1)

c1=Customer("Steni",1000)

restaurant.add_customer(c1)

restaurant.show_menu()


try:
    c1.add_to_cart(v1)
    c1.add_to_cart(n1)
    c1.add_to_cart(b1)

except ValueError as e:
    print(f"Error: {e}")

c1.view_cart()

try:
    restaurant.place_order(c1)

except (OutOfStockError,InsufficientBalanceError,ValueError) as e:
    print(f"Error: {e}")

restaurant.show_menu()

