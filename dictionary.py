#dictionary
#it is  mutable data structure
'''syntax:
    dic_name={'key1':value,'key2':value,....'keyn':value}
'''
'''
menu={
    'chckn_bryn':555,'butter_chckn':450,'tandoori_chckn':555,'Juicy_mandi':800
    }
print(menu)
'''




'''
menu={
    'chckn_bryn':555,'butter_chckn':450,'tandoori_chckn':555,'Juicy_mandi':800
    }
menu['fruit_salad']=100#to add
print(menu)
'''




'''
menu={
    'chckn_bryn':555,'butter_chckn':450,'tandoori_chckn':555,'Juicy_mandi':800
    }
print(menu)
menu.pop('tandoori_chckn')#to delete
print(menu)
'''




'''
menu={
    'chckn_bryn':555,'butter_chckn':450,'tandoori_chckn':555,'Juicy_mandi':800
    }
menu['chckn_bryn']=600#update
print(menu)
'''


'''
menu={
    'chckn_bryn':555,'butter_chckn':450,'tandoori_chckn':555,'Juicy_mandi':800
    }
print(menu.keys()) #to print keys(rates)
print(menu)
'''





''' to print values
menu={
    'chckn_bryn':555,'butter_chckn':450,'tandoori_chckn':555,'Juicy_mandi':800
    }
print(menu.values())
for k,v in menu.items():
    print(k,'->',v)
'''


'''
cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
    }#keys are ages of voters and values are votes
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
    }
countc,countb=0,0
for k,v in cong.items():
    if k>=18:
        countc+=v#41

for k,v in bjp.items():
    if k>=18:
        countb+=v#35
if countb>countc:
    print("bjp won by",countb-countc,"votes")
else:
    print("cong won by",countc-countb,"votes")
'''




'''
cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
    }#keys are ages of voters and values are votes
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
    }
countc,countb=0,0
for k,v in cong.items():
    if k>=18:
        countc+=v#41

for k,v in bjp.items():
    if k>=18:
        countb+=v#35
if countc>countb:
    print("cong won by",countc-countb,"votes")
else:
    print("bjp won by",countb-countc,"votes")
'''

'''
cong={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
    }#keys are ages of voters and values are votes
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
    }
cong_sum=0
bjp_sum=0
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
for age,votes in bjp.items():
    if age>=18:
        bjp_sum+=votes
diff=abs(cong_sum-bjp_sum)
if cong_sum>bjp_sum:
    print("cong win: ",diff)
else:
    print("bjp win:",diff)
    
'''        
        
        


