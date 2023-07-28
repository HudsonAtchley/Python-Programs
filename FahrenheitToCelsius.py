def convert(x):
    fahr = float(x)
    celsius = (fahr-32)*5/9
    print(celsius,"degrees Celsius")
    
fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
convert(fahrenheit)