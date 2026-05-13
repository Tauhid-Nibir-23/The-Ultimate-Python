# Tuple ordered এবং unchangeable (immutable)।

# Tuple তৈরি করা হয় parentheses () দিয়ে।
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Tuple এর মধ্যে duplicate values থাকতে পারে।
my_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(my_tuple) 

# Tuple এর মধ্যে বিভিন্ন ধরনের data types থাকতে পারে।
my_tuple = ("abc", 34, True, 40, "male")
print(my_tuple)

# Tuple এর মধ্যে list থাকতে পারে। 
my_tuple = ("apple", "banana", "cherry", [1, 2, 3])
print(my_tuple)

# Tuple এর মধ্যে tuple থাকতে পারে।
my_tuple = ("apple", "banana", "cherry", ("a", "b", "c"))
print(my_tuple)
print(len(my_tuple)) # Tuple এর length বের করা যায়।

thistuple = ("apple",)
print(type(thistuple)) # Single value এর জন্য comma লাগাতে হয়।

thistuple = ("apple")
print(type(thistuple)) # Single value এর জন্য comma না দিলে তা string হিসেবে বিবেচ

thattuple = tuple(("apple", "banana", "cherry")) # Tuple constructor ব্যবহার করে tuple তৈরি করা।
print(thattuple)    

tuple1 = (1,4,2,3,5)
print(sorted(tuple1)) # Tuple কে sorted list এ রূপান্তর করা যায়。
print(tuple(sorted(tuple1))) # Sorted list কে আবার tuple এ রূপান্তর করা যায়।
print(tuple1[1]) 
print(tuple1[-1])
print(tuple1[2:5]) # Tuple slicing করা যায়。   
print(tuple1[:4])
print(tuple1[2:])   

minetuple = ("apple", "banana", "cherry")
x = list(minetuple) # Tuple কে list এ রূপান্তর করা যায়।
x[1] = "kiwi" # List এর value পরিবর্তন করা যায়।
minetuple = tuple(x) # List কে আবার tuple এ রূপান্তর করা যায়।
print(minetuple)

minetuple = ("apple", "banana", "cherry")
x = list(minetuple) # Tuple কে list এ রূপান্তর করা যায়।
x.pop(1)    # List এর value পরিবর্তন করা যায়।
minetuple = tuple(x) # List কে আবার tuple এ রূপান্তর করা যায়।
print(minetuple)


thattuple = ("apple", "banana", "cherry")
print(thattuple)  
if "banana" in thattuple:
    print("Yes, 'banana' is in the tuple")  

thattuple = ("apple", "banana", "cherry")
del thattuple # Tuple মুছে ফেলা যায়।
print(thattuple) # NameError: name 'thattuple' is not defined 

thistuple = (1,2,3,2,2,4,5)
print(thistuple.count(2)) # Tuple এর মধ্যে একটি নির্দিষ্ট value কতবার আছে তা বের করা যায়।
print(thistuple.index(4)) # Tuple এর মধ্যে একটি নির্দিষ্ট value এর index বের করা যায়।
