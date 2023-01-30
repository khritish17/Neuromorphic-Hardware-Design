import numpy as np 

a=np.ndarray((3,3))
a[0][0]=1
a[0][1]=2
a[0][2]=3
a[1][0]=4
a[1][1]=5
a[1][2]=6
a[2][0]=7
a[2][1]=8
a[2][2]=9
print(a)
print(a[:,0:]) #a[:horizontal axis,:vertical]