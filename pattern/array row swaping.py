'''swapping matrix row
Program to swape row and print new matrix  pattern below
Original matrix:
       [1, 2, 3, 4, 5]
       [6, 7, 8, 9, 10]
       [11, 12, 13, 14, 15]
       [16, 17, 18, 19, 20]
       [21, 22, 23, 24, 25]

Swape matrix:
       [1, 2, 3, 4, 5]
       [21, 22, 23, 24, 25]
       [11, 12, 13, 14, 15]
       [16, 17, 18, 19, 20]
       [6, 7, 8, 9, 10]
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
    # for i in range(N):
    #     arr[1]=arr[N-1]
#print(arr)
print()
