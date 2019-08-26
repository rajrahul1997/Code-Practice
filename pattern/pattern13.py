'''Program to print pattern below
       12345
       1112131415
       2122232425
       1617181920
       678910
if (N=5) is given by user'''
N= int(input("input:"))
for i in range(0,N):
    if (i % 2 == 0):
        for j in range(0, N):
            print(i*N+j+1,end="")
        print()
for i in range(0,N):
    if (i % 2 != 0):
        for j in range(0, N):
            print(i * N + j + 1, end="")
        print()