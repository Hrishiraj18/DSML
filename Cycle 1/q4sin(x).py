import math
x=float(input("Enter the radian"))
n=int(input("Enter the number"))
def sum_sin(x,n):
    sum_sin=0
    for i in range(0,n):
        sign=(-1)**i
        p=(x*math.pi)/180
        sum_sin+=((p**(2*i+1))/math.factorial(2*i+1))*sign
    return sum_sin
result=sum_sin(x,n)
print("The result is ",result)
