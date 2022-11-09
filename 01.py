#print sum of n natural numbers
n=int(input("Enter any number="))
sum=0
'''for i in range(1,n+1):
    sum=sum+i'''
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of",n,"natural number is",sum)