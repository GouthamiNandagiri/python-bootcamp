Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##n=5
##0 1 1 2 3

#def check(n):
   # first=0
   # second=1
   # print(first,second,end=' ')
    #count=2
    #while count<=n:
       # third=first+second
       # print(third,end=' ')
        #first=second
       # second=third
       # count+=1
#check(5) #10,5,20,13

       


##sum of digits until we get a single digit
       
##n=12345
##f=123
##s=45
##output:54321


       
###function calling another function

#arr=[5,9,12,6,17,3]

#def check(ele):
 #   return ele%2==0
#
    
#def increment(arr):
 #   count=0
  #  for i in arr:
   #     if check(i):
    #        print(i) #if we put this in comment the output will be only 2
     #       count+=1
    #return count
#arr=[5,9,12,6,17,3]
#print(increment(arr))
    


#another example palindrome 


def check(ele):
    ele=str(ele)
    return ele==ele[::-1]

    
def increment(arr):
    count=0
    for ele in arr:
        if check(ele):
            print(ele) #if we put this in comment the output will be only 2
            count+=1
    return count
arr=[21,78,212,782,1001]
print(increment(arr))
