string=input("Enter the text ")
vowel_list=['a','e','i','o','u','A','E','I','O','U']
for i in string:
    if i in vowel_list:
       string=string.replace(i,"*")
print("The string after replacing is ",string)