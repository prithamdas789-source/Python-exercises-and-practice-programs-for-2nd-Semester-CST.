N = int(input("Enter height of pyramid: "))
for i in range(1, N + 1):
 print(" " * (N - i) + "* " * i)
 
 
 
 N = int(input("Enter height: "))
for i in range(N, 0, -1):
 print(" " * (N - i) + "* " * i)
 
 
 
 N = int(input("Enter height: "))
for i in range(1, N + 1):
 for j in range(1, i + 1):
 print(j, end=" ")
 print()





N = int(input("Enter height: "))
num = 1
for i in range(1, N + 1):
 for j in range(1, i + 1):
 print(num, end=" ")
 num += 1
 print()




#Taking a string input from user
user_text = input("Enter a sentence or text: ")
print("You entered:", user_text)




text = input("Enter a string: ")
count = 0
for char in text:
 count += 1
print("Length of string is:", count)





text = input("Enter a string: ")
rev_text = ""
for char in text:
 rev_text = char + rev_text
print("Reversed string is:", rev_text)



text = input("Enter a word: ").lower()
rev_text = text[::-1]
if text == rev_text:
 print("It is a Palindrome")
else:
 print("It is NOT a Palindrome")
 
 
 
 text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in text:
 if char in vowels:
     count += 1
print("Total vowels:", count)



text = input("Enter a string: ").lower()
vowels = "aeiou"
consonant_count = 0
for char in text:
 if char.isalpha() and char not in vowels:
 consonant_count += 1
print("Total consonants:", consonant_count)




text = input("Enter a string with numbers: ")
digit_count = 0
for char in text:
 if char.isdigit():
 digit_count += 1
print("Total digits in the string:", digit_count)





text = input("Enter a sentence: ")
space_count = 0
for char in text:
 if char == ' ':
 space_count += 1
print("Total white spaces:", space_count)







text = input("Enter a sentence: ")
words = text.split()
word_count = len(words)
print("Total words:", word_count)





text = input("Enter a string: ")
freq = {}
for char in text:
 if char in freq: 155 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
 freq[char] += 1
 else:
 freq[char] = 1
print("Character Frequencies:")
for char, count in freq.items():
 print(f"'{char}' : {count}")
 
 
 
 
 text = input("Enter text: ")
upper_text = text.upper()
print("Uppercase Text:", upper_text)




text = input("Enter text: ")
lower_text = text.lower()
print("Lowercase Text:", lower_text)






text = "I like Java programming"
print("Original text:", text)
new_text = text.replace("Java", "Python")
print("Updated text:", new_text)



text = "Python Programming"
first_word = text[0:6] # From index 0 to 5
second_word = text[7:] # From index 7 to end
last_chars = text[-4:] # Last 4 characters
print("Original Text:", text)
print("First Word [0:6]:", first_word)
print("Second Word [7:]:", second_word)
print("Last 4 Chars [-4:]:", last_chars)






my_list = [10, 25.5, "Python", True, "Abdur Rahman"]
print("The list is:", my_list)
print("Data type:", type(my_list))





fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Fruit List:")
for item in fruits:
 print("-", item)





numbers = [15, 25, 35, 45, 55]
total = 0
for num in numbers:
 total += num
print("Sum of list elements:", total)




numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
count = len(numbers)
average = total / count
print("Average is:", average)





numbers = [45, 89, 12, 96, 54, 23]
max_val = numbers[0]
for num in numbers:
 if num > max_val:
 max_val = num
 print("Maximum number is:", max_val)
 
 
 
 
 
 numbers = [45, 89, 12, 96, 54, 23]
min_val = numbers[0]
for num in numbers:
 if num < min_val:
 min_val = num
print("Minimum number is:", min_val)





numbers = [12, 15, 18, 21, 24, 27, 30]
evens = []
for num in numbers:
 if num % 2 == 0:
 evens.append(num)
print("Original list:", numbers)
print("Even numbers:", evens)






numbers = [12, 15, 18, 21, 24, 27, 30]
odds = []
for num in numbers:
 if num % 2 != 0:
 odds.append(num)
print("Odd numbers:", odds)




numbers = [-15, 20, -8, 35, -2, 50, 0]
positives = []
for num in numbers:
 if num > 0:
 positives.append(num)
print("Positive numbers:", positives)






numbers = [-15, 20, -8, 35, -2, 50, 0]
negatives = []
for num in numbers:
 if num < 0:
 negatives.append(num)
print("Negative numbers:", negatives)






numbers = [54, 23, 89, 12, 67, 34]
print("Original list:", numbers)
numbers.sort()
print("Sorted list (Ascending):", numbers)






numbers = [54, 23, 89, 12, 67, 34]
numbers.sort(reverse=True)
print("Sorted list (Descending):", numbers)




numbers = [10, 25, 10, 30, 25, 40, 50, 30]
unique_list = []
for num in numbers:
 if num not in unique_list:
 unique_list.append(num)
print("Original list:", numbers)
print("Without duplicates:", unique_list)





numbers = [15, 28, 35, 42, 59, 64]
target = int(input("Enter number to search: "))
found = False
for i in range(len(numbers)):
 if numbers[i] == target:
 print(f"Number {target} found at index {i}")
 found = True
 break
if not found:
 print(f"Number {target} is NOT in the list")
 
 
 
 
 
 
 
 numbers = [10, 20, 10, 30, 10, 40, 20]
target = int(input("Enter number to count: "))
count = 0
for num in numbers:
 if num == target:
 count += 1
print(f"The number {target} appears {count} times")






numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
numbers.reverse()
print("Reversed list:", numbers)





my_tuple = (10, 20, 30, 40, 50)
print("The Tuple is:", my_tuple)
print("Data type:", type(my_tuple))




empty_tuple = ()
print("Empty tuple:", empty_tuple)
print("Length:", len(empty_tuple))
print("Type:", type(empty_tuple))







mixed_tuple = (101, 99.5, "Abdur Rahman", True)
print("Mixed Tuple:", mixed_tuple)
for item in mixed_tuple:
 print(f"Value: {item} | Type: {type(item)}")
 
 
 
 
 
 nested_tuple = ((10, 20), (30, 40), (50, 60))
print("Nested Tuple:", nested_tuple)
print("First inner tuple:", nested_tuple[0])
print("Element 40 inside second inner tuple:", nested_tuple[1][1])





colors = ("Red", "Green", "Blue", "Yellow")
print("Color Tuple Elements:")
for color in colors:
 print("->", color)






numbers = (100, 200, 300, 400, 500)
print("First element (index 0):", numbers[0])
print("Third element (index 2):", numbers[2])
print("Last element (index -1):", numbers[-1])






data = (10, 20, 30, 40, 50, 60, 70) 
sub_tuple = data[1:5] # From index 1 to 4
print("Original Tuple:", data)
print("Sliced Tuple [1:5]:", sub_tuple)




person = ("Abdur Rahman", 22, "Dhaka")
# Unpacking into separate variables
name, age, city = person
print("Name:", name)
print("Age:", age)
print("City:", city)





#Swapping values using Tuple Unpacking
x = 10
y = 20
print("Before Swap: x =", x, ", y =", y)
# Swapping
x, y = y, x
print("After Swap: x =", x, ", y =", y)





#Creating a simple Set
my_set = {10, 20, 30, 40, 50}
print("The Set is:", my_set)
print("Data type:", type(my_set))






numbers_list = [10, 20, 10, 30, 20, 40, 50, 30]
print("Original List with duplicates:", numbers_list)
unique_set = set(numbers_list)
print("After converting to Set:", unique_set)





set1 = {10, 20, 30}
set2 = {30, 40, 50}
union_set = set1 | set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Union (set1 | set2):", union_set)





# Finding Intersection of two Sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
common_set = set1 & set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection (set1 & set2):", common_set)





#Finding Difference between two Sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
diff_set = set1 - set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Difference (set1 - set2):", diff_set)






set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
sym_diff = set1 ^ set2
print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference (set1 ^ set2):", sym_diff)




fruits = {"Apple", "Banana", "Mango", "Orange"}
target = input("Enter fruit name to check: ")
if target in fruits:
 print(target, "is available in the set")
else:
 print(target, "is NOT available in the set")
 
 
 
 
 
 
 my_set = {10, 20, 30, 40, 50}
count = len(my_set)
print("Set elements:", my_set)
print("Total elements in the set:", count)



numbers = {45, 89, 12, 96, 54, 23}
max_val = max(numbers)
print("Set elements:", numbers)
print("Maximum value is:", max_val)




numbers = {45, 89, 12, 96, 54, 23}
min_val = min(numbers)
print("Set elements:", numbers)
print("Minimum value is:", min_val)






student = {
 "name": "Abdur Rahman",
 "age": 22,
 "district": "Dhaka"
}
print("Student Dictionary:", student)
print("Data type:", type(student))





#Adding a new item to Dictionary
student = {"name": "Abdur Rahman", "age": 22}
print("Before adding:", student)
# Adding new key-value pair
student["department"] = "Computer Science"
student["cgpa"] = 3.85
print("After adding:", student)








#Updating an existing item in Dictionary
student = {"name": "Abdur Rahman", "age": 22, "district": "Comilla"}
print("Original Dictionary:", student)
# Updating age and district
student["age"] = 23
student["district"] = "Dhaka"
print("Updated Dictionary:", student)







student = {"name": "Abdur Rahman", "age": 22, "district": "Dhaka", "grade": "A"}
print("Before deletion:", student)
# Using del keyword
del student["grade"]
# Using pop() method
removed_val = student.pop("age")
print("After deleting 'grade' and 'age':", student)
print("Removed age value:", removed_val)






# Storing and displaying student info using dictionary
name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))
gpa = float(input("Enter GPA: "))
student_info = {
 "Name": name,
 "Roll": roll,
 "GPA": gpa
}
print("\n--- Student Bio-Data ---")
for key, val in student_info.items():
 print(f"{key} : {val}")
 
 
 
 
 
 
 results = {
 101: {"name": "Rahim", "gpa": 3.85},
 102: {"name": "Karim", "gpa": 3.60},
 103: {"name": "Sadiya", "gpa": 4.00}
}
search_roll = int(input("Enter Roll Number to check result (101-103): "))
if search_roll in results:
 info = results[search_roll]
 print(f"Name: {info['name']} | GPA: {info['gpa']}")
else:
 print("Result not found for this Roll Number!")
 
 
 
 
 
 