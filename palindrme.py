##with sciling
s='malayalam'
print(s[::3])

s='python'
print(s[::4])



##without sciling
s='python'
s1=''
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
    #print(s1)
if(s1==s):
    print('Palindrome')
else:
        print('Not')
