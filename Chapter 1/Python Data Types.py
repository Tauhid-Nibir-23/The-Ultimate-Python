# ==============================
# Python Data Types বিস্তারিত Note
# ==============================


x = "Hello World"  
# str (String)
# Characteristics:
# 1. Text/String data store করে
# 2. "" বা '' quotation use হয়
# 3. Immutable (change করা যায় না)

x = 20  
# int (Integer)
# Characteristics:
# 1. Whole number store করে
# 2. Decimal থাকে না
# Example: 10, -5, 100

x = 20.5  
# float
# Characteristics:
# 1. Decimal number store করে
# 2. Fractional value support করে
# Example: 3.14, 5.6

x = 1j  
# complex
# Characteristics:
# 1. Complex number store করে
# 2. Real + Imaginary part থাকে
# Example: 2+3j

x = ["apple", "banana", "cherry"]  
# list
# Characteristics:
# 1. Ordered collection
# 2. Mutable (change করা যায়)
# 3. Duplicate value allow করে
# 4. [] square bracket use হয়

x = ("apple", "banana", "cherry")  
# tuple
# Characteristics:
# 1. Ordered collection
# 2. Immutable (change করা যায় না)
# 3. Duplicate value allow করে
# 4. () bracket use হয়

x = range(6)  
# range
# Characteristics:
# 1. Number sequence তৈরি করে
# 2. সাধারণত loop এ use হয়
# 3. Output: 0,1,2,3,4,5

x = {"name": "Arman", "age": 20}  
# dict (Dictionary)
# Characteristics:
# 1. Key-Value pair এ data store হয়
# 2. Mutable
# 3. {} bracket use হয়
# 4. Key unique হতে হয়

x = {"apple", "banana", "cherry"}  
# set
# Characteristics:
# 1. Unordered collection
# 2. Duplicate value allow করে না
# 3. Mutable
# 4. {} bracket use হয়

x = frozenset({"apple", "banana", "cherry"})  
# frozenset
# Characteristics:
# 1. Immutable set
# 2. Duplicate allow করে না
# 3. Change করা যায় না

x = True  
# bool (Boolean)
# Characteristics:
# 1. শুধু True বা False value থাকে
# 2. Conditional statement এ use হয়

x = b"Hello"  
# bytes
# Characteristics:
# 1. Binary data store করে
# 2. Immutable
# 3. b prefix use হয়

x = bytearray(5)  
# bytearray
# Characteristics:
# 1. Mutable binary data
# 2. Bytes modify করা যায়

x = memoryview(bytes(5))  
# memoryview
# Characteristics:
# 1. Memory access করতে use হয়
# 2. Large binary data efficiently handle করে

x = None  
# NoneType
# Characteristics:
# 1. No value / empty value বোঝায়
# 2. Variable এ কিছু assign না থাকলে use হয়



# ==============================
# List এবং Tuple Example
# ==============================

fruits = ["apple", "banana"]
# list example
# Mutable collection

colors = ("red", "green")
# tuple example
# Immutable collection

print(type(fruits))
# type() function variable এর data type দেখায়

print(type(colors))




# ==============================
# Multiple Variable Type Check
# ==============================

a = "Arman"    
# str

b = 25         
# int

c = 3.14       
# float

d = True       
# bool

print(type(a), type(b), type(c), type(d))

# Output:
# <class 'str'> <class 'int'> <class 'float'> <class 'bool'>