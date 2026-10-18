class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
           self.authenticated = True


    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Please authenticate first")
        if amount <= 0:
            raise Exception("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Please authenticate first")
        if amount <= 0:
            raise Exception("Amount must be positive")
        self.balance -= amount

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Please authenticate first")
        if amount <= 0:
            raise Exception("Amount must be positive")

        if self.balance - amount <= self.minimum_balance:
            raise Exception("Minimum balance requirement violated")

        self.balance -= amount

class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list):
            raise Exception("account_list must be a list")

        for account in account_list:
            if not isinstance(account, BankAccount):
                raise Exception("Invalid account in account_list")

        try:
            if (
                isinstance(try_limit, bool)
                or not isinstance(try_limit, (int, float))
                or try_limit <= 0
            ):
                raise Exception("try_limit must be positive")

            self.try_limit = int(try_limit)

        except Exception:
            print("Invalid try_limit. Setting it to 2.")
            self.try_limit = 2

        self.account_list = account_list
        self.current_tries = 0
        self.running = True

        self.show_main_menu()

    def show_main_menu(self):
        while self.running:
            print("\n=== ATM Main Menu ===")
            print("1. Log in")
            print("2. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)

            elif choice == "2":
                print("Goodbye!")
                self.running = False

            else:
                print("Invalid choice. Try again.")

    def log_in(self, username, password):
        while self.current_tries < self.try_limit:
            for account in self.account_list:
                account.authenticate(username, password)

                if account.authenticated:
                    print("Login successful!")
                    self.show_account_menu(account)
                    return

            self.current_tries += 1
            remaining = self.try_limit - self.current_tries

            if remaining == 0:
                print("Maximum login attempts reached.")
                self.running = False
                return

            print("Incorrect username or password.")
            print("Attempts remaining:", remaining)

            username = input("Username: ")
            password = input("Password: ")

    def show_account_menu(self, account):
        while self.running:
            print("\n=== Account Menu ===")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                    print("Deposit successful!")
                    print("Balance:", account.balance)
                except (ValueError, Exception) as error:
                    print("Error:", error)

            elif choice == "2":
                try:
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                    print("Withdrawal successful!")
                    print("Balance:", account.balance)
                except (ValueError, Exception) as error:
                    print("Error:", error)

            elif choice == "3":
                print("Returning to main menu.")
                return

            else:
                print("Invalid choice. Try again.")

account1 = BankAccount(1000, "Imane", "1234")
account2 = MinimumBalanceAccount(2000, "Sara", "5678", 500)

atm = ATM([account1, account2], 3)





