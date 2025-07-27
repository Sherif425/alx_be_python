FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    """Main function to handle temperature conversions."""
    print("Temperature Conversion Tool")
    
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
        
        celsius_input = float(input("Enter temperature in Celsius: "))
        fahrenheit_result = convert_to_fahrenheit(celsius_input)
        print(f"{celsius_input}°C is {fahrenheit_result:.2f}°F")
        
    except ValueError as e:
        print(f"Error: {e}. Invalid temperature. Please enter a numeric value.")
