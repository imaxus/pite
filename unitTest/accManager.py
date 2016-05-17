from Bank import BankAccount as bn


class AccManager(object):

    def __init__(self):
        self.accounts =[]

    def add_account(self,name,init_cash=0):
        self.accounts.append(bn(name,init_cash))

    def display_accounts(self):
        for i in self.accounts:
             print "name: ",i.name," balance: ",i.balance


bank = AccManager()
bank.add_account("john",20)
bank.add_account("meryl")
bank.display_accounts()