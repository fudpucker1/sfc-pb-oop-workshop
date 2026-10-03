class Receipt:
   def __init__(self, tax_rate):
      self.tax_rate = tax_rate
      self.items = []

   def add_item(self, item):
      self.items.append(item)

   def get_subtotal(self):
      return sum(item.get_total() for item in self.items)

   def get_total(self):
      return self.get_subtotal() * (1 + self.tax_rate)

class ReceiptItem:
   def __init__(self, quantity, price):
      self.quantity = quantity
      self.price = price

   def get_total(self):
      return self.quantity * self.price