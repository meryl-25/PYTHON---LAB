a=input("Enter some integers : ").split()
b=map(int,a)
newlist=list(map(lambda x:x+x*0.10 if x>1000 else x+x*0.05,b))
print("After increment : ",newlist)
