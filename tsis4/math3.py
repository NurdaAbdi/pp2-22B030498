import math
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
ap = length/(2*(math.tan(math.pi/sides)))
area = int((sides*length*ap)/2)
print("The area of the polygon is: ", area)
