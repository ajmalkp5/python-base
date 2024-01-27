class Parent:

    def mobile(self):
        print("redmi note 12")

    def vehicle(self):
        print("KTM")

class Child(Parent):

    def mobile(self):
        print("iphone 15")

        
ch=Child()
ch.mobile()
ch.vehicle()