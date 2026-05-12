num = 5
num = 'Nibir'
print(num)
print(type(num))

x = int(3)
X=str(3)
print(X)
print(type(X))
print(type(x))

n,b,r = 'Blue','Red','Green'
print(n)
print(b)        
print(r)

names = ["Arman","Rahim","Karim"]
n1, n2, n3 = names
print(n1)
print(n2)
print(n3)

fruits = ["apple","banana","cherry"]
p, y, z = fruits
print(p)
print(y)
print(z)

print(n1+n2+n3)
# comma(,) dile ekta space aisha pore
print(n1,n2,n3)


t  ="awesome"# global variable

def myfunc():
    t ="fantastic"# local variable
    print("Python is " + t)

myfunc()

print("Python is " + t)
