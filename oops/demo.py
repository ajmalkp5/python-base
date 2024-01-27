class Cuisine:

    name=str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class Dish(Cuisine):
    
    def __init__(self, name,dish_name,ingrediants,price):
        super().__init__(name)
        self.dish_name=dish_name
        self.ingrediants=ingrediants
        self.price=price

cs=Dish("akkk","saad","sassaa",90)
cs.dish_name


