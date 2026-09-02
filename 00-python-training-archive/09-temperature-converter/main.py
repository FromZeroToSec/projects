def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
    return fahrenheit


def main_menu():
    """Display the main menu."""
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    """Display the main menu and handle user input."""
    while True:
        try:
            choice = main_menu()
            if choice == "0":
                break
            elif choice == "1":
                temperature = float(input("Enter your celsius number: "))
                result = celsius_to_fahrenheit(temperature)
                print(f"Result: {result:.2f}")
            elif choice == "2":
                temperature = float(input("Enter your fahrenheit number: "))
                result = fahrenheit_to_celsius(temperature)
                print(f"Result: {result:.2f}")
            elif choice == "3":
                temperature = float(input("Enter your celsius number: "))
                result = celsius_to_kelvin(temperature)
                print(f"Result: {result:.2f}")
            elif choice == "4":
                temperature = float(input("Enter your kelvin number: "))
                result = kelvin_to_celsius(temperature)
                print(f"Result: {result:.2f}")
            elif choice == "5":
                temperature = float(input("Enter your fahrenheit number: "))
                result = fahrenheit_to_kelvin(temperature)
                print(f"Result: {result:.2f}")
            elif choice == "6":
                temperature = float(input("Enter your kelvin number: "))
                result = kelvin_to_fahrenheit(temperature)
                print(f"Result: {result:.2f}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()