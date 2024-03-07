# 1. find area of triangle 
def findArea(base,height):
    print("area: ",(1/2)*base*height)

findArea(10.11,12.22)
findArea(10.26,20.572)

# 2. basic arithmatic

print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1**2)
print(15%2)
print(1+2/4)

# 3. Number data types (int, float, complex numbers)

foo=2.3e-3
foo1=10.1e-2
print(foo,foo1) # 0.0023
print(type(1)) # int
print(0x12) # 18
print(type(0x12)) # int
c1=2+3j
print(type(c1)) # complex
c2=3-4j
print(c1+c2) # 5-j

# 4. Internal representation of numbers
# (a) integers are stored in simple binary format
print(format(5,'b'))


print(6-5.7) # 4 bytes (or 32 bits), visual of binary presentation
# (b) floats use IEEE754 standard : https://en.wikipedia.org/wiki/IEEE_754
# 0.29999999 and not 0.3. why? Due to IEEE 754 standard
