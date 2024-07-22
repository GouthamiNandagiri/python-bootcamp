'''
S='1C0C1C1A0B1'
A  &
B  |
C  ^
'''

#s='1C0C1C1A0B1'
s='1A1B1C0C1B0A1'
res=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='A':
        res=res&int(s[i+1])
    elif s[i]=='B':
        res=res|int(s[i+1])
    else:
        res=res^int(s[i+1])
print(res)
