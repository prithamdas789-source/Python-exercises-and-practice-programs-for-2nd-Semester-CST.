print ("Hello world")

print("My name is: pritham das")

print("House No: 12, Road No: 5")
print("Dhanmondi, Dhaka")
print("Bangladesh")

print("Name : pritham das")
print("Age : 17 Years")
print("District: Dhaka")
print("Country : Bangladesh")

print("Course:\tPython Programming")
print("Topic:\tEscape Characters")
print("Status:\t\"Completed\"")
print("Path:\tC:\\Users\\Python\\Notes")

print("Dhaka", "Chittagong", "Sylhet", sep=" -> ")

print("Hello", end=" ")
print("World!", end=" ")
print("Welcome to Python.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("The sum is:", total)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
difference = num1 - num2
print("The difference is:", difference)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
product = num1 * num2


num1 = float(input("Enter dividend: "))
num2 = float(input("Enter divisor: "))
quotient = num1 / num2
print("The quotient is:", quotient)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
remainder = num1 % num2
print("The remainder is:", remainder)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("The average is:", average)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("The average is:", average)



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: num1 =", num1, "num2 =", num2)

# Using temp variable
temp = num1
num1 = num2
num2 = temp
print("After swapping: num1 =", num1, "num2 =", num2)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swap: num1 =", num1, "num2 =", num2)

# Swapping without temp
num1, num2 = num2, num1
print("After swap: num1 =", num1, "num2 =", num2)



# Converting Integer to Float
integer_num = 25
print("Original value:", integer_num, "| Type:", type(integer_num))
# Type casting to float
float_num = float(integer_num)
print("Converted value:", float_num, "| Type:", type(float_num))



# Converting Float to Integer
float_num = 45.78
print("Original float:", float_num)
# Type casting to int
int_num = int(float_num)
print("Converted integer:", int_num)
print("New Type:", type(int_num))


