class Bank:
    def __init__(self,ac=0,n='nil',t='nil',b=0):
        self.ac=ac
        self.n=n
        self.t=t
        self.b=b
    def deposit(self,amount=0):
        self.b+=amount
        print("NEW BALANCE OF",self.ac," : ",self.b)
    def withdraw(self,amount=0):
        if(amount>self.b):
            print("insufficient balance")
        else:
            self.b-=amount
            print("NEW BALANCE OF",self.ac," : ",self.b)
    def show(self):
        print('DETAILS')
        print('AC NO : ',self.ac)
        print('Name : ',self.n)
        print('Type : ',self.t)
        print('balance : ',self.b)

c1=Bank(1,'Meryl John','Savings')
c2=Bank(2,'Sonu','Savings')
c1.show()
c2.show()
c1.deposit(1000)
c2.deposit(500)
c1.withdraw(655)
c2.withdraw(600)
