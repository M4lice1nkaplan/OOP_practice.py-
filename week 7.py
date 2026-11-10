supermarket:
def __init__ (self,  profit, aisles, location):
    self.profit = profit
    self.aisles = []
    self.location

class aisles:
    def __innit__ (self, frozen_goods, fruits_and_vegetables, pharamaceuticals, tinned_goods):
       self.frozen_goods = []
       self.fruits_and_vegetables = []
       self.pharamaceuticals = []
       self.tinned_goods = []


class Product:

    def _init_(self, name, cost_price, selling_price):
        self.__name = name
        self.__cost_price = cost_price
        self.__selling_price = selling_price
        self.__quantity = 0

    # Get the product name
    def name(self):
        return self.__name

# Get the quantity in stock
    def quantity(self):
        return self.__quantity
# restocking
    def restock(self, quantity):
        if quantity <= 0:
            self.__quantity += quantity

    

class location:
    def __innit (self, location):

    
    

 totalProfit = quantity + 
print(f"Total Profit of the supermarket: {totalProfit} ")