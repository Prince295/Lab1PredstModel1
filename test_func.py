from functions import *

class Place():
    capacity=0
    capacity_label = "Вместимость места проведения"
    address=""
    address_label = "Адрес"
    square=0
    square_label = "Площадь помещения"
    design={1 : "Восточный",
            2 : "Западный",
            3 : "Скандинавский",
            4 : "Детский"}
    design_label = "Дизайн интерьера"
    price=0
    price_label = "цена"
    def __init__(self, capacity, price, design, square, address):
        self.capacity = capacity
        self.price = price
        self.design = design
        self.square = square
        self.address = address
name=[]
for i in range(5):
    name.append(Place(12,'Gorod',120,Place.design[1], 40000))
print(name[0].design)