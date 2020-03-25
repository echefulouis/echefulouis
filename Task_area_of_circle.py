import time #import the time library
import math #import the math library

def calculate(rad):           #Area calculation function
    area = math.pi * rad ** 2 #this is the formula for area of a circle
    return area

print('This program calculates the area of a circle')
time.sleep(1)     #delays for 2 seconds

x= float(input("Enter the radius of the Circle  ")) #collect the radius of the circle from the user


Area = calculate(x)

print ("The area of the circle is " + str(Area)) #Print the area of the circle


