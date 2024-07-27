s = "abcba"
target = "abc"
def fun(s,target):
    f=set(target)
    d={}
    for i in target:
        d[i]=s.count(i)
    print(len(f),len(d))
    if len(f)!=len(d):
        return 0
    _min=d.get(target[0])
    for k,v in d.items():
        if v<_min:
            _min=v
    print(_min,len(target),_min//len(target))
    return len(target)//_min
print(fun(s,target))


