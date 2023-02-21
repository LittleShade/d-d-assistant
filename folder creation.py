import os

pos=os.getcwd()
newDir = pos + "\\"+str(input("input new campaign"))
os.mkdir(newDir)
print(pos)

x=os.listdir(pos)
print(x)