#Convert decimal number to octal number
n=int(input("Enter any number="))
x=n
b=str()
while x>0:
    t=x%8
    b=str(t)+b
    x=x//8
b="0o"+b
print(b)