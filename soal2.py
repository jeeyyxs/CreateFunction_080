#Use the lambda function to create a function that calculates the area of a circle! Input is the length from the center of the circle to the border (jari-jari lingkaran).

r = float(input("Masukkan jari-jari lingkaran: "))
print (f"Luas lingkaran dengan jari-jari {r} adalah: {(lambda r: 3.14 * r ** 2)(r)}")