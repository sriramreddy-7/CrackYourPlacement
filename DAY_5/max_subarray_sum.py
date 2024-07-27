arr=[1,2,3,4,5,6,7,8,9]
k=3
_sum=-1
for i in range(len(arr)-k+1):
    if _sum<sum(arr[i:i+k]):
        _sum=sum(arr[i:i+k])

print(_sum)
