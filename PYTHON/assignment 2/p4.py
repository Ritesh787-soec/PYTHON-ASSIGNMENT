class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin

    # Getter
    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect PIN!"

    # Setter
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Incorrect PIN!"
        if amount > self.__balance:
            return "Insufficient funds!"
        self.__balance -= amount
        return "Withdrawal successful!"


acc = BankAccount("Ravi", 5000, 1234)
print(acc.get_balance(1234))
