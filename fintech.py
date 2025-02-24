class Info:
    
    def __init__(self, name, email, amount, pin):
        self.name = name.strip().title()
        self.email = email.strip().lower()
        self.amount = int(amount)
        self.pin = int(pin)
        self.details = [self.name, self.email, self.amount, self.pin]
        self.is_logged_in = False


    def profile_info(self):

        print("--------------Profile Information----------")
        labels = ["Name", "Email", "Amount", "Pin"]
        for label, value in zip(labels,self.details):
            print(f"{label} {value}")

        print("---------------------------------------------")


    def login(self, email, pin):
        if email == self.email:
            if pin == self.pin:
                self.is_logged_in = True
                print(f"Welcome back, {self.name}")
                return True
            else:
                print("Access denied, Incorrect pin")
                return False
        else:
            print("Account not found that is associated with this email")
            return False
    def logout(self):
        self.is_logged_in = False
        print("Logged out succesfully")

class Transactions(Info):
    def __init__(self, name, email, amount, pin):
        super().__init__(name, email, amount, pin)
        self.debit_transactions = []
        self.credit_transactions = []
        self.all_transactions = []

    def debit_transaction(self, debit, description = "Deposit"):
        if not self.is_logged_in:
            print("Please Login first to make transactions")
            return

        self.amount += int(debit)
        print(f"Account Balance on Debit: {self.amount}")

        transaction = {"type": "Debit", "amount": debit, "description": description}
        self.debit_transactions.append(transaction)
        self.all_transactions.append(transaction)


    def credit_transaction(self, credit, description):
        if not self.is_logged_in:
            print("Please login first to make a transaction")
            return

        if self.amount >= int(credit):
            self.amount-= int(credit)
            print(f"Account Balance: {self.amount}")
        else:
            print(f"Failed Insufficient account balance. Your account balance is {self.amount}")

        transaction = {"type": "Credit", "amount": credit, "description": description}
        self.credit_transactions.append(transaction)
        self.all_transactions.append(transaction)

    def transaction_history(self):
        if not self.is_logged_in:
            print("Please login to view transactions")
            return

        if not self.all_transactions:
            print("No transactions yet")
            return
        print("-----------Transaction history----------------------")
        for x in self.all_transactions:
            type_label = "DEPOSIT" if x["type"] == "Debit" else "WITHDRAWAL"
           
            print(f"{type_label}:{x["amount"]} - {x["description"]}")
        print("---------------------------------------------------------")

user_account = None
transactions = None

while True:
    try:
        print("Welcome to the Reagan FinApp. Please select an option to continue")
        if user_account is None or not user_account.is_logged_in:
            print("1. Create an account\n2.Login to your account\n3. Exit")
        else:
            print("1. Deposit money\n2. Withdraw money\n3. Financial statement\n4.Logout\n 5. Exit")
        option = int(input("Please, enter your option to proceed: "))
        
        if user_account is None or not user_account.is_logged_in:
            if option == 1:
                print("Please enter the following to open an account")

                name = input("Enter your full name: ").strip().title()
                email = input("Enter your email: ").strip().lower()
                amount = int(input("Enter the amount you would wish to deposit to your account: "))
                pin = int(input("Enter your pin(four digits): "))

                user_account = Info(name, email, amount, pin)
                transactions = Transactions(name, email, amount, pin)
                user_account.profile_info()
        
            elif option == 2:
                if user_account is None:
                    print("No account exists please create an account")
                    continue
                email = input("Enter your email: ").strip().lower()
                pin = int(input("Enter your pin: "))

                if user_account.login(email, pin):
                    transactions.is_logged_in = True
                    print("Login succesful!")

            elif option == 3:
                print("Exiting the system, bye!")
                break


        else:
            if option == 1:
                debit = int(input("Please enter the amount to deposit: "))
                description = input("Please enter a description of the transaction: ")
                transactions.debit_transaction(debit = debit, description = description)
                user_account.amount = transactions.amount

            elif option == 2:
                credit = int(input("Enter the amount to withdraw: "))
                description = input("Enter a description of the withdrawal: ")
                transactions.credit_transaction(credit = credit, description = description)
                user_account.amount = transactions.amount

            elif option == 3:
                transactions.transaction_history()

            elif option == 4:
                user_account.logout()
                transactions.is_logged_in = False
                print("Logged out succesfully")

            elif option == 5:
                print("Exiting the system, goodbye!")
                break
    except ValueError:
        print("Invalid input, please enter a number")