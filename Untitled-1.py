def simpleinterest(p,t,r):
    return(p*t*r)/100
p=float(input("Ente the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input(("Enter the time of years:  "))
print("Simple interest:", simpleinterest(p,r,t))