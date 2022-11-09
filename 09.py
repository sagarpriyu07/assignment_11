#Convert decimal number to binary number
n=int(input("Enter any number"))
x=n
b=str()
while x>0:
    t=x%2
    b=str(t)+b
    x=x//2
b="0b"+b
print(b)