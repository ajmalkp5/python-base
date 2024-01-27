class Mobile:

    def __init__(self,name,brand,display,price):
        self.name=name
        self.brand=brand
        self.display=display
        self.price=price
        
    def display_Mobile(self):
        print(self.name,self.brand,self.display,self.price)

    def __str__(self):
        return self.name

obj=Mobile("iphone14pro","apple","amoled","80000")   
obj1=Mobile("s23ultra","samsung","amoled","120000")

obj.display_Mobile()

print(obj1)