#quick sort

def parti(a,start,end,rev):
    p=end
    p1=start-1
    if rev==0:
        for i in range(start,end):
            if a[i]<=a[p]:
                p1+=1
                a[i],a[p1]=a[p1],a[i]
        a[p1+1],a[p]=a[p],a[p1+1]
    elif rev==1:
        for i in range(start,end):
            if a[i]>=a[p]:
                p1+=1
                a[i],a[p1]=a[p1],a[i]
        a[p1+1],a[p]=a[p],a[p1+1]
    else:
        print('for ascend r=0, for desccend r=1')
    return p1+1
def sorte(a,start,end,rev):
    if start<end:
        pi=parti(a,start,end,rev)
        sorte(a,start,pi-1,rev)
        sorte(a,pi+1,end,rev)
ls=['sat','cat','mat','bat']
r=0
sorte(ls,0,len(ls)-1,r)
print(ls)