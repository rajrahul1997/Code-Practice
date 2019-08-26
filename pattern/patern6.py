'''Program to print pattern below
      55555
      4444
      333
      22
      1
if (N=5) is given by user
here one loop of i is running for row in range(0,N+1) and another loop of j in range(0,N-i) to print(N-i)'''
N= int(input("input:"))
for i in range(0,N+1):
    for j in range(0,N-i):
        print(N-i,end ="")
    print()
