#print sum of cubes of n natural numbers
n=int(input("Enter any number="))
sum=0
for i in range(1,n+1):
    sum=sum+i*i*i
print("Sum of cubes of",n,"natural number is",sum)