'''Program to print pattern below
       12345
       678910
       1112131415
       1617181920
       2122232425
if (N=5) is given by user
here one loop of i is running for row in range(0,N)
and 1 loop of j in running in range(0,N) to print (i*N+j+1) '''
N= int(input("input:"))
for i in range(0,N):
        for j in range(0,N):
            print(i*N+j+1,end="")
        print()