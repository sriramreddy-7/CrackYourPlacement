arr=[10,100,1000,10000]
d={}
for i in arr:
    r=str(bin(i))[2:]
    c=r.count("1")
    if c not in d:
        e=[]
        e.append(i)
        d[c]=e
    else:
        x=d[c]
        x.append(i)
        d[c]=x
dic=dict(sorted(d.items()))
result=[]
for k,v in d.items():
    v.sort()
    result.extend(v)
print(result)