def inch_to_cm(num):
    return round(num * 2.54, 4)


def cm_to_inch(num):
    return round(num / 2.54, 4)


def ft_to_m(num):
    return round(num * 0.3048, 4)


def m_to_ft(num):
    return round(num / 0.3048, 4)


def yd_to_m(num):
    return round(num * 0.9144, 4)


def m_to_yd(num):
    return round(num / 0.9144, 4)


def mile_to_km(num):
    return round(num * 1.609344, 4)


def km_to_mile(num):
    return round(num / 1.609344, 4)


def converter():
    while True:
        print("================================")
        print("         UNIT  CONVERSION")
        print("================================")
        print("For Inch to cm      = Press '1'")
        print("For cm to in        = Press '2'")
        print("For ft to m         = Press '3'")
        print("For m to ft         = Press '4'")
        print("For yd to m         = Press '5'")
        print("For m to yd         = Press '6'")
        print("For mile to km      = Press '7'")
        print("For km to mile      = Press '8'")
        print("For Exit            = Press '9'")

        choice = int(input("Enter operator: "))

        if choice == 1:
            value = float(input("Enter value in inches: "))
            print(f"{value} in = {inch_to_cm(value)} cm")
        elif choice == 2:
            value = float(input("Enter value in cm: "))
            print(f"{value} cm = {cm_to_inch(value)} in")
        elif choice == 3:
            value = float(input("Enter value in feet: "))
            print(f"{value} ft = {ft_to_m(value)} m")
        elif choice == 4:
            value = float(input("Enter value in meters: "))
            print(f"{value} m = {m_to_ft(value)} ft")
        elif choice == 5:
            value = float(input("Enter value in yards: "))
            print(f"{value} yd = {yd_to_m(value)} m")
        elif choice == 6:
            value = float(input("Enter value in meters: "))
            print(f"{value} m = {m_to_yd(value)} yd")
        elif choice == 7:
            value = float(input("Enter value in miles: "))
            print(f"{value} mile = {mile_to_km(value)} km")
        elif choice == 8:
            value = float(input("Enter value in km: "))
            print(f"{value} km = {km_to_mile(value)} mile")
        elif choice == 9:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    converter()
