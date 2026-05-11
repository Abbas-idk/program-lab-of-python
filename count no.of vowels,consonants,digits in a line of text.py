s=input('enter line of text')
cons=digits=vowels=0
for ch in s:
    if ch.lower() in 'aeiou':
        vowels+=1
    elif ch.isalpha():
        cons+=1
    elif ch.isdigit():
        digits+=1
print('vowels:{}\nconsonants:{}\ndigits:{}'.format(vowels,cons,digits))
