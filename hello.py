a=["apple","banana","cherry"]   #list
b=("apple","banana","cherry")   #tuples
c={"apple","banana","cherry"}   #set
d={"name":"raihan", "roll": "5"}    #dict
print(a,b,c,d)


x=int(input("Take first int number: "))

y=int(input("Take second int number: "))

print("Add: ",x+y)
print("Sub: ",x-y)
print("Mul: ",x*y)
print("Div: ",x/y)
print("Mod: ",x%y)

if (x>y):
    print(x ,"is greater then ",y)
else:
    print(y," is greater than ",x)

if x <= y:
    for i in range(x, y+1):
        print(i)
else:
    for i in range(x, y-1, -1):
        print(i)

string_input = input("Take string input: ")

if x <= y:
    if string_input == "even":
        for i in range(x, y+1):
            if i % 2 == 0:
                print(i)
    elif string_input == "odd":
        for i in range(x, y+1):
            if i % 2 != 0:
                print(i)
else:
    if string_input == "even":
        for i in range(x, y-1, -1):
            if i % 2 == 0:
                print(i)
    elif string_input == "odd":
        for i in range(x, y-1, -1):
            if i % 2 != 0:
                print(i)

from function import even_odd

x = int(input("Take first int number: "))
y = int(input("Take second int number: "))
string_input = input("Type even/odd string input: ")

even_odd(x, y, string_input)
 