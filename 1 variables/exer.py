
# 1. Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see

# break=5
# print(break) # keywords cannot be used as var names


# 2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

dob=[24,3,2005]
currYear=2024

print("my age is: ",(currYear-dob[2]))

# 3. print your full name using 3 diff variables 

def printName(firstName,MiddleName,LastName):
    print(firstName+" "+MiddleName+" "+LastName)

printName("om","pramod","shelke")


# 4. Answer which of these are invalid variable names: "__nation, 1record, record1, record_one, record-one, record^one, continue"

# 1record,record-one,record^one,continue are invalid