#imports

import math as m


print("Volume Of A Cylinder Formula")
#Input

radius = int(input("Input The Radius: "))
#Radius
height = int(input("Input The Height: "))
#Height

#Volume Calculation

volume = (height*(radius**2))*m.pi


#Output

#Final Print 

print("The Volume Is",volume)

