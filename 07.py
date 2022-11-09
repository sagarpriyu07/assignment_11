#print no of dighit in any number
'''x=input("Enter any number=")
count=len(x)'''
n=int(input("Enter any number="))
x=n
count =0
while n!=0:
    n=n//10
    count+=1
print(count,"digit are present in",x)