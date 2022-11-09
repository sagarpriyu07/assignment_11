#print sum of first n odd natural numbers
n=int(input("Enter any number="))
sum=0
for i in range(1,n*2,2):
    sum=sum+i
print("Sum of first",n,"odd natural number is",sum)