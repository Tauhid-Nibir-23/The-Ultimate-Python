minetuple = ("apple", "banana", "cherry")
x = list(minetuple) # Tuple কে list এ রূপান্তর করা যায়।
x.pop(1)    # List এর value পরিবর্তন করা যায়।
minetuple = tuple(x) # List কে আবার tuple এ রূপান্তর করা যায়।
print(minetuple)