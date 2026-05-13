
#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a ="Hello, World!"
print(a[1]) # 'e', position 1 (0-based index)

a ="Hello, World!"
print(len(a))# 13

for x in "banana":
    print(x)

txt ="The best things in life are free!"
print("free"in txt)# True

if "free" in txt:
    print("Yes, 'free' is present.")

#Python - Slicing Strings

b ="Hello, World!"
print(b[2:5])


b ="Hello, World!"
print(b[-5:-2])

txt ="Python"
print(txt[-3:])# hon

txt ="Python"
print(txt[:4])# Pyth


#Python - Modify Strings

a ="Hello, World!"
print(a.upper())# HELLO, WORLD!

a ="Hello, World!"
print(a.lower())# hello, world! 

a ="   Hello, World!   "
print(a.strip())# Hello, World! (leading and trailing whitespace removed)

a ="Hello, World!"
print(a.replace("H", "J"))# Jello, World!

a ="Hello, World!"
print(a.split(","))# ['Hello', ' World!'] (split at the comma)

#Python - Format - Strings

age =23
txt =f"My name is Arman, I am {age}"
print(txt)

txt =f"The price is {20 * 59} dollars"
print(txt) # The price is 1180 dollars

txt ="We are the so-called \"Vikings\" from the north."
print(txt)

txt ='It\'s Python'
print(txt) # It's Python

txt ="This is a backslash: \\"
print(txt) # This is a backslash: \

txt ="Hello\nWorld!\tPython"
print(txt)


# " " (empty string)
#  [] (empty list)
#  () (empty tuple)
#  {} (empty dictionary)

# isinstance() function চেক করে কোনো object নির্দিষ্ট data type-এর কিনা।

x =200
print(isinstance(x,int))# True
