list=[8,10,6,2,4]

n=len(list)
iter=n
count=0
for i in range(n):
    for j in range(n-1-i):
        count+=1
        if list[j+1]<list[j]:

            list[j],list[j+1]=list[j+1],list[j]
    iter=iter-1

print(list)
print(count)