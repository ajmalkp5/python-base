class Shapes:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    

class Rectangle(Shapes):

    l:int
    b:int

    def __init__(self, name,l,b):
        super().__init__(name)
        self.l=l
        self.b=b

    def area(self):
        result=self.l*self.b
        print(result)
    

rec_obj=Rectangle("rectangle",10,5)
rec_obj.area()