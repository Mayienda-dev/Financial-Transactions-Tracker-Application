class Info:
    
    def __init__(self, name, email, amount, pin):
        self.name = name.strip().title()
        self.email = email.strip().lower()
        self.amount = int(amount)
        self.pin = int(pin)
        self.details = [self.name, self.email, self.amount, self.pin]


    def profile_info(self):

        print("--------------Profile Information----------")
        labels = ["Name", "Email", "Amount", "Pin"]
        for label, value in zip(labels,self.details):
            print(f"{label} {value}")

        print("---------------------------------------------")


    def login(self):
        if self.email in self.details:
            current_pin = int(input("Please enter your pin: "))

            if current_pin == self.pin:
                print("Welcome to the Reagan bank app")

            else:
                print("Access denied. Please enter the correct pin")

        else:
            print("Account does not exist")

class Transactions(Info):
    def __init__(self, name, email, amount, pin):
        super().__init__(name, email, amount, pin)
        self.debit_transactions = []
        self.credit_transactions = []
        self.all_transactions = []

    def debit_transaction(self, debit, description = "Deposit"):
        self.amount += int(debit)
        print(f"Account Balance on Debit: {self.amount}")

        transaction = {"type": "Debit", "amount": debit, "description": description}
        self.debit_transactions.append(transaction)
        self.all_transactions.append(transaction)


    def credit_transaction(self, credit, description):
        if self.amount >= int(credit):
            self.amount-= int(credit)
            print(f"Account Balance: {self.amount}")
        else:
            print(f"Failed Insufficient account balance. Your account balance is {self.amount}")

        transaction = {"type": "Credit", "amount": credit, "description": description}
        self.credit_transactions.append(transaction)
        self.all_transactions.append(transaction)

    def transaction_history(self):
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
        print("Welcome to the Reagan FinApp. Please select an option to continue (1-4)")
        print("1. Create an account\n2. Login to your account\n3. Deposit money\n4. Withdraw money\n5. Financial statement\n6. Exit")
        option = int(input("Please, enter your option to proceed: "))
        

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
            user_account.login()


        elif option == 3:
            if user_account is None or transactions is None:
                print("Account not found, create an account")
                continue
            debit = int(input("Please enter the amount to deposit: "))
            description = input("Please enter a description of the transaction: ")
            transactions.debit_transaction(debit = debit, description = description)
            user_account.amount = transactions.amount

        elif option == 4:
            if user_account is None or transactions is None:
                print("User account not found. Please create an account first")
                continue
            
            credit = int(input("Enter the amount to withdraw: "))
            description = input("Enter a description of the withdrawal: ")
            transactions.credit_transaction(credit = credit, description = description)
            user_account.amount = transactions.amount

        elif option == 5:
           
            transactions.transaction_history()

        elif option == 6:
            print("Exiting the system, goodbye!")
            break
    except ValueError:
        print("Invalid input, please enter a number")