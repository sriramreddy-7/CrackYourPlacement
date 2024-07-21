S = "geeksforgeeks"
d={}
for i in S:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if v>1:
        print(f"{k}:count-{v}")
        

