# Storing and fetching product prices
price_table = {
 "Laptop": 65000,
 "Keyboard": 1200,
 "Mouse": 450,
 "Monitor": 14500
}
product = input("Enter product name (Laptop/Keyboard/Mouse/Monitor): ")
if product in price_table:
 print(f"Price of {product} is: {price_table[product]} BDT")
else:
 print("Product out of stock or unavailable.")
 
 
 
 
 
 
 
 # Character frequency calculation using get()
text = input("Enter a word: ")
char_freq = {}
for char in text:
 char_freq[char] = char_freq.get(char, 0) + 1
print("Character Frequencies:")
for char, count in char_freq.items():
 print(f"'{char}' occurred {count} times")
 
 
 
 
 
 
 sentence = input("Enter a sentence: ").lower()
words = sentence.split()
word_freq = {}
for word in words:
 word_freq[word] = word_freq.get(word, 0) + 1
print("Word Frequencies:")
for word, count in word_freq.items():
 print(f"{word} : {count}") 
 
 
 
 
 
 
 
 capitals = {
 "Bangladesh": "Dhaka",
 "India": "New Delhi",
 "Japan": "Tokyo",
 "UK": "London"
}
print("Country and Capital List:")
for country, capital in capitals.items():
 print(f"The capital of {country} is {capital}")
 
 
 
 
 
 
 
 def greet():
 print("Welcome to Python Programming!")
 print("Functions make code reusable.")
# Calling the function
greet()







def welcome(user_name):
 print(f"Hello {user_name}, welcome to our Python course!")
# Calling with arguments
welcome("Abdur Rahman")
welcome("Sadiya")






def get_square(number):
 return number ** 2
# Storing returned value in a variable
res = get_square(7)
print("The square of 7 is:", res)






def add_numbers(num1, num2): 219 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
 sum_res = num1 + num2
 return sum_res
ans = add_numbers(25, 40)
print("Sum is:", ans)







# Function to subtract two numbers
def subtract(a, b):
 return a - b
diff = subtract(80, 35)
print("Difference is:", diff)






def multiply(x, y):
 return x * y
product = multiply(12, 5)
print("Product is:", product)






# Function to divide two numbers with Zero check
def divide(a, b):
 if b == 0:
 return "Error! Division by zero is not allowed."
 return a / b
print("Division Result:", divide(50, 4))
print("Zero Division Test:", divide(20, 0))










# Function to find factorial of a number
def get_factorial(n):
 if n < 0:
 return "Invalid input"
 fact = 1
 for i in range(1, n + 1):
 fact *= i
 return fact
print("Factorial of 6 is:", get_factorial(6))







def is_prime(n):
 if n <= 1:
 return False
 for i in range(2, int(n ** 0.5) + 1): 225 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
 if n % i == 0:
 return False
 return True
num = 37
if is_prime(num):
 print(num, "is a Prime Number")
else:
 print(num, "is NOT a Prime Number")
 
 
 
 
 
 
 
 def generate_fibonacci(n):
 if n <= 0:
 return []
 elif n == 1:
 return [0]
 
 fib_series = [0, 1]
 for i in range(2, n):
 next_val = fib_series[-1] + fib_series[-2]
 fib_series.append(next_val)
 return fib_series
print("First 10 Fibonacci numbers:", generate_fibonacci(10))






# Function to find maximum among arbitrary numbers using *args
def find_max(*numbers):
 if not numbers:
 return None
 max_val = numbers[0]
 for num in numbers:
 if num > max_val:
 max_val = num
 return max_val
print("Max among (10, 50, 25):", find_max(10, 50, 25))
print("Max among (5, 99, 12, 105, 88):", find_max(5, 99, 12, 105, 88))







def sum_list(my_list):
 total = 0
 for num in my_list:
 total += num
 return total
sample_list = [10, 20, 30, 40, 50]
print("Sum of list elements:", sum_list(sample_list)









def is_palindrome(text):
 clean_text = text.lower()
 return clean_text == clean_text[::-1]
word = "Madam"
if is_palindrome(word):
 print(word, "is a Palindrome")
else:
 print(word, "is NOT a Palindrome")
 
 
 
 
 with open("my_file.txt", "w") as file:
 file.write("Welcome to Python File Handling!\n")
 file.write("This file was created programmatically.")
print("File 'my_file.txt' created successfully!")






try:
 with open("my_file.txt", "r") as file:
 content = file.read()
 print("--- File Content ---")
 print(content)
except FileNotFoundError:
 print("Error: The specified file does not exist!")
 
 
 
 
 
 
 with open("my_file.txt", "w") as file:
 file.write("This is completely new text.\n")
 file.write("Previous contents have been overwritten.")
print("New data written successfully.")






with open("my_file.txt", "a") as file:
 file.write("\nThis line is appended at the end.")
 file.write("\nWe preserved the old text!")
print("Data appended successfully.")






Storing multiple student records in a file
students = [
 {"roll": 1, "name": "Rahim", "gpa": 3.80},
 {"roll": 2, "name": "Karim", "gpa": 3.90},
 {"roll": 3, "name": "Sadiya", "gpa": 4.00}
]
with open("students.txt", "w") as file:
 file.write("Roll | Name | GPA\n")
 file.write("---------------------\n")
 for s in students:
 file.write(f"{s['roll']} | {s['name']:<6} | {s['gpa']}\n")
print("Student records saved to 'students.txt'.")





with open("my_file.txt", "w") as f:
 f.write("Python is a powerful and easy programming language.")
with open("my_file.txt", "r") as file:
 content = file.read()
 words = content.split()
 print("Total words in file:", len(words))
 
 
 
 
 
 with open("sample_lines.txt", "w") as f:
 f.write("Line 1: Hello\nLine 2: Python\nLine 3: World")
with open("sample_lines.txt", "r") as file:
 lines = file.readlines()
 print("Total lines in file:", len(lines))
 
 
 
 
 
 with open("my_file.txt", "r") as file:
 content = file.read()
 print("Total characters in file:", len(content))
 
 
 
 
 
 with open("my_file.txt", "r") as file:
 text = file.read().lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
print("Total vowels in file:", vowel_count)






with open("my_file.txt", "r") as src:
 data = src.read()
with open("copy_file.txt", "w") as dest:
 dest.write(data)
print("File copied successfully to 'copy_file.txt'.")






with open("f1.txt", "w") as f: f.write("Part 1: Hello from file 1.\n")
with open("f2.txt", "w") as f: f.write("Part 2: Welcome from file 2.\n")
# Reading both
with open("f1.txt", "r") as f1, open("f2.txt", "r") as f2:
 data1 = f1.read()
 data2 = f2.read()
# Merging
with open("merged.txt", "w") as m:
 m.write(data1 + data2)
print("Files merged successfully into 'merged.txt'.")






#Saving and Reading Student Results from File
# Step 1: Saving results
with open("results.txt", "w") as file:
 file.write("101,Abdur Rahman,A+\n")
 file.write("102,Sadiya Islam,A\n")
 file.write("103,Tanvir Ahmed,A+\n")
# Step 2: Reading and formatting results
print("--- Result Sheet ---")
print("Roll | Name | Grade")
print("----------------------------")
with open("results.txt", "r") as file:
 for line in file:
 roll, name, grade = line.strip().split(",")
 print(f"{roll:<4} | {name:<13} | {grade}")
 
 
 
 
 
 
 # Searching a word inside a file line by line
with open("story.txt", "w") as f:
 f.write("Python is very popular.\nMany developers love Python.\nJava is also 
widely used.\nPython makes automation easy.")
search_word = "Python"
found_lines = []
with open("story.txt", "r") as file:
 for line_num, line in enumerate(file, 1):
 if search_word.lower() in line.lower():
 found_lines.append((line_num, line.strip()))
print(f"Search results for '{search_word}':")
if found_lines:
 for num, text in found_lines:
 print(f"Line {num}: {text}")
else:
 print("Word not found in the file.")
 
 
 
 
 