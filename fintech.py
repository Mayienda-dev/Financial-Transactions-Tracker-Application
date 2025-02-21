class Info:
    
    def __init__(self, name, pin, email, amount):
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
    def __init__(self, name, pin, email, amount):
        super().__init__(name, pin, email, amount)
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
            print(f"Account Balance on Credit: {self.amount}")
        else:
            print(f"Failed Insufficient account balance. Your account balance is {self.amount}")

        transaction = {"type": "Credit", "amount": credit, "description": description}
        self.credit_transactions.append(transaction)
        self.all_transactions.append(transaction)

    def transaction_history(self):
        if not self.all_transactions:
            print("No transactions yet")
            return
        print("-----------Transaction histrory----------------------")
        for transactions in self.all_transactions:
            type_label = "DEPOSIT" if transactions["type"] == "Debit" else "WITHDRAWAL"
           
            print(f"{type_label}:{transactions["amount"]} - {transactions["description"]}")
        print("---------------------------------------------------------")

bank = Transactions("Reagan Mogambi", 4987, "reaganmogambi@gmail.com", 4000)
bank.profile_info()
bank.debit_transaction(1000, "salary")
bank.credit_transaction(500, "rent")
bank.transaction_history()