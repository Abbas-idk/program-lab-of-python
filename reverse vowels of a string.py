"""reverse vowels of a string"""
s=input('enter string')
l=list(s)
i=0
j=len(s)-1
s1='aeiouAEIOU'
for k in range(len(l)):
    while l[i] not in s1:
        i+=1
    while l[j] not in s1:
        j-=1
    l[i],l[j]=l[j],l[i]
    t=str(l)
print(t)  
 
