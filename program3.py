Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="hello world"
print(x)
hello world
x=20
print
<built-in function print>(
print(x)
20
x=20.5
print(x)
20.5
x=lj
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x=lj
NameError: name 'lj' is not defined
x=1j
print(x)
1j
x["apple","banana","cherry"]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x["apple","banana","cherry"]
TypeError: 'complex' object is not subscriptable
x=["apple","banana","cherry"]
print
<built-in function print>
(x)
['apple', 'banana', 'cherry']
x=True
print(x)
True
x=("apple","banana","cherry")
print(x)
('apple', 'banana', 'cherry')
x={"name":"john":"age":36}
SyntaxError: invalid syntax
x={"name":"john","age":36}
print(x)
{'name': 'john', 'age': 36}
