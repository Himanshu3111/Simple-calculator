def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
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
    return num1 ** (1/3)

print("Please select the operator: \n" \
      "1. Addition\n" \
      "2. Substract\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n" \
      "6. Square\n"
      "7. Cube\n" \
      "8. Square root\n" \
      "9. Cube root\n")

select = int(input("Select a operator from 1, 2, 3, 4, 5, 6, 7, 8 or 9: "))

if select == (1, 2, 3, 4, 5):
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

else:
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

elif select == 9:
    print("\u221b",number3, "= ",\
          cube_root(number3))
    
else:
        print("Invalid operator.")
