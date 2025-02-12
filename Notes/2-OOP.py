"""
OOP and Testing:

    Objects contain both data and code:
        Data is in the form of an attribute
        Code is in the form of methods
    
    Goal:
        Write code in a way to match what it represents
        Readable and Maintable code
    
    Class:
        Type
        "A blueprint for building objects"
    
    Object:
        Instance of a class
    
    Abstraction:
        Hiding Info

    Encapsulation:
        Grouping Info

        1. Combinging Data and the methods that operate on it into a single entity
        2. Partitioning attributes of a class into public and private

    Inheritance:
        Sharing Info

        A child class that inherits attributes from a parent class
            IE: A dog is an animal

    Polymorphism:
        Redefining Info

        Share a method but this method does different things for both classes
        Python does this through duck typing:
            Meaning we can pass a type of object to a function and it will work.

"""


class Car:
    def __init__(self, year, make, model, is_running=False):
        self.year = year
        self.make = make
        self.model = model
        self.is_running = is_running
        self._num_starts = 0

    def _check_starter_health(self):
        if self._num_starts <= 5000:
            return True

    def start(self):
        if self.is_running == False:
            if self._check_starter_health():
                self._num_starts += 1
                self.is_running = True
                return f"The {self.make} {self.model} is now running!"
            else:
                return f"Won't turn over"
        else:
            return f"The {self.make} {self.model} is already running!"

    def stop(self):
        if self.is_running == True:
            self.is_running = False
            return f"The {self.make} {self.model} has stopped!"
        else:
            return f"The {self.make} {self.model} is already stopped!"

    def __str__(self):
        return f"Year: {self.year}, Make: {self.make}, Model: {self.model}"


class electric_Car(Car):  # Inheritance, electric_Car gets all the methods and attributes of Car
    def __init__(self, year, make, model):
        super().__init__(year, make, model)
        self._battery_level = 100

    def drive(self, miles):
        if self._check_charge(miles):
            print(f"Driving {miles} miles")
        else:
            print("Not enough charge remaing")

    def recharge(self):
        self._battery_level = 100

    def _check_charge(self, miles):
        if miles <= self._battery_level * 2:
            return True
        else:
            return False
    
my_car = electric_Car(2014, "Mazda", 6)

my_car.drive(500)
