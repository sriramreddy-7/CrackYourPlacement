strs = ["flower","flow","flight"]
s=strs[0]
for i in strs:
    if len(i)<len(s):
        s=""
        s=i

# def check(flag):
def fun(s,strs):
    i=0
    f=len(s)
    while i<=len(strs):
        if strs[i][:len(s)]==s:
            i+=1
            print(strs[i][:len(s)])
        else:
            print(strs[i][:len(s)],s)
            r=""
            r=s
            s=""
            s=r[:f]
            f=f-1
    return s

print(fun(s,strs))