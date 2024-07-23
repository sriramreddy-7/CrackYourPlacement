arr = [1,4,2,5,3]
s=0
for i in range(len(arr)):
    if i%2!=0:
        for j in range(len(arr)):
            if i==len(arr[j:j+i]):
                s=s+sum(arr[j:j+i])
if len(arr)%2!=0:
    s=s+sum(arr)
print(s)


