def check(S):
    #special_char=['!','@','#','$','%','^','&','*','`','?']
    up_c,low_c,sp_c,dig_c=0,0,0,0
    if len(S)>8:
        for i in range(len(S)):
            if S[i].isdigit():
                dig_c+=1
            elif S[i].isupper():
                up_c+=1
            elif S[i].islower():
                low_c+=1
            elif S[i].isascii():
                sp_c+=1
            else:
                break
        if dig_c>0 and up_c>0 and low_c>0 and sp_c>0:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")
string=input()
check(string)
