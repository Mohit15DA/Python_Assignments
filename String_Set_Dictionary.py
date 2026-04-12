"""
## String Programming Questions 
   Basic
   
1. Write a program to count the number of vowels in a string. 
Program:
count=0
st="Python is easier language!"
st1="a,e,i,o,u,A,E,I,O,U"
for ch in st:
    if ch in st1:
        count=count+1
        print("Total No. of vowels in string :",count)

2. Reverse a string without using built-in functions. 
Program:
st="Python is easier language"
print(st[::-1])

3. Check whether a string is a palindrome. 
Program:
st = "NAMAN"
print(st)
if st==st[::-1]:
    print(" Yes! Palindrome")
else:
    print("Not Palindrome")
    
4. Count uppercase and lowercase letters in a string. 
Program:
St="PythonIsEasierProgrammingLanguage"
lower=0
upper=0
for ch in St:
      if(ch.islower()):
            lower=lower+1
      else:
            upper=upper+1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)

5. Replace all spaces in a string with _. 
Program:
st="Python Is Easier Programming Language"
print(st.replace(" ","_"))

Intermediate

6. Find the frequency of each character in a string. 
Program:
st="Python Is Easier Programming Language"
for ch in st:
  print(f"frequency of element {ch} is:" ,st.count(ch))

7. Remove duplicate characters from a string. 
Program:
st="Python Is Easier Programming Language"
se_t=set()
result=""
for ch in st:
    if ch not in se_t:
        se_t.add(ch)
        result=result+ch
    print(result)
  
8. Find the first non-repeating character in a string. 
Program:
st = "varungupta"
for i in st:
    if st.count(i)==1:
        print("First Non-Repeating Charcter :",i)
        break
else:
    print("No Non-Repeating Character")


9. Check if two strings are anagrams. 
Program:
st1 = "SILENT"
st2 = "LISTEN"
if len(st1)==len(st2):
    for ch in st1:
        if st1.count(ch)!=st2.count(ch):
            print("Strings Are Not Anagram")
            break
    else:
        print("Strings Are Anagram")
else:
    print("Strings Are Not Anagram!")
    
10. Convert "hello world" → "Hello World" (title case without using .title()). 
Program:
st="hello world" 
result = " ".join(ch.capitalize() for ch in st.split())
print(result)

Tricky 

11. Find the longest word in a sentence. 
Program:
st="I am doing string assignment"
spli_t=st.split()
result=""
for ch in spli_t:
    if len(ch)>len(result):
        result=ch
    print(result)

12. Compress a string like "aaabbc" → "a3b2c1". 
Program:
st = "aaabbc"
i = 0
count = 1
temp = ""
while i<len(st)-1:
    if st[i]==st[i+1]:
        count+=1
    else:
        temp = temp+st[i]+str(count)
        count = 1
    i=i+1
temp = temp+st[i]+str(count)
print(temp)

13. Count words, characters, and digits in a string. 
Program:
st = "PYTHON 3.14 IS AMAZING"
digit_count=sum(i.isdigit() for i in st )
print("count of characters :",len (st))
print("count of words :",len(st.split()))
print("count of digit:",digit_count)

14. Rotate a string left by n positions. 
Program:
st = "ANUPAMVERMA"
print(st)
n = int(input("No of position by left : "))
st = st[n:]+st[0:n]
print(st)

15. Find all substrings of a given string.
Program:
st = "JATINKUMAR"
for i in range (0,len(st)):
    print(st[0:i+1])


## Set Programming Questions 
Basic

1. Create a set and add elements dynamically.
program:
s={55,42 }
i=int(input("Enter your no. to add in the set :"))
add=s.add(i)
print(s)

2. Find the union and intersection of two sets.
Program:
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
union=s1.union(s2)
intersection=s1.intersection(s2)
print(f"Union set is {union} and intersection set is {intersection}")

3. Remove duplicate elements from a list using a set. 
Program:
li=[1,2,3,4,5,6,5,4,3,2,1]
s=set(li)
print(s)

4. Check if an element exists in a set. 
Program:
s={1,2,3,4,5,6,7,8,9,10}
u=int(input("Enter Your Element to check:"))
for i in s:
    if u==i:
        print("Element exists")
    else:
        print("NOT Exists")
        
5. Find the difference between two sets. 
Program:
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
diff=s1.difference(s2)
print("Difference between two sets is :",diff)

Intermediate 

6. Find common elements in two lists using sets. 
Program:
li1=[1,2,3,4,5,6]
li2=[4,5,6,7,8,9]
s1=(set(li1))
s2=(set(li2))
common=s1.intersection(s2)
print("Common elements in two lists are:",common)

7. Check whether one set is a subset of another. 
Program:
s1=[1,2,3,4,5,6]
s2=[4,5,6,[1,2,3,4,5,6],7,8,9]
print("Yes! here s1 is the subset of s2:",s1 in s2)

8. Find symmetric difference of two sets. 
Program:
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
symm_diff=s1.symmetric_difference(s2)
print("SYmmetric difference:",symm_diff)

9. Count unique elements in a list using a set. 
Program:
li=[1,2,3,4,5,6,5,4,3,2,1]
se_t=set(li)
count=len(se_t)
print(count)

10. Remove all common elements from two sets. 
Program:
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
symm_diff=s1.symmetric_difference(s2)
print(symm_diff)

Tricky

11. Find missing numbers from 1 to n using sets. 
Program:

12. Check if two lists have any common elements. 
Program:
li1=[1,2,3]
li2=[4,5,6,7,8,9]
s1=(set(li1))
s2=(set(li2))
common=s1.intersection(s2)
if len(common)>0:
    print("Common elements in two lists are:",common)
else:
     print("NO Common elements")

13. Convert a set of strings into uppercase. 
Program:
s="hello sir"
print(type(s))
upper=s.upper()
print(upper)

14. Identify unique vowels in a given string using a set. 
Program:
count=0
s="hello friends"
copy_s=set(s)
s1="a,e,i,o,u,A,E,I,O,U"
for ch in copy_s:
    if ch in s1:
        count=count+1
        print("Total No. of unique vowels in string :",count)

15. Find elements that appear only once in a list.
Program:
li=[1,2,3,4,5,6,5,4,3,2,1]
for i in li:
    if li.count(i)==1:
       print(f"{i} is the Element that appear only once in a list. ")

## Dictionary Programming Questions 
Basic 

1. Create a dictionary and print all keys and values. 
Program:
d={1:11,3:55,4:66,5:8,6:77}
for i,j in d.items():
    print(f"Keys{i}and Values are{j} ")

2. Count frequency of each word in a sentence. 
Program:
st=["Python" ,"Is", "Easier", "Programming", "Language"]
for ch in st:
    ch1=len(ch)
    print(f"{ch}:",ch1)
    
3. Merge two dictionaries. 
Program:
d1={1:34,2:67,4:78,'A':54}
d2={6:24,3:46,9:45,7:88}
d1.update(d2)
print(d1)
    
4. Find the length of a dictionary. 
Program:
d1={1:34,2:67,4:78,'A':54}
print(len(d1))
    
5. Check if a key exists in a dictionary. 
Program:
u=int(input("Enter key to check existence:"))
d1={1:34,2:67,4:78,'A':54}
for i,j in d1.items():
    if u==i:
     print("Key exists in a dictionary")
    else:
        print("NOT Exists")
    
Intermediate 

6. Sort a dictionary by values. 
Program:
d1={1:34,2:67,4:78,'A':54}
for i,j in d1.items():
    ch=d1.values()
    ch1=list(ch)
    ch2=ch1.sort()
    print(ch1)
    
7. Find the key with the maximum value. 
Program:
d1={1:34,2:67,4:78,'A':54}
max_val=(max(d1.values()))
for i,j in d1.items():
    if max_val==j:
        print("Key with max value:",i)

8. Remove a key from a dictionary. 
Program:
a = {"name": "Varun", "age": 25, "city": "New York"}
rv = a.pop("age")
print(a)  
print(rv)  

9. Convert two lists into a dictionary. 
Program:
li1=[1,2,3,4]
li2=[6,7,8,9]
dic = {}
for k, v in zip(li1, li2):
    dic[k] = v
print(dic)

10. Count character frequency using a dictionary. 
Program:
d={"The","Python"," Is"," Easier"," Programming"," Language"}
d1=list(d)
for ch in d1:
    print(f"frequency of element {ch} is:" ,d1.count(ch))

Tricky 

11. Invert a dictionary (swap keys and values). 
Program:
o_d={1:34,2:45,3:56,4:55}
inverted_d=dict(zip(o_d.values(),o_d.keys()))
print(inverted_d)

12.Group elements by frequency using a dictionary. 
Program:

13. Find duplicate values in a dictionary. 
Program:

14. Create a nested dictionary for student records. 
Program:
students={}
students['student1'] = {'name': 'Anupam', 'age': 20, 'grade': 'A'}
students['student2'] = {'name': 'Varun', 'age': 22, 'grade': 'B'}
students['student3'] = {'name': 'Jatin', 'age': 21, 'grade': 'A+'}
print("Student Details:",students)

15. Flatten a nested dictionary.
Program:

## Mixed (String + Set + Dictionary)

1. Count unique words in a sentence. 
Program:
st="I am doing string assignment"
se_t=set(st)
print("Unique Words :",se_t)

2. Find common characters between two strings. 
Program:
st="I am doing string assignment"
st1=" I am doing project "
se_t=set(st)
se_t1=set(st1)
print("common characters:",se_t.intersection(se_t1))

3. Find the most frequent character in a string.
Program:

4. Remove duplicate words from a sentence.
Program:
st="I am doing string assignment"
se_t=set(st)
print("After removing duplicate words:",se_t)

5. Find words with the same letters (anagram groups).
Program:

"""







