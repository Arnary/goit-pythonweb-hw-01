from abc import ABC, abstractmethod


class Vehicle(ABC): 
    def __init__(self, make, model, spec=None):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model): 
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec}): Мотор заведено")

class USVehicleFactory(VehicleFactory): 
    def create_car(self, make, model):
        return Car(make, model, 'US Spec')

    def create_motorcycle(self, make, model): 
        return Motorcycle(make, model, 'US Spec')

class EUVehicleFactor(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, 'EU Spec')

    def create_motorcycle(self, make, model): 
        return Motorcycle(make, model, 'EU Spec')


# Використання
vehicle1 = USVehicleFactory().create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = USVehicleFactory().create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

vehicle3 = EUVehicleFactor().create_car("Toyota", "Corolla")
vehicle3.start_engine()

vehicle4 = EUVehicleFactor().create_motorcycle("Harley-Davidson", "Sportster")
vehicle4.start_engine()
