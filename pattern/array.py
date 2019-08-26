'''array inside array
Program to print pattern below
       [1, 2, 3, 4, 5]
       [6, 7, 8, 9, 10]
       [11, 12, 13, 14, 15]
       [16, 17, 18, 19, 20]
       [21, 22, 23, 24, 25]

if (N=5) is given by user '''
N= int(input("input:"))
temp=[]
arr=[]
count=0
for i in range(0,N):
    for j in range(0, N):
        count=count+1
        temp.append(count)
    arr.append(temp)
    temp=[]
for i in arr:
    print(i)
print()