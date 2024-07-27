s = "abcd"
k = 2
i=0
t=""
while i<=len(s)-1:
    if len(s[i:i+k])==k:
        t+=s[i:i+k][::-1]
        i=i+k
    else:
        t+=s[i:i+k]
        i=i+1
print(t)



