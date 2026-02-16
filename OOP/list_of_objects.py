##Has a Relationship

class Car:
    def stop(self):
        print('Car stopped.')

class Bike:
    def stop(self):
        print('Bike stopped.')

class Student:
    def display(self):
        print('Student data displayed.')

c1 = Car()
b1 = Bike()
c2 = Car()
b2 = Bike()
s1 = Student()
list_of_objects = [c1,b1,c2,b2]
for obj in list_of_objects:
    obj.stop()