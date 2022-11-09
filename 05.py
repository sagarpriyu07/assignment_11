#print sum of first n even natural numbers
n=int(input("Enter any number="))
sum=0
for i in range(2,n*2+1,2):
    sum=sum+i
print("Sum of first",n,"even natural number is",sum)