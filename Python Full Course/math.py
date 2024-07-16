import timeCode

import math
pi = 3.14
x=1
y=2
z=3

Pi_Round = round(pi)
#ceiling, floor, abs, pow() [Power], sqrt
print(max(x,y,z)) #prints 3
print(min(x,y,z)) #prints 1

#slicing - create substring by extracting element from another string
#
name = "Trevor Newhook"
first_name = name[0:6]
print(first_name) #Trevor
first_name = name[0:6:2]
print(first_name) #Teo

website = "Http://google.com"
wikipedia = "http://wikipedia.com"
slice = slice(7,-4)
print(website[slice]) #google
print(wikipedia[slice]) #wikipedia

#if...else
age = int(input("How old are you?:"))


if age >=18:
    print("You are an adult!")
elif age == 100:
    print("you are a century!")
elif age<0:
    print("You haven't been born yet")
else:
    print("You are a child.")

temp = float(input("What is the temperature today?"))
#logical operators (and,or,not)
if temp>=0 and temp<=30:
    print("The temperature is good today. Go outside")
elif (temp<=0
      or temp>30):
    print("The temperature is crazy! Stay inside.")

#while loops
name = ""
while len(name)==0:
    name = input("Enter your name")
print("Hello " + name)

#For loops

for i in range(10):
    print(i+1)

for i in range(50,100+1):
    print(i)

for i in "my full name":
    print(i)

#sleep
for seconds in range(10,0,-1):
    if seconds== 1:
        print(str(seconds) + " Second")
    else:
        print(str(seconds)+" Seconds")
    time.sleep(1)
print("Happy New Year!")

#nested loops
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

#loop control
#break gets out of loop; pass skips over loop iteration (placeholder)
while True:
    name = input("Enter your name: ")
    if name != "":
        break

#Lists = arrays??
food=["pizza","hamburger","hot dog","spaghetti"]
print(food[2])


