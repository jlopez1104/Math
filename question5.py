import math

radius=float(input("Enter radiues of the cylinder: "))
height=float(input("Enter height of cylinder: "))
volume= math.pi *radius**2 * height
SurfaceArea = 2*math.pi*radius*(radius+height)
print("the volume of the cylinder in cm is ",volume,)
print("the surface area of the cylinder in cm is ",SurfaceArea,)