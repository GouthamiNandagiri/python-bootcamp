'''
*
**
***
****
*****
'''
'''
ch='*'
for i in range(1,6):
    print(ch*i)
'''
'''
n=5
for i in range(1,n+1):
    print('*'*i)
'''
'''
*****
****
***
**
*
n=5
for i in range(n,0,-1):
  print('*'*i)
  ----------------------
'''

'''*     *
      *
   *     *'''

'''
n=5
for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
  ------ ---------------------------------
'''

'''
****
*  *
*  *
****
'''
'''n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
'''





    

