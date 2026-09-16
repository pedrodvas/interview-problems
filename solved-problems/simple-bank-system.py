class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1>len(self.balance) or account2>len(self.balance) or account1<1  or account2<1:
            return False
        if money < 0 or self.balance[account1-1] < money:
            return False
        try:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        except:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account>len(self.balance) or account<1:
            return False
        try:
            self.balance[account-1] += money
            return True
        except:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account>len(self.balance) or account<1:
            return False
        if money < 0 or self.balance[account-1] < money:
            return False
        try:
            self.balance[account-1] -= money
            return True
        except:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)