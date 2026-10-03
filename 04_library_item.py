class LibraryItem:
   def __init__(self, title, publication_date, identifier):
      self.title = title
      self.publication_date = publication_date
      self.identifier = identifier
      self.items = []

   def get_info(self):
      return f"Title: {self.title}, Publication Date: {self.publication_date}, Identifier: {self.identifier}"

class Book(LibraryItem):
   def __init__(self, title, publication_date, identifier, author, pages):
      super().__init__(title, publication_date, identifier)
      self.author = author
      self.pages = pages

   def get_info(self):
      return f"{super().get_info()}, Author: {self.author}, Pages: {self.pages}"

class Magazine(LibraryItem):
   def __init__(self, title, publication_date, identifier, issue_number, month):
      super().__init__(title, publication_date, identifier)
      self.issue_number = issue_number
      self.month = month

   def get_info(self):
      return f"{super().get_info()}, Issue Number: {self.issue_number}, Month: {self.month}"

class DVD(LibraryItem):
   def __init__(self, title, publication_date, identifier, duration, director):
      super().__init__(title, publication_date, identifier)
      self.duration = duration
      self.director = director

   def get_info(self):
      return f"{super().get_info()}, Duration: {self.duration}, Director: {self.director}"