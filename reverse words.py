#s='sridevi engineering college'
## revering the str
## egelloc gnireenigne iveidirs

def check(s):
    s=s.split()
    s=list(reversed(s)) #s because reverse list
    print(s)
    #rev=''
    for i in s:
        rev=i[::-1] # characters of reverse list
        print(rev,end=' ')
        #rev=i+rev
    #print(type(rev))
    return rev
s='sridevi engineering college'
#print(check(s))
check(s)
