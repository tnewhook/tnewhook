class Car: #capitalize class name
    
    wheels = 4 #class variable - applies to all instances of class, can be customized
    def __init__ (self,make,model,year,color):
        self.make = make        #instance variables
        self.model = model      #instance variables
        self.year = year        #instance variables
        self.color = color      #instance variables


    def drive(self):
        print(f"The {self.color} car is driving.")

    def stop(self):
        print(f"This {self.make} {self.model} has stopped.")