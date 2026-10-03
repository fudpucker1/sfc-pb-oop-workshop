class BankAccount:
   def __init__(self, balance):
      self.balance = balance

   def check_balance(self):
      return self.balance
   def deposit(self, ammount):
      self.balance += ammount
      return self.balance
   def withdraw(self, ammount):
      if self.balance - ammount < 0:
         return "Insufficient funds"
      else:
         self.balance -= ammount
         return self.balance