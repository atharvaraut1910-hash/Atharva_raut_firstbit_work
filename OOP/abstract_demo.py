###Abstract method
#1.Method should


from abc import ABC, abstractmethod

class Vehicle(ABC);
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price

    @abstractmethod
    def stop():
        pass

class Car(Vehical):
    def __init__(self,brand,color,price,sunroof):
        super().__init__(brand,color,price)
        self.sunroof = sunroof
    def stop(self):
        print('')