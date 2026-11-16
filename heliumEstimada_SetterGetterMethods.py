#ACTIVITY2

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")


rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)



#ACTIVITY3
class BankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = 0.0
        self.set_balance(balance)

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    # Public setter methods
    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def set_balance(self, balance: float):
        if balance < 0:
            print("The balance must not be a negative number.")
        else:
            self.__balance = float(balance)



a1 = BankAccount(12345, 1000)

print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

print("\nUpdate balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

# Utilizing set_account_number to demonstrate all public methods
a1.set_account_number(67890)
print("\nAfter updating account number:")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

