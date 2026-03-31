"""
Python Programming Questions – LIST 
Basic Level

1. Write a Python program to create a list of integers and print its elements.

Program:
i= int(input("enter your number from  1 to :"))
li=[]
for i in range(1,i+1):
      li.append(i)
print("Your List is ",li)
for num in li:
    print(num)

2. Write a program to find the sum and average of all elements in a list.

Program:
i= int(input("enter your number from  1 to :"))
li=[]
for i in range(1,i+1):
      li.append(i)
print(li)      
print("the sum is:",sum(li))
print("the average is :",sum(li)/len(li))  


3. Write a program to find the largest and smallest element in a list.

Program:
i= int(input("enter your number from  1 to :"))
li=[]
for i in range(1,i+1):
      li.append(i)
print(li)      
print("the largest element is:",max(li))
print("the smallest element is :",min(li))


4. Write a Python program to count the number of elements in a list without using len().

Program:
i= int(input("enter your number from  1 to :"))
li=[]
count=0
for i in range(1,i+1):
      li.append(i)
print("Your List is ",li)
for num in li:
    print(num)
    count = count+1
print(" Total lenght :",count)


5. Write a program to reverse a list without using built-in functions.

Program:
i= int(input("enter your number from  1 to :"))
li=[]
for i in range(1,i+1):
      li.append(i)
print("Your List is ",li)
li.reverse()
print("Reverse List is",li)


6. Write a program to check if an element exists in a list.

Program:
i= int(input("enter your number from  1 to :"))
li=[]
for i in range(1,i+1):
      li.append(i)
print("Your List is ",li)
check= int(input(" enter no.to check:"))
if check in li:
    print("Yes element exists in the list")
else:
    print ("No element not exists in the list")


7. Write a Python program to remove duplicate elements from a list.

Program:
li=[1,12,23,52,12,23,96,56]
print("Your List is ",li)
new_li=[]
for num in li:
    if num not in new_li:
        new_li.append(num)
print("NEW list without duplicates",new_li)        


8. Write a program to sort a list in ascending and descending order.

Program:
li=[1,12,23,52,12,23,96,56]
print("Your List is ",li)
li.sort()
print("Ascending",li)
li.reverse()
print("Descending",li)

Intermediate Level

9. Write a program to merge two lists and remove duplicates.
Program:
li1=[1,12,23,34,45,56,78]
li2=[45,78,89,45,65,25,42]
sol=list(set(li1+li2))
print("merge list",sol)

10. Write a program to find common elements between two lists.
Program:
li1=[1,12,23,34,45,56,78]
li2=[45,78,89,45,65,25,42]
common=list(set(li1)&set(li2))
print("common relements",common)

11. Write a program to split a list into even and odd numbers.
Program:
li=[12,13,45,16,18,19,9,8,6,7]
O_list=[]
E_list=[]
for num in li:
    if num%2==0:
        E_list.append(num)
    else:
        O_list.append(num)
print("EVEN list",E_list)
print("ODD list",O_list)

12. Write a program to rotate a list by n positions.
Program:
li=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter N no of right rotations: "))
for i in range(n):
    val=li.pop(len(li)-1)
    li.insert(0,val)
print(li)

13. Write a Python program to find the second largest number in a list.
Program:
li=[11,45,9,2,35,65]
print(li)
li.sort()
print(li)
li.reverse()
print(li)
print("second largest",li[1])

14. Write a program to flatten a nested list.
Program:
li=[11,[45,9],2,35,[65,55,41],13,45]
f_li=[]
print("Nested list:",li)
for x in li:
    if type(x)==list:
        for i in x:
         f_li.append(i)
    else:
        f_li.append(x)
print("Flatten list:",f_li)
    
15. Write a program to count frequency of each element in a list.
Program:

16. Write a program to replace all negative numbers with zero in a list.
Program:

Advanced Level

17. Write a program to remove all occurrences of a given element from a list.
Program:

18. Write a program to check if a list is a palindrome.
Program:

19. Write a Python program to find missing numbers in a given list of consecutive integers.
Program:

20. Write a program to perform element-wise addition of two lists.
Program:

21. Write a Python program to find the longest increasing subsequence in a list.
Program:
li=[21,78,89,765,23,34,35,39,45,667,8,10,635,58]
longest_sub_seq=[]
temp=[]
for i in range(0,len(li)-1):
    if li[i]<li[i+1]:
        temp.append(li[i])
    else:
        temp.append(li[i])
        if len(temp)>len(longest_sub_seq):
            longest_sub_seq=temp
            temp=[]
print(longest_sub_seq)
    
22. Write a program to group elements based on frequency.
Program:
li=[1,5,6,8,9,9,8,1,2,3,8,4,5,6,12,13,14,12,13,14,88,98,77]
grouped_list=[]
selected=[]
for x in li:
    if x not in selected:
        selected.append(x)
        for j in li:
            if x==j:
                grouped_list.append(j)  
print("GROUPED list:",grouped_list)

Python Programming Questions – TUPLE 
Basic Level 
23. Write a Python program to create a tuple and print its elements. 
Program:

24. Write a program to find the length of a tuple. 
Program:

25. Write a program to find the maximum and minimum element in a tuple. 
Program:

26. Write a program to convert a tuple into a list. 
Program:

27. Write a program to check if an element exists in a tuple. 
Program:

28. Write a program to count occurrences of an element in a tuple. 
Program:

Intermediate Level 
29. Write a program to slice a tuple and display the result. 
Program:

30. Write a program to find repeated elements in a tuple. 
Program:

31. Write a program to merge two tuples. 
Program:

32. Write a program to unpack elements of a tuple into variables. 
Program:

33. Write a Python program to sort a tuple. 
Program:

34. Write a program to convert a list of tuples into a dictionary. 
Program:

Advanced Level 
35. Write a program to find the index of an element in a tuple. 
Program:

36. Write a program to remove an element from a tuple (without directly modifying it). 
Program:

37. Write a program to find common elements between two tuples. 
Program:

38. Write a Python program to check if a tuple is a palindrome. 
Program:

39. Write a program to find the element with maximum frequency in a tuple. 
Program:
t=(1,5,5,78,9,4,653,2,4,6,78,6,4,4,5,3,45,6,7,4,4)
maxx=t.count(t[0])
element=t[0]
for m in t:
    if maxx<t.count(m):
        maxx=t.count(m)
        element=m
print(element,maxx)

40. Write a program to create a nested tuple and access its elements.
Program:


"""



