import random
import os

class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance

    def send_money(self, amount, recipient):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"{self.account_number},{self.password},{self.account_type},{self.balance}"

class BusinessAccount(Account):
    pass

class PersonalAccount(Account):
    pass

class Bank:
    def __init__(self, accounts_file="accounts.txt"):
        self.accounts_file = accounts_file
        self.accounts = self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(self.accounts_file):
            return {}
        
        accounts = {}
        with open(self.accounts_file, 'r') as file:
            for line in file:
                account_number, password, account_type, balance = line.strip().split(',')
                balance = float(balance)
                if account_type == "Business":
                    accounts[account_number] = BusinessAccount(account_number, password, account_type, balance)
                else:
                    accounts[account_number] = PersonalAccount(account_number, password, account_type, balance)
        return accounts

    def save_accounts(self):
        with open(self.accounts_file, 'w') as file:
            for account in self.accounts.values():
                file.write(str(account) + "\n")

    def create_account(self, account_type):
        account_number = str(random.randint(100000, 999999))
        password = str(random.randint(1000, 9999))
        if account_type == "Business":
            account = BusinessAccount(account_number, password, account_type)
        else:
            account = PersonalAccount(account_number, password, account_type)
        
        self.accounts[account_number] = account
        self.save_accounts()
        return account_number, password

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            return account
        return None

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            self.save_accounts()
            return True
        return False

def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank")
        print("1. Open Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            account_type = input("Enter account type (Business/Personal): ")
            account_number, password = bank.create_account(account_type)
            print(f"Account created. Your account number is {account_number} and password is {password}")

        elif choice == '2':
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            account = bank.login(account_number, password)
            if account:
                print("Login successful!")
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Send Money")
                    print("5. Delete Account")
                    print("6. Logout")

                    choice = input("Choose an option: ")

                    if choice == '1':
                        print(f"Your balance is: {account.check_balance()}")

                    elif choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        if account.deposit(amount):
                            bank.save_accounts()
                            print(f"Deposited {amount}. New balance is: {account.check_balance()}")
                        else:
                            print("Invalid amount.")

                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        if account.withdraw(amount):
                            bank.save_accounts()
                            print(f"Withdrew {amount}. New balance is: {account.check_balance()}")
                        else:
                            print("Insufficient funds or invalid amount.")

                    elif choice == '4':
                        recipient_number = input("Enter recipient account number: ")
                        amount = float(input("Enter amount to send: "))
                        recipient = bank.accounts.get(recipient_number)
                        if recipient and account.send_money(amount, recipient):
                            bank.save_accounts()
                            print(f"Sent {amount} to {recipient_number}. New balance is: {account.check_balance()}")
                        else:
                            print("Insufficient funds or invalid recipient.")

                    elif choice == '5':
                        if bank.delete_account(account_number):
                            print("Account deleted successfully.")
                            break
                        else:
                            print("Error deleting account.")

                    elif choice == '6':
                        print("Logged out.")
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Invalid account number or password.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

