
a=[1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,1,1]
count=0
for i in range(35):
    if not count==4:
        if a[i]==0:
            print(" ",end="")
        else:
            print("#",end="")
        count+=1
    else:
        if a[i]==0:
            print(" ",end="\n")
        else:
            print("#",end="\n")
        count=0
    

