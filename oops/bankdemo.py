class Bank:

    ac_num=str
    name=str
    ac_type=str
    ifsc_code=str
    branch=str
    balance=int

    def create_account(self,ac_num,name,ac_type,ifsc_code,branch,balance):
        self.ac_num=ac_num
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance


    def deposit(self,amount):

        self.balance+=amount
        print(f"your {self.ac_num} has been credited with {amount} aval bal is {self.balance}")

    def withdraw(self,amount):

        if amount>self.balance:

            print(" insufficient balance ")
        else:
            self.balance-=amount
        print(f"your {self.acno} has been debited with {amount} aval bal is {self.balance}")

    def get_balance(self):
        print("your aval bal is ",self.balance)

obj=Bank()
obj.create_account(123,"hari","savings","sbi00456","kakkanad",6000)

obj.deposit(500)
