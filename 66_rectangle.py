class Rectangle:
    def __init__(self,l=0,w=0):
        self.__l=l
        self.__w=w
        self.a=l*w
    def __lt__(self,other):
        if self.a<other.a:
            return True
        else:
            return False

r1=Rectangle(10,10)
r2=Rectangle(50,2)
print(r1<r2)
