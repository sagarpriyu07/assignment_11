#print factorial of any number
n=int(input("Enter any number="))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("Factorial of number",n,"is",fact)