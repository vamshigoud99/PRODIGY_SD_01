def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f- 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return k * 9/5 - 459.67

def temperatureconv():
    print("Temperature Conversion Program...\n")
   
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        k = celsius_to_kelvin(c)
        print("Temperature in Fahrenheit:", f)
        print("Temperature in Kelvin:", k)
    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        k = fahrenheit_to_kelvin(f)
        print("Temperature in Celsius:", c)
        print("Temperature in Kelvin:", k)
    elif choice == 3:
        k = float(input("Enter temperature in Kelvin: "))
        c = kelvin_to_celsius(k)
        f = kelvin_to_fahrenheit(k)
        print("Temperature in Celsius:", c)
        print("Temperature in Fahrenheit:", f)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

temperatureconv()