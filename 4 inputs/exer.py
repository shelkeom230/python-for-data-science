# Write a program that can find area of a triangle. It should take base and height as an input from user and using that it should print an area of a triangle

base=float(input("enter base of triangle: "))
height=float(input("enter height of triangle: "))

print("area: ",(1/2)*base*height)


# Write a program that takes file name with extension as an input and prints just the file name without extension (you can assume that file extensions are always 3 character long)

filename=input("enter filename: ")

modified=filename.split('.')
print(modified[0])