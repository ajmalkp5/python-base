class Student:

    name:str
    rollno:int
    subject:str
    mark:int

    def set_std(this,name,rollno,subject,mark):
        this.name=name
        this.rollno=rollno
        this.subject=subject
        this.mark=mark

    def display_std(this):
        print(this.name,this.rollno,this.subject,this.mark)

std1=Student()
std1.set_std("ajmal",26,"BCA",95)

std2=Student()
std2.set_std("fino",6,"BCA",85)


std1.display_std()
std2.display_std()