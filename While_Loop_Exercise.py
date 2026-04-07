"""
Python While Loop Exercise 
## Part 1 – Basic Level

1. Print numbers from 1 to 10 using a while loop.
Program:
a=1
while a<=10:
    print(a)
    a=a+1

2. Print even numbers from 1 to 20. 
Program:
a=1
while a<=20:
    if a%2==0:
      print("Even no.s are:",a)
    a=a+1
    
3. Print odd numbers from 1 to 20. 
Program:
a=1
while a<=20:
    if a%2!=0:
      print("Odd no.s are:",a)
    a=a+1
    
4. Print numbers from 10 to 1 (reverse order). 
Program:
a=10
while a>=1:
    print("Reverse order are:",a)
    a=a-1
      
5. Print multiplication table of 5 using while loop. 
Program:
n=5
a=1
while a<=10:
    print(f"{n}*{a}=",n*a)
    a=a+1
    
## Part 2 – Intermediate Level 

6. Find the sum of first 10 natural numbers using while loop. 
Program:
count=0
a=1
while a<=10:
    count=count+a
    print(count)
    a=a+1
    
7. Find factorial of a number entered by user. 
Program:
factorial=1
n=int(input("Enter your no. to know factorial:"))
while n>=1:
    factorial=n*factorial
    print("factorial is =",factorial)
    n=n-1
    
8. Count number of digits in a given number. 
Program:
count=0
n=int(input("Enter your number to count digits :"))
while n>0:
    rem=n%10
    n=n//10
    count=count+1
    print("no.of digits is:",count)
    
9. Reverse a number using while loop. 
Program:
n=int(input("Enter your number to reverse :"))
add=0
while n>0:
    rem=n%10
    add=add*10+rem
    n=n//10
    print("reverseof number is:",add)
   
10. Check whether a number is palindrome or not using while loop. 
Program:
n=int(input("Enter number to check palindrome :"))
copy=n
add=0
while n>0:
    rem=n%10
    add=add*10+rem
    n=n//10
if copy==add:
    print("palindrome")
else:
    print("Not palindrome")
    
    
## Part 3 – Pattern Based 

11. Print pattern: 
* 
** 
*** 
**** 
***** 
Program:
i=1
while i<=5:
    print("*"*i)
    i=i+1
    
12. Print pattern: 
1 
12 
123 
1234 
12345 
Program:
i=1
while i<=5:
    j=1
    while j<=i:
       print(j,end='')
       j=j+1
    print()
    i=i+1

   
## Part 4 – Logical / Real Scenario 

13. Ask user to enter password until correct password is entered. 
Program:
password="yo yo 123"
u_input=""
while u_input!=password:
    u_input=input("Enter Your Password:")   
if u_input==password:
    print("Access Granted")
else:
    print("INcorrect Password.Please try again!")
    
14. Create a number guessing game: 
• Generate a random number (1–10) 
• Keep asking user until they guess correctly 
Program:
import random
num= random.randint(1,10)
while True:
    u= int(input("Guess A number from 1 to 10:"))
    if num==u:
        print("you guess the right number")
        break
    
15. Keep taking input numbers until user enters 0, then print total sum. 
Program:
add=0
while True:
    num=int(input("Enter your numbers to add OR (enter zero to exit):"))
    add=add+num
    if num==0:
        break
print("adittion",add)
    

## Bonus Challenge (Interview Level) 

16. Print Fibonacci series up to N terms using while loop. 
Program:
n=int(input("Enter value of N terms:"))
a=int(input("Enter value of 'A' which means starting of fabonacci:"))
b=a+1
terms=0
while terms<=n-1:
    c=a+b
    print(c)
    a=b
    b=c
    terms=terms+1
    
17. Check whether a number is Armstrong number. 
Program:
num=int(input("Enter your number to check armstrong:"))
copy=num
add=0
while num>0:
    rem= num%10
    add= add+rem**3
    num=num//10
print("New number",add)
if copy==add:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
18. Print prime numbers between 1 to 50 using while loop.
Program:
num=2
while num <=50:
    is_prime= True
    d=2
    while d *d <=num:
        if num %d==0:
            is_prime=False
            break
        d=d+1
    if is_prime:
        print(num)
    num =num+1
    
            


"""



