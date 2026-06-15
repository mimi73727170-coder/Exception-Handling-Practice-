try :
    num = int(input("Enter a number :"))
    print(num)
except :
    print("Please enter a valid number!")

try :
    num = 10/0
except ZeroDivisionError :
    print("Cannot divided by zero!")

try :
    num = int(input("Enter a number :"))
    result = 10/num
    print(result)

except ValueError :
    print("Enter value please!")

except ZeroDivisionError :
    print("Cannot divide by zero")

try :
    print(8/2)

except :
    print("Error")

finally :
    print("Program finished!")

try :
    num = int(input("Enter a number :"))
    print("You entered :",num)

except ValueError :
    print("Invalid input")

try :
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))

    result = num1/num2

    print("Answer :",result)

except ZeroDivisionError :
    print("Cannot divide by zero!")

except ValueError :
    print("Invalid input,please enter numbers only!")

try :
    num = int(input("Enter a number :"))
    print(num)

except ValueError :
    print("Invalid input")

finally :
    print("Program finished!")
    




