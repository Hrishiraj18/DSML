string=input("Enter the text ")
count_upper=0
count_lower=0
for i in string:
    if(i.islower()):
        count_lower+=1
    elif(i.isupper()):
        count_upper+=1
print("The uppercase count is ",count_upper)
print("The lowercase count is ",count_lower)