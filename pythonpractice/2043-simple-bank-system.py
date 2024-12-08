from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if money < 0:
            return False
        if self._hasEnoughMoney(account1, money) and self._isValidAccount(account2):
            self.accounts[account1 - 1] -= money
            self.accounts[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if money < 0:
            return False
        if self._isValidAccount(account):
            self.accounts[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if money < 0:
            return False
        if self._hasEnoughMoney(account, money):
            self.accounts[account - 1] -= money
            return True
        else:
            return False

    def _isValidAccount(self, accountId: int) -> bool:
        return accountId >= 1 and accountId <= len(self.accounts)

    def _hasEnoughMoney(self, accountId: int, money: int) -> bool:
        if self._isValidAccount(accountId):
            return money <= self.accounts[accountId - 1]
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
