#importing the calculate module 
import calculate

# ASking the user to enter the length and width of the triangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#Now we are calling out the functions we created in the calculator module
area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f" The area of the rectagles is: {area}")
print(f" The perimeter of the rectagles is: {perimeter}")
