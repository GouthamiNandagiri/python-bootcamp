
'''
num=[1,2,3,4,5]
#hide 1 and do sum 14
#hide 2 and do sum 13
#hide 3 and do sum 12
#hide 4 and do sum 11
#hide 5 and do sum 10
#maximum sum=14
#minimum=10
sum=sum(num)
print((sum-min(num))-(sum-max(num)))
'''
#to get max-remove min number from total 76-2=74
#min 76-34=42
#diff=74-42=32



arr=[2,6,34,21,9,4]
arr.sort()
min_sum=sum(arr[:len(arr)-1])
max_sum=sum(arr[1:])
diff=abs(min_sum-max_sum)
print(diff)
