"""
## Beginner Level (Basics) 
1.Write a function to print "Hello World".  
Program:
def greet():
    print("Hello World")

greet()

2. Create a function that takes a number and returns its square.  
Program:
num=int(input("Enter no. to know square:"))
def greet(num):
    return num*num
print(greet(num))

3. Write a function to check whether a number is even or odd.  
Program:
def check_even(num):
    if num%2==0:
       return True
    return False

num=int(input("Enter your no. to check even or odd:"))
if check_even(num):
    print("EVEN")
else:
    print("ODD")
    
4. Create a function that returns the sum of two numbers.  
Program:
def add(a,b):
    return a+b

a=int(input("Enter A nubmer to add:"))
b=int(input("Enter B nubmer to add:"))
print(add(a,b))

5. Write a function to find the maximum of three numbers.  
Program:
def ismax(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(ismax(5,6,7))

6. Create a function that takes a string and returns it in uppercase.  
Program:
def Upper_case(text):
    return text.upper()
print(Upper_case("python"))
        
7. Write a function to calculate the factorial of a number.  
Program:

8. Create a function that checks if a number is positive, negative, or zero.  
9. Write a function to count the number of vowels in a string.  
10. Create a function that returns the length of a list (without using len()).
  


"""
def Upper_case(text):
    return text.upper()
print(Upper_case("python"))
        

    
