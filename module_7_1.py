
class Product:
    def __init__(self,name='Potato',weight= 50.5,category='Vegetables'):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name,'r')
        a=file.read()
        file.close()
        return a

    def add(self,*products):
        _list_prod =str(self.get_products())
        file = open(self.__file_name,'a')

        for i in products:
            if _list_prod.__contains__(str(i)):
                print(f'Продукт {i.name} уже есть в магазине.')
            else:
                file.write(str(i))
                file.write('\n')
        file.close()

s1 = Shop()
p1 = Product('Potato',50.5,'Vegetables')
p2 = Product('Spaghetti',3.4,'Droceries')
p3 = Product('Potato',5.5,'Vegetables')
print(p2)
s1.add (p1,p2,p3)
print(s1.get_products())

