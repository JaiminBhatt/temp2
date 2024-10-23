def getinterest(p,r,n):
    SI=(p*r*n)/100
    return SI

principal=int(input("Enter the amount= "))
rate=float(input("enter the rate= "))
time=int(input("enter the no of years= "))
ans=getinterest(principal,rate,time)

print("Simple interest = ",ans)
