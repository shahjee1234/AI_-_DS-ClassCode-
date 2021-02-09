class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make+ ' ' +self.model
        return long_name.title()
    def read_odometer(self,mileage):
         print("This car has " + str(self.odometer_reading) + " miles on it")
        
   # def update_odometer(self,mileage):
        
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
        
        
class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.resturant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def increment_number_served(self):
        
        self.number_served += 1
    def describe_restaurant(self):
         print(self.resturant_name,self.cuisine_type)
    def open_restaurant(self):
        print("The resturant {self.restaurant_name} is open")
    
restaurant = Restaurant("ABC rest","Desi")


def additionalfunc():
    print("I am additional function")
