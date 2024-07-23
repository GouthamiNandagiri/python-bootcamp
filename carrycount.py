'''
  1 1
n1=288
n2=594
------
   882
   count no.of  carry?
'''

n1=288
n2=594
s1=str(n1)
s2=str(n2)
c=0
for i in range(len(s1)-1,-1,-1):
    if int(s1[i])+int(s2[i])>=10:
        c+=1
print(c)


'''
n1=2894
n2=5786
carry=0
count=0
while n1>0 and n2>0:
    rem1=n1%10
    rem2=n2%10
    sum=rem1+rem2+carry
    if(sum>9):
        carry=1
        count+=1
    else:
        carry=0
    n1=n1//10
    n2=n2//10
print('count',count)
'''
