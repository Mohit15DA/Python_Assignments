"""
A. Python IF (Single Condition)

1. Write a Python program to check if a number is positive.
Program:
num= int(input("enter no to check"))
if num>0:
 print("Positive")

2. Print "Eligible to vote" if age is 18 or above.
Program:
age= int(input("Enter your age :"))
if age>=18:99

 print("Eligible to vote")

3. Check if a number is divisible by 7.
Program:
num= int(input("Enter your number :"))
if num%7==0:
 print("Number is Divisible by 7")

4. Print "Pass" if marks are greater than 40.
Program:
marks= int(input("Enter your marks :"))
if marks>40:
 print("Pass")
 
5. Check if a number is greater than 100.
Program:
num= int(input("Enter your number :"))
if num>100:
 print(f"{num} is Greater than 100 ")
 
6. Display a message if temperature exceeds 45°C.
Program:
temp= int(input("Enter temperature :"))
if temp>45:
 print(f"{temp} temperature exceeds ")

7. Check if a string length is more than 8 characters.
Program:
st= input("Enter your string :")
if len(st)>8:
 print("string has more than 8 characters")

8. Print "Logged In" if password matches "admin123".
Program:
password="admin123"
login_password = input("Enter your password:")
if login_password== password:
 print("Logged In")
 
9. Check if a number is a multiple of 10. 
Program:
num= int(input("Enter your number:"))
if num%10==0:
 print("Multiple of 10")

10. Print a warning if balance is below minimum limit.
Program:
bal= int(input("Enter your balance:"))
minimum_limit=1000
if bal<minimum_limit :
 print("Warning :Your balance is low")

B. Python IF–ELSE (Two Conditions)

11. Check whether a number is even or odd.
Program:
num= int(input("enter no to check"))
if num%2==0:
 print("Even")
else:
    print("Odd")
    
12. Find the largest of two numbers.
Program:
n1=int(input("Enter your first number:"))
n2=int(input("Enter your second number:"))
if n1>n2:
 print(f"{n1}, is greater")
else:
    print(f"{n2}, is greater")
    
13. Check whether a person is eligible for driving license.
Program:
age=int(input("Enter your age:"))
if age>=18:
 print("Eigible for license")
else:
    print("Not eligible for license")

14. Print "Pass" or "Fail" based on marks.
Program:
marks=int(input("Enter your marks out of 100:"))
if marks>=33:
 print("Pass")
else:
    print("Fail")
    
15. Check whether a number is positive or negative.
Program:
num= int(input("enter no to check:"))
if num>0:
 print("Positive")
else:
    print("Negative")

16. Check whether a character is a vowel or consonant.
Program:
ch= input("Enter charater:")
if ch=='a':
 print("Vowel")
else:
    if ch=='e':
        print("Vowel")
    else:
        if ch=='i':
            print("Vowel")
        else:
            if ch=='o':
                print("Vowel")
            else:
                if ch=='u':
                   print("Vowel")
                else:
                    print("Consonant")


17. Check if a year is leap or not.
Program:

18. Print "Valid Password" or "Invalid Password".
Program:
pass_word=input("Enter your password:")
password="Python1234"
if pass_word==password:
    print("Valid password")
else:
    print("Invalid password")
    
19. Determine whether salary is taxable or not.
Program:
salary=int(input("Enter your salary:"))
if salary >=10000:
    print("Taxable")
else:
    print("Not taxable")

20. Check whether a number is greater than 50 or not.
Program:
num=int(input("Enter your num:"))
if num>50:
    print("Greater than 50")
else:
    print("Not greater than 50")

C. Python NESTED IF–ELSE

21. Find the largest of three numbers.
Program:
n1=int(input("Enter your first number:"))
n2=int(input("Enter your second number:"))
n3=int(input("Enter your third number:"))
if n1>n2:
    if n1>n3:
        print(f"{n1} is largest")
    else:
        print(f"{n3} is largest")
else:
    if n2>n3:
        print(f"{n2} is largest")
    else:
        print(f"{n3} is largest")

22. Check whether a number is positive, negative, or zero.
Program:
num=int(input("Enter your number:"))
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")
        
23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60
Program:
num=int(input("Enter your numbers:"))
if num>=90:
    print("A Grade")
else:
    if num>=75:
        print("B Grade")
    else:
        if num>=60:   
            print("C Grade")
        else:
            print("Fail")
        
24. Check whether a triangle is equilateral, isosceles, or scalene.
Program:

25. Check whether a character is uppercase, lowercase, digit, or special character. 
26. Calculate electricity bill using slab-wise rates. 
27. Validate login using username and password. 
28. Check student result using marks of 3 subjects. 
29. Find the second largest number among three numbers. 
30. Check loan eligibility using age, salary, and credit score.
"""






