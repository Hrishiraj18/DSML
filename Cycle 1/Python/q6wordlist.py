name=input('Enter the string ')
n=int(input("Enter the number of items"))
wordlist=[]
print('Enter item')
for item in range(n):
    word=input()
    wordlist.append(word)

def findwordlist(wordlist,name):

    count =0
    indexlist=[]

    for i in wordlist:
        if i.find(name)!=-1:
            count+=1
            indexlist.append(i.find(name))
    
    return(count,indexlist)
result=findwordlist(wordlist,name)
print(result)


