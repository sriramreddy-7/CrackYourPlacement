arr=[1,0,1,1,1,0,0]
_max=-1
for i in range(len(arr)):
    for j in range(i,len(arr)):
        r=[]
        r=arr[i:j+1]
        if r.count(0)==r.count(1) and len(r)>_max:
            _max=len(r)
print(_max)