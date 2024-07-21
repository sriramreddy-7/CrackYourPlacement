# a = "1010"
# b = "1011"
# ba=int(a,2)
# bb=int(b,2)
# print(bin(ba+bb))
n=6
x=78
arr= [5, 20, 3, 2, 5, 80]
for i in arr:
    print(x-i)
    if (x-i) in arr:
        print(1)
else:
    print(-1)