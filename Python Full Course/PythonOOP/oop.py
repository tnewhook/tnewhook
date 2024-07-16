from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue") #Don't need to pass in 'self'
car_1.wheels=2 #can change value of class variable for specific instance

car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.wheels)
car_1.drive()
car_1.stop()
print("----------------------------\n\n")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print(car_2.wheels)
car_2.drive()
car_2.stop()

print (Car.wheels) #because class variables defined outside instance of class, is already defined. Car1 isn't affected, since car1 wheels is defined on line 4

Car.wheels = 6 #this affects all instances of class variable
print(f"Car1 wheels: {car_1.wheels}")
print(f"Car2 wheels: {car_2.wheels}")
#instance variables defined inside the object init - only refer to that specific object
#class variable defined inside class, outside init - is a default referring to all instances of that class