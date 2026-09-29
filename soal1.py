#1. Create a function that converts temperature from Celsius to Fahrenheit and vice versa. The function accepts two parameters, namely the temperature value and the temperature unit ('C' for Celsius, 'F' for Fahrenheit).
def convert_temperature(value, unit):
    if unit == 'C':
        #Convert Celsius to Fahrenheit
        return (value * 9/5) + 32
    elif unit == 'F':
        #Convert Fahrenheit to Celsius
        return (value - 32) * 5/9
    else:
        return "Unit tidak valid! unit harus 'C' atau 'F'"

print(convert_temperature(25, 'C'))  
print(convert_temperature(77, 'F'))  
print(convert_temperature(100, 'X'))  

#def convert_temperature(value, unit):
#    if unit == 'C':
#        return (value * 9/5) + 32
#    elif unit == 'F':
#        return (value - 32) * 5/9
#    else:
#        return "Unit tidak valid! unit harus 'C' atau 'F'"