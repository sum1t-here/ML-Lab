class BankAccount:
    def __init__(self,account_holder,initial_bal=0):
        self.__holder = account_holder
        self.__balance = initial_bal

    def get_acc_holder_details(self):
        print(f"Name of Acc Holder is {self.__holder}")

    def get_bal_details(self):
        return self.__balance
    
    def deposit(self,balance):
        if(balance>0):
            print(f"Balance deposited and new balance is {self.__balance+balance}")
        else:
            print("Invalid Amount")

account1 = BankAccount("IronMan", 1000000)
account1._BankAccount__balance
account1.deposit(1000)
# Balance deposited and new balance is 1001000