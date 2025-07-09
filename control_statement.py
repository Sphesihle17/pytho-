#if statement 
num = 8
if num > 0:
    print("The number is positive")
    
    
    #else-if  statement
elif num == 0: 
    print("The number is zero")
    
    
    # else statement
else:
    print("The number is negative")
    
    
    


#asking for user input using else, if and else-if statement

num1 = int(input("Please enter the first number"))
num2 = int(input("Please enter the second number"))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 >num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")