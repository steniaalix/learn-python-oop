from abc import ABC, abstractmethod
class InsufficientBalanceError(Exception):
    pass

class Paymentmethod(ABC):
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.balance=balance
    def __str__(self):
        return ( f"Owner: {self.owner_name}|"
                f"Balance: {self.balance}")
    @abstractmethod
    def pay(self,amount):
        pass 
        

    @abstractmethod
    def refund(self,amount):
        pass



class CreditCardPayment(Paymentmethod):
    def __init__(self,owner_name,balance,card_number):
        super().__init__(owner_name,balance)
        self.card_number=card_number

    def pay(self,amount):
        if amount<=0:
            raise ValueError("Amount can not be negative or zero")
        if amount>self.balance:
            raise InsufficientBalanceError("Amount is higher than balance")
        self.balance-=amount
        print(f"Rs.{amount} is withdrawn")
        print(f"Your card number: {self.card_number}")
        print("Thank you for using credit card")
        

    def refund(self,amount):
        if amount<0:
            raise ValueError("Can not refund negative amount")
        self.balance+=amount
        print(f"Rs.{amount} successfully refunded")
        print(f"Current balance is {self.balance}")
        print("Thank you for using credit card!!!")




class UpiPayment(Paymentmethod):
    def __init__(self,owner_name,balance,upi_id):
        super().__init__(owner_name,balance)
        self.upi_id=upi_id
    
    def pay(self,amount):
        if amount<=0:
            raise ValueError("Amount can not be negative or zero")
        if amount>self.balance:
            raise InsufficientBalanceError("Amount is higher than balance")
        self.balance-=amount
        print(f"Rs.{amount} is withdrawn")
        print(f"Your Upi ID: {self.upi_id}")
        print("Thank you for using UPI")
        

    def refund(self,amount):
        if amount<0:
            raise ValueError("Can not refund negative amount")
        self.balance+=amount
        print(f"Rs.{amount} successfully refunded")
        print(f"Current balance is {self.balance}")
        print("Thank you for using UPI!!!")



class WalletPayment(Paymentmethod):
    def __init__(self,owner_name,balance,wallet_name):
        super().__init__(owner_name,balance)
        self.wallet_name=wallet_name

    def pay(self,amount):
        if amount<=0:
            raise ValueError("Amount can not be negative or zero")
        if amount>self.balance:
            raise InsufficientBalanceError("Amount is higher than balance")
        self.balance-=amount
        print(f"Rs.{amount} is withdrawn")
        print(f"Your wallet name: {self.wallet_name}")
        print(f"Thank you for using {self.wallet_name} wallet")
        

    def refund(self,amount):
        if amount<0:
            raise ValueError("Can not refund negative amount")
        self.balance+=amount
        print(f"Rs.{amount} successfully refunded")
        print(f"Current balance is {self.balance}")
        print(f"Thank you for using {self.wallet_name} wallet!!!")

money=[]

ccp=CreditCardPayment("steni",50000,123)
money.append(ccp)



upi=UpiPayment("Steni",1000,"Abc123")

money.append(upi)





wallet=WalletPayment("Steni",50000,"Meow")
money.append(wallet)


for p in money:
    try: 
        p.pay(3000)
        p.refund(1000)
    except InsufficientBalanceError as e:
        print(e)
    except ValueError as e:
        print(e)