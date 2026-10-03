class Vehicle:
   def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year
      self.items = []

   def get_info(self):
      return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
   def __init__(self, make, model, year, doors):
      super().__init__(make, model, year)
      self.doors = doors

   def get_info(self):
      return f"{super().get_info()}, Doors: {self.doors}"

class Truck(Vehicle):
   def __init__(self, make, model, year, towing_capacity):
      super().__init__(make, model, year)
      self.towing_capacity = towing_capacity

   def get_info(self):
      return f"{super().get_info()}, Towing Capacity: {self.towing_capacity}"

class Motorcycle(Vehicle):
   def __init__(self, make, model, year, type):
      super().__init__(make, model, year)
      self.type = type

   def get_info(self):
      return f"{super().get_info()}, Type: {self.type}"