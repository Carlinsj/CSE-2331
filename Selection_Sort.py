#Selection Sort
a=[5,4,2,10,14,3,1]
for i in range(len(a)-1):
    ind=i
    for j in range(i+1, len(a)):
        if a[ind]> a[j]:
            ind=j
    a[i],a[ind]=a[ind],a[i]
for i in range(len(a)):
    print(a[i],end=", ")
    