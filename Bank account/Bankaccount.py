import datetime
import pytz


class Account(object):
    #simple account class with balance
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self , name ,  balance):
        self.__name = name
        self.__balance = balance
        self.__transaction_list = [(Account._current_time() , balance)]
        self.Showbalance()
        print("Account created for " + self.__name)

    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
            self.Showbalance()
            self.__transaction_list.append((Account._current_time() , amount))
    
    def withdraw(self , amount):
        if amount > self.__balance :
            print("You don't have enough money")
            self.Showbalance()
        else:
            self.__balance -= amount
            self.Showbalance()
            self.__transaction_list.append((Account._current_time() , -amount))

    def Showbalance(self):
        print("the balance is {}".format(self.__balance))
    
    def show_transactions(self):
        for date , amount in self.__transaction_list :
            if amount > 0 :
                tran_type = "Deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount , tran_type , date , date.astimezone()))

if __name__ == "__main__":
    amin=Account("amin" , 200)

# amin.__balance = 1000
amin.Showbalance()
amin.deposit(1000)
amin.withdraw(700)
amin.show_transactions()
