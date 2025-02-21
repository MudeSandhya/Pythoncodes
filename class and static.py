class Bank:
    bname = "AXIS"
    roi = 0.01

    def __init__(self, name, phno, accno, adhar, pan, pin, bal):
        self.name = name
        self.phno = phno
        self.accno = accno
        self.adhar = adhar
        self.pan = pan
        self.pin = pin
        self.bal = bal

    def balcheck(self):
        """Check account balance after validating PIN."""
        print("Total number of attempts: 3")
        count = 0
        while count < 3:
            if self.checkpin() == self.pin:
                print(f"Available balance: {self.bal}")
                break
            else:
                count += 1
                print("Try again")
                print(f"Remaining attempts: {3 - count}")
        else:
            print("Failed too many times. Access denied.")

    @staticmethod
    def checkpin():
        """Static method to validate the PIN."""
        passcode = int(input("Enter the PIN: "))
        return passcode

    def deposit(self):
        """Deposit money into the account."""
        amount = int(input("Enter the amount to deposit: "))
        if amount <= 20000:
            self.bal += amount
            print("Amount credited successfully.")
            print(f"Account balance: {self.bal}")
        else:
            print("Maximum deposit amount is 20,000.")

    def withdraw(self):
        """Withdraw money from the account after validating PIN."""
        print("Number of attempts: 3")
        count = 0
        while count < 3:
            if self.checkpin() == self.pin:
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= 20000:
                    if self.bal >= amount:
                        self.bal -= amount
                        print("Successfully withdrawn the amount.")
                        print(f"Available balance: {self.bal}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Withdrawal amount must be less than or equal to 20,000.")
                break
            else:
                count += 1
                print("Incorrect PIN. Try again.")
                print(f"Remaining attempts: {3 - count}")
        else:
            print("Failed too many times. Withdrawal denied.")

    @classmethod
    def alterbankname(cls):
        """Change the bank name."""
        cls.bname = "State Bank of India"
        print(f"Bank name updated to: {cls.bname}")


# Example usage
user1 = Bank("Sindhiya", 7548819758, "AC40UCS34567", "ADHAR1234234", "PANNUMBER1", 181630, 10000)
user2 = Bank("Sandhiya", 7548869758, "AC40UCS34568", "ADHAR12349834", "PANNUMBER2", 181631, 1000)

# Testing deposit
user2.deposit()

# Testing withdraw
user2.withdraw()

# Testing balance check
user2.balcheck()

# Altering bank name
Bank.alterbankname()
