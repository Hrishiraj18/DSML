number=int(input("Enter a Number"))
temp=number
rev=0
sum=0
while(number):
    remainder=number%10;
    sum+=remainder
    rev=rev*10+remainder
    number//=10
print("The reversal of the number is ",rev)
print("The sum of the digits is ",sum)