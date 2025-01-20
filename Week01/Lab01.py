#Week 01
#Full Name: Parvkumar

# 1. Defining Variables
array = [1, 4, 7, 9]
print("Array:", array)

# 2. Order of Operations

a = 1
b = 2
c = 3
d = 4

e1 = (a * c) - (b / d)
print("Fully-bracketed result of e1:", e1)


e2 = (((a - (b ** c)) // d) + (a % c))
print("Fully-bracketed result of e2:", e2)

# 3. Formatting: 
temperature = 32.6
print("The temperature of today is: {:.3f} degrees Celsius".format(temperature))

# 4. Common Functions: User input and operations
userAge = int(input("Enter your age: "))
userAge += 22
print(f"Now showing the shop items filtered by age: {userAge}")
