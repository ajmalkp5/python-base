class Cloth:
    # title=str
    # brand:str
    # price:int

    def __init__(self,title,brand,price):
        self.title=title
        self.brand=brand
        self.price=price
    
    def __str__(self):
        return self.title
    
class Clothvarient(Cloth):

    def __init__(self, title, brand, price,color,size):
        super().__init__(title, brand, price)
        self.color=color
        self.size=size

cv=Clothvarient("ucb full sleeve","ucb",1300,"blue","m")
cv2=Clothvarient("ucb full sleeve","ucb",3300,"red","l")
print(cv)
