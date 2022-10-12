# constructors - is a function inside a class (__init__()), that is used to
# initialize attributes of a class
# A class contains attributes/properties/states and behaviour/methods
# Classes starts with capital letters e.g Book

class Book:
    def __init__(self, author, title, price, quantity):
        self.author = author
        self.title = title
        self.price = price
        self.quantity = quantity

    def show_book(self):
        print(f'The author is {self.author}, The title is {self.title}, Price {self.price}, and the quantity is {self.quantity}')


# should follow the order
book1 = Book("James","Python concepts","100$","20")

# book1.price = "100$"
# book1.author = "James"
# book1.title = "Python concepts"
# book1.quantity = "20"

book1.show_book()
