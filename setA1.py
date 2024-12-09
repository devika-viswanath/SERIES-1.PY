n=int(input("enter the size"))
lst=[]
for i in range(n):
    num=int(input("elements"))
    lst.append(num)
print(lst)
# lst.sort()
# print(lst)
for i in range(n):
    for j in range(i+1,n):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
