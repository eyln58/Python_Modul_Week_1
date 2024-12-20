# Question 1: 
for i in range(1, 11):
    print(i)

-------------------------------------------
# Question 2: 
number = int(input("Enter a number: "))

for i in range(0, number + 1, 2):  
    print(i)

# Using 'while' loop
number = int(input("Enter a number: "))
i = 0
while i <= number:
    print(i)
    i += 2  
----------------------------------------------

# Question 3: 
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
for i in range(start, end + 1): 
    print(i)

----------------------------------------------

# Question 4: 
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
----------------------------------------------
# Question 5: 
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):  
    factorial *= i  
print("Factorial:", factorial)

-----------------------------------------------

# Question 6: 
number = int(input("Enter a number: "))
if number > 1:
    is_prime = True
    for i in range(2, number + 1):  
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
else:
    print("Zero is not prime number.")
------------------------------------------------
# Question 7: 

limit = int(input("Fibonacci sequence limit: "))
if limit == 0:  
    print("It is zero")
else:
    fibonacci = [0, 1]  
    for _ in range(limit):  
        next_number = fibonacci[-1] + fibonacci[-2]  
        if next_number > limit: 
            break
        fibonacci.append(next_number) 
    print("Fibonacci sequence up to", limit, ":", fibonacci)
-----------------------------------------------------
# Question 8: 
word = input("Enter a word: ")
reversed_word = word[::-1]  
print("Reversed word:", reversed_word)
---------------------------------------------------
# Question 9: 
word = input("Enter a word: ").lower()
if word == word[::-1]:  
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
---------------------------------------------------
# Question 10: 
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)  
print("Your BMI is:", round(bmi, 2))
if bmi < 25:
    print("You are underweight.")
elif bmi < 30:
    print("You have a normal weight.")
elif bmi < 40:
    print("You are overweight.")
else:
    print("You are obese.")
------------------------------------------------------
# Question 11: 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largest = max(num1, num2, num3) 
print("The largest number is:", largest)

-------------------------------------------------------

course_result = ""  
courses=["Math","Geo","Chemistry","Biology"]
for i in courses: 
    Midterm = float(input(f"Midterm for {i}: "))
    final = float(input(f"Final for {i}: "))
    ave = (Midterm * 0.4) + (final * 0.6)    
    if ave >= 50:
        result = "Succeed"
    else:
        result = "Failed"  
    course_result += f"Course {i} - Average: {ave:.2f}, Status: {result}\n"
print(course_result)
