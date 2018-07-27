n=input("enter n value :")
n=int(n)
x=0
y=n
a=0
b=0
c=0

while n!=0:
    if x<n:
        x=n
    if n>0 and n<10:
        a+=1
    if n>10 and n<100:
        b+=1
    if n>100 and n<1000:
        c+=1
    
    print ("Enter another number")
    n=input("enter n value :")
    n=int(n)

    if n>=x:
        x=n
    if n==0:
        break
    if n<=y:
        y=n    
print(x, "is largest number")
print(y, "is smallest number")
print(a, ": number of single digit numbers")
print(b, ": number of two digit numbers")
print(c, ": number of three digit numbers")
adding a line
