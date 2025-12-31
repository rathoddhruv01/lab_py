Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#assigment operator
x=10
print(x)
10
#urnary minus
a=5
print(-a)
-5
#relational
p=10
q=5
print(p>q)
True
print(p==q)
False
#logical
x=true
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
x = True
y = False
print(x and y)
False
print(x or y)
True
print(not x)
False
#boolean
is pass = True
SyntaxError: invalid syntax
print(is pass) #o/p = True
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
is_pass = True
print(is_pass) #o/p = True
True
#bitwise
a=5
b=3
print(a & b)
1
print(a|b)
7
#membership
numbers=[1,2,3,4,6]
print(2 in number)  #o/p=True
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(2 in number)  #o/p=True
NameError: name 'number' is not defined. Did you mean: 'numbers'?
print(2 in numbers)  #o/p = True
True
print(5 not in numbers) #o/p = false
True
#indentity
x=10
y=10
print(x is y)
True
print(x is not y)
False
