

class Employee:

    id:int
    name:str
    department:str
    salary:int


    def set_emp(self,id,name,dep,sal):
        self.id=id
        self.name=name
        self.department=dep
        self.salary=sal

    def display_emp(self):
        print(self.id,self.name,self.department,self.salary)

