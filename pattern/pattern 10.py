'''Program to print pattern below
       10001
       1001
       101
       11
       1
if (N=5) is given by user
here one loop of i is running for row in range(0,N)
and 1 loop of j in running ,one in range(0,N-i) and checking condition for value of j
if(j == 0 or j == N-i-1) print(1) else print(0)'''

N= int(input("input:"))
for i in range(0,N):
    for j in range(0,N-i):
        if (j == 0 or j == N-i-1):
            print('1',end ="")
        else:
            print('0',end ="")
    print()
