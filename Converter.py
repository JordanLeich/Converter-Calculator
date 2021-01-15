# Made by Jordan Leich on 6/14/2020

import time
import restart
import colors


def starter():
    """
Begins the program and first bits of code
    """
    user_convert_choice1 = input('''Temperature Converter
Mass Converter
Select a converter:  ''')
    print()
    time.sleep(1)

    if user_convert_choice1.lower() == 't' or user_convert_choice1.lower() == 'temperature' or user_convert_choice1. \
            lower() == 'temperature converter':
        temp_converter()

    elif user_convert_choice1.lower() == 'm' or user_convert_choice1.lower() == 'mass' or user_convert_choice1.lower() \
            == 'mass converter':
        mass_converter()

    else:
        print(colors.red + 'Error found!\n' + colors.reset)
        time.sleep(2)
        restart.restart()


def temp_converter():
    """
Handles all temperature conversions here
    """
    user_choice = int(
        input("""Celsius to Fahrenheit (1)
Celsius to Kelvin (2)
Fahrenheit to Celsius (3)
Fahrenheit to Kelvin (4)
Kelvin to Celsius (5)
Kelvin to Fahrenheit (6)
Select a temperature conversion:    """))
    print()

    if user_choice == 1:
        user_celsius = float(input("Celsius: "))
        print()
        c_to_f = float(user_celsius * 1.8 + 32)
        print(colors.green, user_celsius, "in Celsius equals", c_to_f, "in Fahrenheit.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    elif user_choice == 2:
        user_celsius = float(input("Celsius: "))
        print()
        c_to_k = float(user_celsius + 273.15)
        print(colors.green, user_celsius, "in Celsius equals", c_to_k, "in Kelvin.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    elif user_choice == 3:
        user_fahrenheit = float(input("Fahrenheit: "))
        print()
        f_to_c = float((user_fahrenheit - 32) * 5 / 9)
        print(colors.green, user_fahrenheit, "in Fahrenheit equals", f_to_c, "in Celsius.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    elif user_choice == 4:
        user_fahrenheit = float(input("Fahrenheit: "))
        print()
        f_to_k = float((user_fahrenheit - 32) * 5 / 9 + 273.15)
        print(colors.green, user_fahrenheit, "in Fahrenheit equals", f_to_k, "in Kelvin.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    elif user_choice == 5:
        user_kelvin = float(input("Kelvin: "))
        print()
        k_to_c = float(user_kelvin - 273.15)
        print(colors.green, user_kelvin, "in Kelvin equals", k_to_c, "in Celsius.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    elif user_choice == 6:
        user_kelvin = float(input("Kelvin: "))
        print()
        k_to_f = float((user_kelvin - 273.15) * 1.8 + 32)
        print(colors.green, user_kelvin, "in Kelvin equals", k_to_f, "in Fahrenheit.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        temp_converter()


def mass_converter():
    """
Handles all mass conversions
    """
    user_choice2 = int(
        input("""Kilogram to All (1)
Select a mass conversion:    """))
    print()

    if user_choice2 == 1:
        user_kilo = float(input("Kilogram: "))
        print()
        kg_to_g = float(user_kilo * 1000)
        kg_to_p = float(user_kilo * 2.205)
        kg_to_o = float(user_kilo * 35.274)
        print(colors.green, user_kilo, "in Kilogram equals", kg_to_g, "in Grams.", colors.reset)
        print(colors.green, user_kilo, "in Kilogram equals", kg_to_p, "in Pounds.", colors.reset)
        print(colors.green, user_kilo, "in Kilogram equals", kg_to_o, "in Ounces.\n", colors.reset)
        time.sleep(1)
        restart.restart()

    elif user_choice2 == 2:
        print('test')

    else:
        print(colors.red + "Invalid input... Restarting input choice...\n" + colors.reset)
        time.sleep(2)
        mass_converter()


starter()
