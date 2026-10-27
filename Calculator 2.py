import math
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

def root(num1,num2):
    return round(num2 ** (1/num1), 2)

def square_root(num1):
    return num1 ** 0.5

def cube_root(num1):
    return round(num1 ** (1/3))

def percent(num1, num2):
    if num2 == 0:
        raise ValueError("Total can't be zero")
    return (num2 / num1)* 100

def fact(num1):
    return math.factorial(num1)

def sin(num1):
    return round(math.sin(math.radians(num1)), 4)

def cos(num1):
    return round(math.cos(math.radians(num1)), 4)

def tan(num1):
    return round(math.tan(math.radians(num1)), 4)

def arcsin(num1):
    if not -1 <= num1 <= 1:
        raise ValueError("Inverse sine is defined for values from -1 to 1.")
    return round(math.degrees(math.asin(num1)), 2)

def arccos(num1):
    if not -1 <= num1 <= 1:
        raise ValueError("Inverse cosine is defined for values from -1 to 1.")
    return round(math.degrees(math.acos(num1)), 2)

def arctan(num1):
    return round(math.degrees(math.atan(num1)), 2)

def log(num1,num2):
    return round(math.log(num1,num2), 4)

def red_degree(num1):
    return round(math.degrees(num1), 3)

def degree_red(num1):
    return round(math.radians(num1), 3)


def calculator():
    while True:
        print("================================")
        print("           CALCULATOR")
        print("================================\n"
              "Please select the operator: \n"
              "For Addition         : Press '1' \n"
              "For Subtraction      : Press '2'\n"
              "For Multiplication   : Press '3'\n"
              "For Division         : Press '4'\n"
              "For Average          : Press '5'\n"
              "For Root             : Press '6'\n"
              "For Square           : Press '7'\n"
              "For Cube             : Press '8'\n"
              "For Square root      : Press '9'\n"
              "For Cube root        : Press '10'\n"
              "For Percentage       : Press '11'\n"
              "For Factorial        : Press '12'\n"
              "For sin\u03B8             : Press '13'\n"
              "For cos\u03B8             : Press '14'\n"
              "For tan\u03b8             : Press '15'\n"
              "For Inverse sin      : Press '16'\n"
              "For Inverse cos      : Press '17'\n"
              "For Inverse tan      : Press '18'\n"
              "For log              : Press '19'\n"
              "For Radian to Degree : Press '20'\n"
              "For Degree to Radian : Press '21'\n"
              "To exit              : Press '0'\n")

        select = int(input("Select an operator (0 to exit): "))
        if select == 0:
            print("Goodbye!")
            break

        if select in (1, 2, 3, 4, 5, 6):
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            if select == 1:
                print(number1, "+", number2, "= ", add(number1, number2))
            elif select == 2:
                print(number1, "-", number2, "= ", sub(number1, number2))
            elif select == 3:
                print(number1, "*", number2, "= ", multiply(number1, number2))
            elif select == 4:
                print(number1, "/", number2, "= ", divide(number1, number2))
            elif select == 5:
                print("(", number1, "+", number2, ")/2 = ",
                      avg(number1, number2))
            else:
                print(number1, "√", number2, "=", root(number1, number2))

        elif select in (7, 8, 9, 10):
            number3 = float(input("Enter the number: "))

            if select == 7:
                print(number3, " * ", number3, "= ", squr(number3))
            elif select == 8:
                print(number3, " * ", number3, " * ", number3, "= ",
                      cube(number3))
            elif select == 9:
                print("√", number3, "= ", square_root(number3))
            else:
                print("∛", number3, "= ", cube_root(number3))

        elif select == 11:
            number4 = float(input("Enter total number: "))
            number5 = float(input("Enter other number: "))
            print("(", number5, "/", number4, ") * 100 = ",
                  percent(number4, number5))

        elif select == 12:
            number6 = int(input("Enter the number: "))
            print(fact(number6))

        elif select in (13, 14, 15):
            number7 = float(input("Enter the value of θ: "))

            if select == 13:
                print(f"sin({number7}) = ", sin(number7))
            elif select == 14:
                print(f"cos({number7}) = ", cos(number7))
            else:
                print(f"tan({number7}) = ", tan(number7))

        elif select in (16, 17, 18):
            number8 = float(input("Enter the value: "))

            if select == 16:
                print(f"sin\u207B\u00B9({number8}) = ", arcsin(number8))
            elif select == 17:
                print(f"cos\u207B\u00B9({number8}) = ", arccos(number8))
            else:
                print(f"tan\u207B\u00B9({number8}) = ", arctan(number8))

        elif select == 19:
            number9 = int(input("Base of log:"))
            number10 = int(input("log of :"))
            print(f"log base {number9} of {number10} = ", log(number10,number9))

        elif select == 20:
            number10 = float(input("Enter the value of Radians: "))
            print(f"{number10} radian = ", red_degree(number10))

        elif select == 21:
                    number11 = float(input("Enter the value of Degrees: "))
                    print(f"{number11} radian = ", degree_red(number11))

        else:
            print("Invalid operator.")


if __name__ == "__main__":
    calculator()
