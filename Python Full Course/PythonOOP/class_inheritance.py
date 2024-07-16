# import abc
# from abc import ABC, abstractclassmethod #abstract base class
import functools
#SECTION -------------------------------------------------------------------------------------------------------------------
#class inheritance
# class Animal:
#     alive = True

#     def eat(self):
#         print(f"The animal is eating.")

#     def sleep(self):
#         print(f"The animal is sleeping.")

# class Rabbit(Animal):
#     def run(self):
#         print(f"This rabbit is running.")

# class Fish(Animal):
#     def run(self):
#         print(f"This animal is swimming.")

# class Hawk(Animal):
#     def fly(self):
#         print(f"This animal is flying.")

# rabbit = Rabbit()
# # fish = Fish()
# # hawk = Hawk()

# print(rabbit.alive)
# print(rabbit.run())

#SECTION -------------------------------------------------------------------------------------------------------------------
#multi-level inheritance

# class Organism:
#     alive=True

# class Animal(Organism):
#     def eat(self):
#         print("This animal is eating")

# class Dog(Animal):

#     def bark(self):
#         print("This dog is barking")

# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

#SECTION -------------------------------------------------------------------------------------------------------------------
#multiple inheritance - when a child class is derived from more than one parent class

# class Prey:
#     def flee(self):
#         print("This animal flees.")

# class Predator:
#     def hunt(self):
#         print("This animal is hunting.")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Predator,Prey):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
# # rabbit.flee()
# # hawk.hunt()
# fish.hunt()
# fish.flee()

#SECTION -------------------------------------------------------------------------------------------------------------------
#method overriding
# class Animal:
#     alive = True

#     def eat(self):
#         print(f"The animal is eating.")

# class Rabbit(Animal):
#     def run(self):
#         print(f"This rabbit is running.")

#     def eat(self):
#         print(f"This rabbit is eating")

# rabbit = Rabbit()
# rabbit.eat() #An object will use a method more closely associated with itself, before looking for that method in its parent objects
#SECTION -------------------------------------------------------------------------------------------------------------------
#method chaining
#method chaining =  calling multiple methods sequentially
                    #each call performs an action on the slame object and returns self
# class Car:
#     def turn_on(self):
#         print ("You start the engine")
#         return self
    
#     def drive (self):
#         print ("You drive the car")
#         return self
    
#     def brake(self):
#         print ("You step on the brakes")
#         return self
    
#     def turn_off(self):
#         print ("You turn off the engine")
#         return self
    
# car = Car()
# car.turn_on().drive()
# # car.brake().turn_off()
# car. turn_on()\
#         .brake()\
#         .drive()\
#         .turn_off()
#SECTION -------------------------------------------------------------------------------------------------------------------
# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):
#     def __init__(self, length,width):
#         super().__init__(length,width)

#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle) :
#     def __init__(self, length, width,height ):
#         super().__init__(length, width)
#         self.height = height

#     def volume(self):
#         return self.length*self.width*self.height

# square = Square(3,3)
# cube = Cube(length=1,width=2,height=3)

# print(square.area())
# print(cube.volume())
#SECTION -------------------------------------------------------------------------------------------------------------------
# ##Abstract Classes
# #Prevents a user from creating an object of that class
# # + compels a user to override abstract methods in a child class
# # abstract class - a class which contains one or more abstract methods.
# # abstract method - a method that has a declaration but does not have an implementation.

# #used to create base classes that have  the base parameters and methods of child classes, but not complete implementations

# class Vehicle:
#     @abstractclassmethod #signifies that method is abstract, and can't be inherited. Must be overridden in child class
#     def go(self):
#         pass

#     def stop(self):
#         print("the vehicle is stopped.")

# class Car (Vehicle):
#     def go(self):
#         print ("You drive the car")
# class Motorcycle(Vehicle):
#     pass
#     # def go(self):
#     #     print ("You ride the motorcycle")

# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle ()

# vehicle=Vehicle() #error if instiantiated, because it includes an @abstractclassmethod

# print(motorcycle.go())
# #in the example above, Vehicle is a base class that only has the stuff that's common to all vehicles - NOT a complete class in itself
#SECTION -------------------------------------------------------------------------------------------------------------------
#pass objects as arguments
#need to use

# class Car:
#     color: None
#     def change_color(car,color): #inside class
#         car.color=color


# class Motorcycle:
#     color:None

# def change_color(car,color): #outside of class
#     car.color=color

# car_1=Car()
# car_2=Car()
# car_3=Car()
# bike_1=Motorcycle()

# change_color(car_1,"red")
# change_color(car_2,"blue")
# change_color(car_3,"green")
# change_color(bike_1,"black")
# car_1.change_color("white")

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)
#SECTION -------------------------------------------------------------------------------------------------------------------
# # Duck typing
# # - concept where the class of an object is less important than the methods
# # class type is not checked if minimum methods/ attributes are present
# # "If it walks like a duck, and it quacks like a duck, then it must be a duck"

# class Duck:
#     def walk(self):
#         print ("This duck is walking")

#     def talk(self):
#         print ("This duck is quacking")

# class Chicken: #same methods, but slightly different
#     def walk(self):
#         print ("This chicken is walking")

#     # def talk(self):
#     #     print ("This chicken is clucking")

# class Person:
#     def catch(self, duck):
#         duck.walk()
#         # duck.talk()
#         print ("You caught the critter!!")

# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(duck)
# person.catch(chicken) 
#the Person object is set to use duck.walk and duck.talk. 
#However, because chicken ALSO has walk and talk, we can use chicken, and the 
#Person object will use chicken.walk and chicken.talk

#If I comment out duck.talk() in person, and chicken.talk in chicken, I can still call person.catch(chicken), because Chicken has a walk, and Person is ONLY using walk
#SECTION -------------------------------------------------------------------------------------------------------------------
#walrus (assignment) operator :=
# assigns values to variables as part of a larger expression
# happy = True

#A
# foods = list ()
# while True:
#     food = input("What food do you like?:")
#     print(f" Selected Food: " + food)
#     if food == "quit":
#         break
#     foods.append ( food)

#B
# foods=list()
# while food := input("What food do you like?:") != "quit":
#     foods.append ( food)

#A is programatically equivalent to #B
#SECTION -------------------------------------------------------------------------------------------------------------------
#Assign Function to Variable
# def hello():
#     print("Hello")

# #in Python, everything is an object, so we can assign functions to variables.
# print(hello) #memory address of hello() function
# hi = hello
# print(hi) #memory address of hello() function, since they're the same

# say = print
# say("Hello")

#   Higher Order Function = a function that either::
#                           1.  accepts a function as an argument
#                               or
#                           2.  returns a function
#                           (In python, functions are also treated as objects)

#Part 1 (accepts a function as an argument): 
# def loud(text) :
#     return text.upper()

# def quiet(text):
#     return text. lower ()

# def hello(func):
#     text = func("Hello")
#     print(text)

# hello(loud)
# hello(quiet)
#Becasue a function is passed in as an argument, the function is run when the higher order function is called

# def loud(text) :
#     return text.upper()

# def quiet(text):
#     return text. lower ()

# def hello(func,text):
#     text = func(text)
#     print(text)

# hello(loud,"You are too loud")
# hello(quiet,"You are too quiet")
#I can also pass in a variable as well as a function, and run that function with the variables as arguments


#Part 2(returns a function):
#we can call a function with an argument, assign that to a variable, then use that as a function with its own argument
# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend

# divide = divisor(2)
# print(divide(10))

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda parameters: expression

# double = lambda x:x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# full_name = lambda first_name, last_name: first_name+" "+last_name
# age_check = lambda age:True if age >= 18 else False
# print(f"Double: {double(5)}")
# print(f"Multiply: {multiply(6,7)}")
# print(f"Add: {add(6,7,8)}")
# print(f"Full Name: {full_name("Fred","McMurray")}")
# print(f"Age Check: {age_check(5)}")
#SECTION -------------------------------------------------------------------------------------------------------------------
#SORTING 
# sort() method of lists     = used with lists (not tuples)
# sort() function   = used with iterables (including tuples)


# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr . Krabs"] #list
# studentsTuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr . Krabs") #tuple


# students.sort(reverse=True)
# for i in students:
#     print(i)
# print("-----------------------------")
# sorted_Students = sorted(students, reverse=True) 
# print("sortedStudents (reverse): ")
# print(sorted_Students)

# # sorting list of tuples (name, gender, age)
# print("!!-----------------------------!!")
# students = [("Squidward", "F", 60),
# ("Sandy", "A", 33),
# ("Patrick","D", 36),
# ("Spongebob", "B", 20),
# ("Mr. Krabs", "C", 78) ]

# students.sort() #for lists
# for i in students:
#     print(i)
# print("@@-----------------------------@@")
# grade = lambda grade:grade[1] #set index to sort by to second element of tuple
# students.sort(key=grade) #set key to sort by to grade, which is already defined as the second element of tuple

# for i in students:
#     print(i)
# print("$$-----------------------------$$")
# age = lambda age:age[2] #set index to sort by to second element of tuple
# students.sort(key=age) #set key to sort by to grade, which is already defined as the second element of tuple
# for i in students:
#     print(i)


# sorting tuple of tuples (name, gender, age)
# print("!!-----------------------------!!")
# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Krabs","C", 78))

# age = lambda ages: ages [2]
# # students.sort(key=age,reverse=True)
# sorted_students = sorted(students,key=age)

# for i in sorted_students:
#     print(i)
#SECTION -------------------------------------------------------------------------------------------------------------------
# map () =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

# store = [("shirt", 20.00),
# ("pants", 25.00),
# ("jacket",50.00),
# ("socks",10.00) ]
# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# to_euros = lambda data: (data[0],"{:.2f}".format(round(data[1]*0.82,2))) #lambda for converting price (store[1]) to euros, returns tuple of data[0],data[1]
# #                                                                          {:.2f} rounds to 2 decimal places, but keeps trailing zeroes (eg. 5.20) 
# to_dollars = lambda data: (data[0],round(data[1]/0.82,2))

# store_dollars = list(                       #convert tuple to list
#                     map(                    #applies to_dollarsc() to each element of store. Returns map object 
#                         to_dollars, store
#                     )
#                 ) 

# store_euros = map(to_euros,store) #this is a map object

# for j in store_euros:
#     print(j)
# print('******************************')

# for i in store_dollars:
#     print(i)
#SECTION -------------------------------------------------------------------------------------------------------------------

# filter() = creates a collection of elements from an iterable for which a function returns true

# filter(function, iterable)

# friends = [("Rachel",19),
# ("Monica",18),
# ("Phoebe", 17),
# ("Joey", 16),
# ("Chandler",21),
# ("Ross", 20) ]

# age = lambda data:data[1] >=18 #returns the tuple if data[1] (age) >=18

# drinking_buddies = list(filter(age, friends)) #gets list of tuples where tuple[1]>18

# age = lambda age:age[1] #set index to sort by to second element of tuple
# friends.sort(key=age)
# for i in friends:
#     print(i)
#SECTION -------------------------------------------------------------------------------------------------------------------
# reduce() =    apply a function to an iterable and reduce it to a single cumulative value.
#               performs function on first two elements and repeats process until 1 value remains
#               need list 
#
# reduce(function, iterable)

# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x, y,:x +y,letters)
# print(word)

# factorial = [20,3,2,1]
# result = functools.reduce(lambda x, y, :x * y, factorial)
# print(result)

#SECTION -------------------------------------------------------------------------------------------------------------------
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression (conditional if/else if needed) for item in iterable ]

# squares = []                # create an empty list
# for i in range(1,11):       # create a for loop
#     squares.append(i * i)       # define what each loop iteration should do
# print(squares)
# # print('******************************')
# squares = [i * i for i in range(1,11)]
# print(squares)

# students = [100,90,80,70,60,50,40,30,0]

# passed_students = list(filter(lambda x: x >= 60, students) )
# print(f"1: {passed_students}")
# passed_students = [i for i in students if i >= 60]
# print(f"2: {passed_students}")

# print('******************************')

# students = [
#     ("Rachel",80),
#     ("Monica",63),
#     ("Phoebe", 22),
#     ("Joey", 100),
#     ("Chandler",84),
#     ("Ross", 0),
#     ("Lydia",97),
#     ("Ohanna",82)
# ]

# passed_students = [i for i in students if i[1]>=60]
# print(f"2: {passed_students}")

#
#SECTION -------------------------------------------------------------------------------------------------------------------
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50} #F = Fahrenheit
# cities_in_C = {key: (round(5/9*(value - 32))) for (key,value) in cities_in_F.items()}

# print(f"Cities in F: {cities_in_F}")
# print(f"Cities in C: {cities_in_C}")

# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago':"cloudy"}
# sunny_weather = {key for (key,value) in weather.items() if  value=="sunny"}
# print('-----------------------------------------')
# print(f"Sunny Weather Cities{sunny_weather}")
# print('-----------------------------------------')
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities. items ()}
# print(f"Desc Cities{desc_cities}")

# print('-----------------------------------------')

# def check_temp(value):
#     if value>=70:
#         return "HOT"
#     elif value>=40:
#         return "WARM"
#     else:
#         return "COLD"
    

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key, value) in cities. items ()}
# print(desc_cities)

#SECTION -------------------------------------------------------------------------------------------------------------------
# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element (a[0] is paired with b[0])

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")

# users = dict(zip(usernames,passwords)) 
# for i in users:
#     print(i)

# print(type(users))

# users = dict(zip(usernames,passwords)) 
# for key,value in users.items():
#     print(f"Key:{key}, Value:{value}")


usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users=zip(usernames,passwords,login_date)

for i in users:
    print(i)