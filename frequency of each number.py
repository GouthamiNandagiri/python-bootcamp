arr=[1,3,6,2,5,3,7,5,1]
#count the frequency of each number
'''
1:2
3:2
6:1
2:1
5:2
7:1
'''
'''
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1

print(d)'''

#op:{1:2,3:2,6:1,2:1,5:2,7:1}


#print unique number
arr=[1,3,6,2,5,3,7,5,1]
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
for num,count in  d.items():
   # if count==1:#unique#6 2 7
     
    if count>1:#duplicate#1 3 5
        print(num)



 
