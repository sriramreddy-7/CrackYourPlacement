with open('test.csv',"w") as file:
    file.write("Hello How are you ?")

with open(r'D:\Coding\CrackYourPlacement\DAY_5\test.txt',"r") as file:
    context=file.read()

print(context)