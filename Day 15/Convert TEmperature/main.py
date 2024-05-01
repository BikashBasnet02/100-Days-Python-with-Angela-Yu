def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: Fahrenheit = (Celsius * 9/5) + 32
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: Celsius = (Fahrenheit - 32) * 5/9
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    Formula: Kelvin = Celsius + 273.15
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    Formula: Celsius = Kelvin - 273.15
    """
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert temperature from Fahrenheit to Kelvin.
    Formula: Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
    """
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """
    Convert temperature from Kelvin to Fahrenheit.
    Formula: Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
    """
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Welcome to Temperature Unit Converter!")

    choice = input("Choose conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Celsius to Kelvin\n4. Kelvin to Celsius\n5. Fahrenheit to Kelvin\n6. Kelvin to Fahrenheit\nEnter your choice (1-6): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Kelvin:", celsius_to_kelvin(celsius))
    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print("Temperature in Celsius:", kelvin_to_celsius(kelvin))
    elif choice == '5':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Kelvin:", fahrenheit_to_kelvin(fahrenheit))
    elif choice == '6':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print("Temperature in Fahrenheit:", kelvin_to_fahrenheit(kelvin))
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
