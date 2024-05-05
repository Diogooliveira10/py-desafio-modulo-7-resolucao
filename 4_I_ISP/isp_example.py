# pdf, txt, excel

from abc import ABC, abstractmethod

class Document(ABC): # generic

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass

# class PDF(Document):
#     def load(self):
#         print("Load in PDF")

#     def view(self):
#         print("View informations")

#     def calculate(self):
#         print("no user")

#     def format(self):
#         print("no user")

# document1 = PDF()
# document1.load()

class DocumentPDF(ABC): # ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentTXT(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentExcel(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass