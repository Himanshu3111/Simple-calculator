def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        raise ValueError("Can't divided by zero.")
    return num1 / num2

def avg(num1,num2):
    return (num1 + num2)/2

def squr(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def square_root(num1):
    return num1 ** 0.5

def cube_root(num1):
    return round(num1 ** (1/3))

def percent(num1, num2):
    if num2 == 0:
        raise ValueError("Total can't be zero")
    return (num2 / num1)* 100

print("Please select the operator: \n" \
      "For Addition       : Press '1' \n" \
      "For Substract      : Press '2'\n" \
      "For Multiplication : Press '3'\n" \
      "For Division       : Press '4'\n" \
      "For Average        : Press '5'\n" \
      "For Square         : Press '6'\n"
      "For Cube           : Press '7'\n" \
      "For Square root    : Press '8'\n" \
      "For Cube root      : Press '9'\n" \
      "For Percentage     : Press '10'\n")

select = int(input("Select a operator from 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10: "))

if select in (1, 2, 3, 4, 5):
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if select == 1:
        print(number1, "+", number2, "= ",\
              add(number1, number2))

    elif select == 2:
        print(number1, "-", number2, "= ",\
              sub(number1, number2))

    elif select == 3:
        print(number1, "*", number2, "= ",\
              multiply(number1, number2))

    elif select == 4:
        print(number1, "/", number2, "= ",\
              divide(number1, number2))

    else:
        print("(",number1, "+", number2,")/2 = ",\
              avg(number1, number2))

elif select in (6, 7, 8, 9):
    number3 = int(input("Enter the number: "))

    if select == 6:
        print(number3, " * ", number3, "= ",\
             squr(number3))
    
    elif select == 7:
        print(number3, " * " , number3, " * " , number3, "= ",\
            cube(number3))

    elif select == 8:
        print("\u221a",number3, "= ",\
              square_root(number3))

    else:
        print("\u221b",number3, "= ",\
              cube_root(number3))

elif select == 10:
    number4 = int(input("Enter total number: "))
    number5 = int(input("Enter other number: "))

    print("(", number5, "/" ,number4 ,") * 100 = ", \
          percent(number4, number5))

else:
    print("Invalid operator.")
