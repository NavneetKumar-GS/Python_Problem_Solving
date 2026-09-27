class BankAccount:

    def __init__(self,account_holder,inital_balance=0):

        self.balance = inital_balance
        self.holder = account_holder


    def deposit_amount(self):
        amount = int(input("Enter the amount: "))

        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited!!")
        else:
            print("Amount must be greater than zero.")

    def withdraw_amount(self):
        amount = int(input("Enter the amount: "))

        if amount < self.balance:
            self.balance -= amount
            print(f"₹{amount} deposited!!")
        else:
            print("Insufficeint balance!")

    def check_balance(self):
        print(f"₹{self.balance} left in {self.holder} bank account!!")


account = BankAccount(account_holder="Navneet", inital_balance=0)

while True:
    user_input = input("""
    How would you like to proceed?
1. Enter 1 to deposit amount.
2. Enter 2 to withdraw amount.
3. Enter 3 to check balance.
4. Enter 4 to exit.
>""")

    if user_input == "1":
        account.deposit_amount()
    elif user_input == "2":
        account.withdraw_amount()
    elif user_input == "3":
        account.check_balance()
    elif user_input == "4":
        print("Thank u for banking with us!")
        break
    else:
        print("Invalid option selected. Please choose a number from 1 to 4.")
             

           

    
        