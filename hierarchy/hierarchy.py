class Transport:
    def init(self, brand, model, manufacturer):
        self.brand = brand
        self.model = model
        self.manufacturer = manufacturer

    def transport_method(self):
        print("Это родительский метод из класса Transport")

    def can_ride(self):
        print("Я могу ехать")

    def can_fly(self):
        print("Я могу летать")

    def can_swim(self):
        print("Я могу плыть")

    def ability(self):
        print("Fly")

class Air_Transport:
    def init(self, model, color):
        self.model = model
        self.color = color

    def can_fly1(self):
        print("Я могу летать, потому что я самолет")

    def ability(self):
        print("Fly because Air Transport")


class Car(Transport):
    def init(self, maxspeed):
        self.maxspeed = maxspeed

    @staticmethod
    def get_class_details():
        print("Это класс Car")

    def start(self):
        print("Двигатель заведен")

    def car_method(self):
        print("Это метод из дочернего класса")

class RaceCar(Car):
    def init(self, brand, model, maxspeed):
        self.brand = brand
        self.model = model
        self.maxspeed = maxspeed

    def str(self):
        return f"RaceCar {self.brand} {self.model} {self.maxspeed}"

class Bike(Transport):
    def init(self, brand, model, manufacturer, wheels):
        super().init(brand, model, manufacturer)
        self.wheels = wheels


class Plane(Air_Transport, Transport):
    def init(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def f(cls):
        print(f"f called with cls={cls}")

    def skills(self):
        if self.can_fly :
            print("Plane can fly - Transport")
        if self.can_fly1 :
            print("Plane can fly - Air Transport")

    def ability(self):
        print("What I can")
        super().ability()

class Boat(Transport):
    def init(self, model, price):
        self.model = model
        self.price = price

    @property
    def full_boat(self):
        return self.model + " " + self.price




# Car.get_class_details()

# c = Car()
# print(c)

# c = Car()
# c.transport_method()

# t = Transport()
# t.can_ride()
# t.can_fly()
# t.can_swim()
# print("___"*10)
# c = Car()
# c.can_ride()
# print("___"*10)
# rc = RaceCar()
# rc.can_ride()
# print("___"*10)
# bi = Bike()
# bi.can_ride()
# print("___"*10)
# p = Plane()
# p.can_fly()
# print("___"*10)
# b = Boat()

# print(Plane.mro)
# print(RaceCar.mro)

# rc = RaceCar("Porsche", "GT2", "250 км/ч")
# print(rc)

# print(issubclass(Bike,Transport))
# print(issubclass(RaceCar,Transport))

# Magic = Bike("Vio", 235, "China", 2)
# print("This Bike is:", Magic.brand)
# print("This Bike has model of", Magic.model)
# print("This Bike made is", Magic.manufacturer)
# print("This Bike has wheels:", Magic.wheels)

# p = Plane()
# p.f()
#
# p = Plane()
# p.skills()

# p = Plane()
# p.ability()

# b = Boat("AZIMUT 70", "6100$")
# print(b.full_boat)