#swap varaiable without temporary variable
'''a=4
b=5
a,b=b,a
print(a,b)
'''
'''
a=10
b=20
a=a+b#10+20=30
b=a-b#30-20-=10
a=a-b#30-10=20
print(a,b)
'''


'''xor'''

a,b=5,6
a=a^b
b=a^b
a=a^b
print(a,b)
