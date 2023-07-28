def convert(x):
    celsius = float(x)
    kelvin = (celsius + 273.15)
    print(kelvin,"K")
    
cel = int(input("Enter the temperature in Celsius: "))
convert(cel)