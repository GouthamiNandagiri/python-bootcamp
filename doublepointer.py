#doublepointer
arr=[1,2,3,4,5]
k=6
count=0
f=0
last=len(arr)-1
while f<last:
    if arr[f]+arr[last]==k:
        count+=1
        f+=1
        last-=1
    elif arr[f]+arr[last]<k:
        f+=1
    else:
        last-=1
print(count)


