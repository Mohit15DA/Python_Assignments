"""
PART 1 – Basic For Loop Questions

Q1. Print Numbers
Use a for loop to print numbers from 1 to 10.

Program:
for i in range(1,11,1):
 print(i)

Q2. Print Even Numbers 
Print all even numbers between 1 and 20.

Program:
for i in range(1,21,1):
      if (i%2)==0:
       print(i)
       
Q3. Find Sum 
Print the sum of numbers from 1 to 10 using a for loop.

Program:
sm=0
for i in range(1,11):
     sm=sm+i
     print(" sum of numbers",sm)

Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.

Program:
num= int(input("Enter which table:"))
for i in range (1,11):
    print (num*i)

Q5. Count Characters 
Take a string and count the total number of characters using a for loop.

Program:
text="hello python"
count=0
for char in text:
    count=count+1
    print("total no.of characters is",count)
 
PART 2 – Break Related Questions

Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5.

Program:
for i in range(1,11):
    print(i)
    if i==5:
        break

Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.

Program:
numbers=[2,3,5,10,15,20,25,30,35,40]
for num in numbers:
    if num==25:
        print("found")
        break

Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop.

Program:
number=[1,2,3,4,-2,3,-4,6]
for num in number:
    if num<0:
        print(" first negative no. is ",num)
        break

PART 3 – Continue Related Questions

Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5.

Program:
for i in range(1,11):
    if i==5:
        continue
    print(i)

Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers.

Program:
for i in range(1,21):
    if i%2==0:
        continue
    print(i)

Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O".

Program:
text="PYTHON"
for char in text:
    if char=="O":
        continue
    print(char)

PART 4 – Pass Related Questions 
 
Q12. Empty Loop 
Run a loop from 1 to 5 but do nothing inside the loop using pass.

Program:
for i in range(1,6):
     if i==3:
         pass
     print(i)

Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass.

Program:
for i in range(1,11):
     if i==6:
         pass
     print(i)
 
PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.) 
 
Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found".

Program:
number=[10,20,30,100,20,30,50]
for num in number:
 if num==100:
    print("Found")
 else:
    print("Not Found")
       
 
Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else.

Program:
count=0
num= int(input("Enter your number:"))
for i in range (1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("prime")
else:
     print("not prime")
     
 
PART 6 – Pattern Questions 
 
Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****

Program:
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()
 
Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
* 

Program:
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()
 
Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345

Program:
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555

Program:
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()
 
Q20. Pyramid Pattern 
Print:
    * 
   *** 
  ***** 
 ******* 
*********      

Program:
for i in range(1,10,2):
    for k in range(9,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print("* ",end='')
    print()

 
Q21. Inverted Pyramid 
Print: 
********* 
 ******* 
  ***** 
   ***
    *
Program:
for i in range(9,-1,-2):
    for k in range(9,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print("* ",end='')
    print()


Bonus Question

Q22. Break in Pattern 
Print a star pattern. 
Stop printing when the row number reaches 4.

Program:
for i in range(1,10):
    if i==4:
            break
    for j in range(1,i+1):
        print("*",end='')
    print()

    
"""




















     
     
