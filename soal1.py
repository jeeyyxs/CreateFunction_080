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
#print("======== KONVERSI SUHU ========")
#input_suhu = float(input("Masukkan nilai suhu: "))
#unit = input("Masukkan satuan suhu (C/F): ").upper()
#konversi = convert_temperature(input_suhu, unit)
#if unit.upper() == 'C':
#   print(f"{input_suhu}°C = {konversi:.2f}°F")
#elif unit.upper() == 'F':
#   print(f"{input_suhu}°F = {konversi:.2f}°C")
#else:
#print("Satuan tidak dikenal."  )
