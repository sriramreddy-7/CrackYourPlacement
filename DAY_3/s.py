s = "a-bC-dEf-ghIj"
r=[i for i in s]
i=0
j=len(s)-1
while i<=j:
    if r[i].isalpha() and r[j].isalpha():
        r[i],r[j]=r[j],r[i]
        i=i+1
        j=j-1
    elif r[i].isalpha()==False and r[j].isalpha():
        i=i+1
    elif r[i].isalpha() and r[j].isalpha()==False:
        j=j-1
    else:
        i=i+1
        j=j-1
print("".join(r))