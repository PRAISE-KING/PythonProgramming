# Bank Account
# properties - balance, acc no. ,name, branch ,active
# methods - check_balance(), deposit(),withdraw(), get_loan()


class Account:
    def __int__(self, balance, accno, name, branch, status):
        if balance < 0:
            print("balance cannot be zero")
        elif len(name) == 0:
            print("Please enter your name")
        elif len(accno) != 5:
            print("invalid account number")
        else:
            print("bank details captured")

        self.balance = balance
        self.accno = accno
        self.name = name
        self.branch = branch
        self.status = status

    def check_balance(self):
        print(self.balance)
        return self.balance

    def deposit(self, amount_to_deposit):
        if amount_to_deposit <= 0:
            print("Cannot deposit zero or negative amount")
        elif amount_to_deposit > 70000:
            print("exeeded the Maximum Deposit Amount")
        else:
            if self.status == "active":
                print("thank you for depositing with us")
                print(f'your previous balance was {self.check_balance()}')
                self.balance = self.balance + amount_to_deposit
                print(f'your current balance is {self.balance}')
            else:
                print("your account is active")

    def Withdraw(self,withdraw_amount,balance):
        if withdraw_amount > balance :
            print("Insuficient balance in the account")
        elif withdraw_amount >=101 :
            print("succefully withdrawn , Thank you")
        else:
            if self.status == "active":
                print("keep parnering with us")
                print(f'your previous balance was {self.check_balance()}')
                self.balance = self.balance - withdraw_amount
                print(f'your current balance is {self.balance}')
            else:
                print("Account is inactive")




account = Account()
account.balance = 100
account.accno = 12345
account.name = "Praizking"
account.branch = "Westlands"
account.status = "active"

account.check_balance()
account.deposit(10000)

# encapsulation
# exception handling

# Database - collection of tables with records
# C - creating a database /table , storing data
# R - retrieve data from data
# U - update the data
# D - delete the data

# MySQL, Oracle, SQLite, Postgesql....
# pymysql library/module
# Xampp/phpMyadmin database interface