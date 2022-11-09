#print sum of all digits in any number
n=int(input("Enter any number"))
x=n
sum=0
while x!=0:
    sum=sum+x%10
    x=x//10
print("Sum of all digits in",n,"is",sum)
