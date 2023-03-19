num=int(input("please enter a num"))

list = []
newlist=[]

for i in range(1,num+1):
    newlist = []
    for j in range(1, i + 1):
        newlist.append(j*i)
    list.append(newlist)
print(list)
