nums = [4,3,2,1]
k = 2
s=0
for i in range(len(nums)):
    f=str(bin(i))[2:]
    if f.count("1")==k:
        s=s+nums[i]
print(s)
