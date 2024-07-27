def check(s,t):
    if s == "":
        return True
    j = 0
    i=0
    while j <= len(s) - 1 and i <= len(t) - 1:
        if t[i] == s[j]:
            j = j + 1
        i = i + 1
    if len(s) == j:
        return True
    return False

s = "abc"
t = "ahbgdc"
print(check(s,t))
