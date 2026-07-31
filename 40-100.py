celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit is:", round(fahrenheit, 2))



kilometers = float(input("Enter distance in kilometers: "))
meters = kilometers * 1000
print(kilometers, "km is equal to", meters, "meters")



meters = float(input("Enter distance in meters: "))
kilometers = meters / 1000
print(meters, "meters is equal to", kilometers, "km")



num = int(input("Enter a number: "))
if num % 2 == 0:
 print(num, "is an Even number")
else:
 print(num, "is an Odd number")
 
 
 
 num = float(input("Enter a number: "))
if num > 0:
 print("The number is Positive")
elif num < 0:
 print("The number is Negative")
else:
 print("The number is Zero")




num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
 print("Maximum number is:", num1)
elif num2 > num1:
 print("Maximum number is:", num2)
else:
 print("Both numbers are equal")
 
 
 
 
 num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 < num2:
 print("Minimum number is:", num1)
elif num2 < num1:
 print("Minimum number is:", num2)
else:
 print("Both numbers are equal")
 
 
 
 
 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
 print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
 print("Largest number is:", c)
 
 
 
 a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a <= b and a <= c:
 print("Smallest number is:", a)
elif b <= a and b <= c:
 print("Smallest number is:", b)
else:
 print("Smallest number is:", c)
 
 
 
 year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
 print(year, "is a Leap Year")
else:
 print(year, "is NOT a Leap Year")
 
 
 
 marks = float(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
 print("Invalid marks entered!")
elif marks >= 80:
 print("Grade: A+")
elif marks >= 70:
 print("Grade: A")
elif marks >= 60:
 print("Grade: A-")
elif marks >= 50:
 print("Grade: B")
elif marks >= 40:
 print("Grade: C")
elif marks >= 33:
 print("Grade: D")
else:
 print("Grade: F (Fail)")
 
 
 
 
 
 marks = float(input("Enter obtained marks: "))
passing_mark = 33
if marks >= passing_mark:
 print("Result: PASS")
else:
 print("Result: FAIL")
 
 
 
 
 
 age = int(input("Enter your age: "))
if age >= 18:
 print("You are eligible to vote.")
else:
 years_left = 18 - age
 print("You are NOT eligible to vote.")
 print("Please wait for", years_left, "more years.")
 
 
 
 
 
 char = input("Enter a single character: ")
if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
 print(char, "is an Alphabet")
else:
 print(char, "is NOT an Alphabet")
 
 
 
 char = input("Enter a single character: ")
if '0' <= char <= '9':
 print(char, "is a Digit")
else:
 print(char, "is NOT a Digit")
 
 
 
 
 char = input("Enter an alphabet character: ")
# Convert to lower case to handle both uppercase and lowercase
lower_char = char.lower()
if lower_char in ['a', 'e', 'i', 'o', 'u']:
 print(char, "is a Vowel")
elif lower_char.isalpha():
 print(char, "is a Consonant")
else:
 print("Invalid input! Please enter an alphabet.")
 
 
 
 char = input("Enter an alphabet character: ")
if 'A' <= char <= 'Z':
 print(char, "is an UPPERCASE character")
elif 'a' <= char <= 'z':
 print(char, "is a lowercase character")
else:
 print(char, "is not an alphabet character")
 
 
 
 
 a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if (a + b > c) and (b + c > a) and (a + c > b):
 print("Valid Triangle! A triangle CAN be formed.")
else:
 print("Invalid Triangle! A triangle CANNOT be formed.")
 
 
 
 
 for i in range(1, 11):
 print(i, end=" ")
 
 
 
 for num in range(1, 101):
 print(num, end=" ")
 
 
 
 
 N = int(input("Enter upper limit (N): "))
print("Numbers from 1 to", N, "are:")
for i in range(1, N + 1):
 print(i, end=" ")





 N = int(input("Enter starting number (N): "))
print("Countdown from", N, "to 1:")
for i in range(N, 0, -1):
 print(i, end=" ")
 
    
       
          
 total = 0
for i in range(1, 101):
 total += i
print("The sum of numbers from 1 to 100 is:", total)

   
      
N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
 total += i
print("The sum from 1 to", N, "is:", total)  

 
  
N = int(input("Enter N: "))
total = 0
for i in range(2, N + 1, 2):
 total += i
print("Sum of even numbers from 1 to", N, "is:", total) 
    
    
 
 N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1, 2):
 total += i
print("Sum of odd numbers from 1 to", N, "is:", total)



N = int(input("Enter N: "))
total = 0 93 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
for i in range(5, N + 1, 5):
 total += i
print("Sum of numbers divisible by 5 up to", N, "is:", total)




N = int(input("Enter N: "))
total = 0
for i in range(7, N + 1, 7):
 total += i
print("Sum of numbers divisible by 7 up to", N, "is:", total)




N = int(input("Enter N: "))
print("Numbers divisible by both 3 and 5 up to", N, "are:")
for i in range(1, N + 1):
 if i % 3 == 0 and i % 5 == 0:
 print(i, end=" ")
 
 
 
 
 num = int(input("Enter a positive integer: "))
count = 0
temp = abs(num) # Handling negative numbers
if temp == 0:
 count = 1
else:
 while temp > 0:
 temp = temp // 10
 count += 1
print("Total number of digits:", count)



num = int(input("Enter a number: "))
temp = abs(num)
sum_digits = 0
while temp > 0:
 digit = temp % 10
 sum_digits += digit
 temp = temp // 10
print("Sum of digits is:", sum_digits)





print("Looping from 1 to 10, but stopping when 5 is reached:")
for i in range(1, 11):
 if i == 5:
 print("\nCondition (i == 5) met! Breaking the loop.")
 break
 print(i, end=" ")
print("Program finished.")




print("Printing 1 to 10 except the number 5:")
for i in range(1, 11):
 if i == 5:
 continue # Skips the rest of the loop block for i = 5
 print(i, end=" ")
 
 
 
 num = int(input("Enter a positive integer: "))
if num < 0:
 print("Factorial does not exist for negative numbers")
elif num == 0:
 print("The factorial of 0 is 1")
else:
 fact = 1
 for i in range(1, num + 1):
 fact *= i
 print("The factorial of", num, "is:", fact)
 
 
 
 
 N = int(input("Enter which Fibonacci term you want (N): ")) 106 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
if N <= 0:
 print("Please enter a positive integer greater than 0")
elif N == 1:
 print("The 1st Fibonacci number is: 0")
elif N == 2:
 print("The 2nd Fibonacci number is: 1")
else:
 a, b = 0, 1
 for i in range(3, N + 1):
 c = a + b
 a, b = b, c
 print("The", N, "th Fibonacci number is:", b)
 
 
 
 
 
 
 num = int(input("Enter a number: "))
if num <= 1:
 print(num, "is NOT a Prime number")
else:
 is_prime = True
 for i in range(2, int(num ** 0.5) + 1):
 if num % i == 0:
 is_prime = False
 break
 
 if is_prime:
 print(num, "is a Prime number")
 else:
 print(num, "is NOT a Prime number")
 
 
 
 
 
 N = int(input("Enter upper limit (N): ")) 109 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
print("Prime numbers between 1 and", N, "are:")
for num in range(2, N + 1):
 is_prime = True
 for i in range(2, int(num ** 0.5) + 1):
 if num % i == 0:
 is_prime = False
 break
 if is_prime:
 print(num, end=" ")
 
 
 
 
 num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a, b = num1, num2
while b != 0:
 a, b = b, a % b
print("The GCD of", num1, "and", num2, "is:", a)




num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Finding GCD first
a, b = num1, num2
while b != 0:
 a, b = b, a % b
gcd = a
lcm = (num1 * num2) // gcd
print("The LCM of", num1, "and", num2, "is:", lcm)




num = int(input("Enter a positive integer: "))
if num <= 0:
 print("Please enter a positive number greater than 0")
else:
 sum_divisors = 0
 for i in range(1, (num // 2) + 1):
 if num % i == 0:
 sum_divisors += i
 
 if sum_divisors == num:
 print(num, "is a Perfect Number")
 else:
 print(num, "is NOT a Perfect Number")
 
 
 
 
 
 num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)
total_sum = 0
temp = num
while temp > 0:
 digit = temp % 10
 total_sum += digit ** power
 temp = temp // 10
if total_sum == num:
 print(num, "is an Armstrong Number")
  else:
 print(num, "is NOT an Armstrong Number")
 
 
 
 
 import math
num = int(input("Enter a number: "))
temp = num
total_sum = 0
while temp > 0:
 digit = temp % 10
 total_sum += math.factorial(digit)
 temp = temp // 10
if total_sum == num:
 print(num, "is a Strong Number")
else:
 print(num, "is NOT a Strong Number")
 
 
 
 
 num = int(input("Enter a number: "))
temp = num
rev_num = 0
while temp > 0:
 digit = temp % 10
 rev_num = (rev_num * 10) + digit
 temp = temp // 10
if num == rev_num:
 print(num, "is a Palindrome Number")
else:
 print(num, "is NOT a Palindrome Number")
 
 
 
 
 num = int(input("Enter a number: "))
square = num ** 2
# Check if square ends with the original number
if str(square).endswith(str(num)):
 print(num, "is an Automorphic Number (Square:", square, ")")
else:
 print(num, "is NOT an Automorphic Number (Square:", square, ")")
 
 
 
 
 num = int(input("Enter a number: "))
square = num ** 2
temp = square
sum_digits = 0
while temp > 0:
 digit = temp % 10
 sum_digits += digit
 temp = temp // 10
if sum_digits == num:
 print(num, "is a Neon Number")
else:
 print(num, "is NOT a Neon Number")
 
 
 
 
 
 N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
 total += i
print("Sum of the series is:", total)




N = int(input("Enter N: "))
total = 0
for i in range(2, N + 1, 2):
 total += i 123 | P a g e
Python Programming Problem Solving Practice | Mohammad Arman
print("Sum of even series is:", total)






N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1, 2):
 total += i
print("Sum of odd series is:", total)




N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
 total += i ** 2
print("Sum of square series is:", total)




N = int(input("Enter N: "))
total = 0
for i in range(1, N + 1):
 total += i ** 3
print("Sum of cube series is:", total)



total = 0
for i in range(3, 100, 3):
 total += i ** 2
print("Sum of the series 3^2 + ... + 99^2 is:", total)





N = int(input("Enter N: "))
total = 0
for i in range(2, N + 1, 2):
 total += i ** 2
print("Sum of even square series is:", total)





N = int(input("Enter number of terms (N): "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(N):
 print(a, end=" ")
 a, b = b, a + b




N = int(input("Enter N: "))
fact = 1
print("Factorial Series up to", N, ":")
for i in range(1, N + 1):
   fact *= i
 print(f"{i}! = {fact}")

 
  
   
 
 N = int(input("Enter size of square: "))
for i in range(N):
 print("* " * N)
 
  
   
    
     
      rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
 print("* " * cols)

 
  
   
    
 
N = int(input("Enter height: "))
for i in range(1, N + 1):
 print("* " * i)

 
  
     
           
# Printing Right-aligned Triangle Pattern
N = int(input("Enter height: "))
for i in range(1, N + 1):
 print(" " * (N - i) + "* " * i)

     
          
                    
 
 
 N = int(input("Enter height: "))
for i in range(N, 0, -1):
   
   
   
    
    
    