#candles=[3,7,1,5,4,7]
#print(candles.count(max(candles)))
candles=[3,7,1,5,4,7]
#candles=[3,7,1,5,4,8]#op:1
max=candles[0]
count=0
for i in candles:
    if i>max:
        max=i
for i  in candles:
    if max==i:
        count+=1
print(count)

    
