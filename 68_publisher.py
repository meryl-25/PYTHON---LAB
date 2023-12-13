
class Publisher:
    def __init__(self,name='nil'):
        self.name=name
    def display(self):
        print('Name : ',self.name)

class Book(Publisher):
    def __init__(self,name='nil',title='nil',author='nil'):
        super().__init__(name)
        self.title=title
        self.author=author

    def display(self):
        super().display()
        print('title : ',self.title)
        print('auhtor : ',self.author)

class Python(Book):
    def __init__(self,name='nil',title='nil',author='nil',price=0,nop=0):
        super().__init__(name,title,author)
        self.price=price
        self.nop=nop
        
    def display(self):
        super().display()
        print('price : ',self.price)
        print('no of pages : ',self.nop)

p1=Python('Revolution 2020','Fiction','Chetan Bhagath',120,450)
p2=Python('Alchemist','Fiction','Paulo Coelho',170,490)

print('BOOK 1')
p1.display()
print('')
print('BOOK 2')
p2.display()
