from abc import ABC , abstractmethod


class BankAccount(ABC):
    def __init__(self,account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balancr = balance


    @abstractmethod
    def deposit(self , amount):
        pass

    @abstractmethod
    def withdraw(self , amount):
        pass

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"account: {self.account_number},, holder: {self.account_holder},, balance: {self.balance} Taka"


class SavingAccount(BankAccount):
    def __init__(self,account_number, account_holder, balance=0, interest_rate = 0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} taka deposited successfully")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} Taka withdrawn successfully")
        else:
            print(f"{amount} Taka is insufficient")

    def add_interst(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest:.2f} Taka added")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self,account_number, account_holder, balance=0):
        if account_number in self.accounts:
            print("This account number already exists")
            return
        account = SavingsAccount(account_number, account_holder, balance)
        self.accounts[account_number] = account
        print(f"Savings account created for {account_holder}")

    def get_account(self , account_number):
        return self.accounts.get(account_number , None)

    
    def display_account(self):
        if not self.accounts:
            print("Account not available")
        for acc in self.accounts.values():
            print(acc)

def main():
    bank = BankSystem()

    while True:
        print("\n ====== Savings account menu ======")
        print("1. Create account")
        print("2.Deposit Money")
        print("3. Withdraw Money")
        print("4. Check balance")
        print("5. Add interest")
        print("6. Display all accounts ")
        print("7. Exit")
        choice = input("Enter your chocie:")


        if chocie == "1" :
            acc_num = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(acc_num , acc_holder , balance)


        elif choice == "2" :
            acc_num = input("Enter account number:")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter deposit amount:"))
                account.deposit(amount)
            else:
                print("Account not found")

        elif choice == "3":
            acc_num = input("Enter acount number:")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter withdraw amount:"))
                account.wothdraw(amount)
            else:
                print("Account not found")
        

        elif choice == "4":
            acc_num = input("Enter acount number:")
            account = bank.get_account(acc_num)
            if account:
                print(f"balance ; {account.get_balance()} Taka")
            else:
                print("Account not found")

        elif choice == "5":
            acc_num = input("Enter acount number:")
            account = bank.get_account(acc_num)
            if account:
                
                account.add_interst()
            else:
                print("Account not found")
        
        elif choice == "6":
            bank.display_account()

        elif choice == "7":
            print("Thanks for using it ")
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()






        


