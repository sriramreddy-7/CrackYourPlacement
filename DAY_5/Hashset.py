ransomNote = "aa"
magazine = "aab"

def fun(ransomNote,magazine):
    r = "".join(set(ransomNote))
    for i in r:
        print(type(i))
        if i in magazine:
            if magazine.count(i) < ransomNote.count(i):
                print(1)
                return False
        else:
            print(i,2)
        return False
    return True


print(fun(ransomNote,magazine))
