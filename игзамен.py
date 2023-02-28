#1
'''
def single_elements(tup1, tup2): 
  return set(tup1) ^ set(tup2) 
print(single_elements((1, 2, 3, 4), (3, 4, 5))) 
single_elements = lambda tup1, tup2: set(tup1) ^ set(tup2)
print(single_elements((1, 2, 3, 4), (3, 4, 5)))'''

#3

'''class Square:
    @staticmethod
    def get_sides():
        return 4
class Rectangle:
    @staticmethod
    def get_sides():
        return 4
class Triangle:
    @staticmethod
    def get_sides():
        return 3
def get_perimeter(shape):
    sides = shape.get_sides()
    return sides * 10
print(get_perimeter(Square))
print(get_perimeter(Rectangle))
print(get_perimeter(Triangle))
'''
#2

class Product:
    def __init__(self, name, description, price, quality):
        self.name = name
        self.description = description
        self.price = price
        self.quality = quality
        self.sold = 0
    
    def sell(self):
        self.sold += 1
        
    def get_number_sold(self):
        return self.sold


