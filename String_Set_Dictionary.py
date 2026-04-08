"""
## String Programming Questions 
   Basic
   
1. Write a program to count the number of vowels in a string. 
Program:

2. Reverse a string without using built-in functions. 
Program:

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

5. Replace all spaces in a string with _. 
Program:

Intermediate

6. Find the frequency of each character in a string. 
Program:

7. Remove duplicate characters from a string. 
Program:

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

Tricky 

11. Find the longest word in a sentence. 
Program:

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

"""







