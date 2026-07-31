
num_str = "250"
print("Original string:", num_str, type(num_str))
# Convert to integer
num_int = int(num_str)
result = num_int + 50
print("After conversion and adding 50:", result)
print("New Type:", type(num_int))

age = 22 # Integer 
height = 5.8 # Float
name = "Abdur Rahman" # String
is_student = True # Boolean
print("Value:", age, "| Type:", type(age))
print("Value:", height, "| Type:", type(height))
print("Value:", name, "| Type:", type(name))
print("Value:", is_student, "| Type:", type(is_student))


a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Normal Division (a / b):", a / b)
print("Modulus / Remainder (a % b):", a % b)
print("Floor Division (a // b):", a // b)
print("Exponentiation / Power (a ** b):", a ** b)



num = 10
print("Initial value:", num)
num += 5 # Same as: num = num + 5
print("After num += 5:", num)
num -= 3 # Same as: num = num - 3
print("After num -= 3:", num)
num *= 2 # Same as: num = num * 2
print("After num *= 2:", num)
num /= 4 # Same as: num = num / 4
print("After num /= 4:", num)



x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))
print("x is equal to y (x == y):", x == y)
print("x is not equal to y (x != y):", x != y)
print("x is greater than y (x > y):", x > y)
print("x is less than y (x < y):", x < y)
print("x is greater than or equal to y (x >= y):", x >= y)
print("x is less than or equal to y (x <= y):", x <= y)


age = int(input("Enter your age: "))
has_id = input("Do you have ID card? (yes/no): ") == "yes"
# AND operator: Both conditions must be True
can_enter = (age >= 18) and has_id
print("Can enter restricted area (age >= 18 AND has ID):", can_enter)
# OR operator: At least one condition must be True
discount = (age < 12) or (age > 60)
print("Eligible for special discount (age < 12 OR age > 60):", discount)
# NOT operator: Reverses the boolean result
print("Is NOT eligible for discount:", not discount)


# Demonstrating Identity Operators (is, is not )
list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1 # Pointing to the same object in memory
print("list1 == list2 (Same values?):", list1 == list2)
print("list1 is list2 (Same memory object?):", list1 is list2)
print("list1 is list3 (Same memory object?):", list1 is list3)
print("Memory ID of list1:", id(list1))
print("Memory ID of list2:", id(list2))
print("Memory ID of list3:", id(list3))



fruits = ["apple", "banana", "mango", "orange"]
text = "Python Programming Practice"
print("Is 'mango' in fruits list?:", "mango" in fruits)
print("Is 'grape' in fruits list?:", "grape" in fruits)
print("Is 'Program' inside text?:", "Program" in text)
print("Is 'Java' NOT in text?:", "Java" not in text)


print("Bitwise AND (a & b):", a & b) # 1010 & 0100 = 0000 (0)
print("Bitwise OR (a | b):", a | b) # 1010 | 0100 = 1110 (14)
print("Bitwise XOR (a ^ b):", a ^ b) # 1010 ^ 0100 = 1110 (14) 40 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
print("Bitwise NOT (~a):", ~a) # -(10+1) = -11
print("Left Shift (a << 1):", a << 1) # Shifts bits left by 1 (Doubles: 20)
print("Right Shift (a >> 1):", a >> 1) # Shifts bits right by 1 (Halves: 5)


base = float(input("Enter base number: "))
exponent = float(input("Enter exponent / power: "))
result = base ** exponent
print("Result is:", result) 


total_seconds = int(input("Enter total seconds: "))
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60
print(total_seconds, "seconds is equal to:", minutes, "minutes and", 
remaining_seconds, "seconds")




chocolates = int(input("Enter total chocolates: "))
children = int(input("Enter number of children: "))
per_child = chocolates // children
remaining = chocolates % children
print("Each child gets:", per_child, "chocolates")
print("Chocolates left:", remaining)



length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print("The area of rectangle is:", area)




length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
print("The perimeter of rectangle is:", perimeter)



side = float(input("Enter side length of square: "))
area = side ** 2
print("The area of square is:", area)



import math
radius = float(input("Enter radius of circle: "))
area = math.pi * (radius ** 2)
print("The area of circle is:", round(area, 2))



import math
radius = float(input("Enter radius of circle: "))
circumference = 2 * math.pi * radius
print("The circumference of circle is:", round(circumference, 2))



base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = 0.5 * base * height
print("The area of triangle is:", area)



base = float(input("Enter base: "))
perpendicular = float(input("Enter perpendicular height: "))
area = (base * perpendicular) / 2
print("The area of right-angled triangle is:", area)




import math
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))
volume = math.pi * (radius ** 2) * height
print("The volume of cylinder is:", round(volume, 2))



side = float(input("Enter side length of cube: "))
volume = side ** 3
print("The volume of cube is:", volume)


fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = ((fahrenheit - 32) * 5) / 9
print("Temperature in Celsius is:", round(celsius, 2))