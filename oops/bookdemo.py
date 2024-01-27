class Book:
    
    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        # initialize instance variables
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
            print(self.name,self.author,self.pages,self.price)

    def __str__(self):
        return self.name

obj=Book("randamoozham","mt",435,234)

obj.display_book()

print(obj)