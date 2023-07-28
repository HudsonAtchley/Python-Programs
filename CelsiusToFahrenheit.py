def convert(x):
    celsius = float(x)
    fahrenheit = (celsius*9/5)+32
    print(fahrenheit,"degrees fahrenheit")
    
cel = int(input("Enter the temperature in Celsius: "))
convert(cel)