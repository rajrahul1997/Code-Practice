'''Program to print pattern below
      1
      22
      333
      4444
      55555
if (N=5) is given by user
here one loop of i is running for row in range(0,N+1) and another loop of j in range(0,i) to print(i)'''
N= int(input("input:"))
for i in range(0,N+1):
    for j in range(0,i):
        print(i,end ="")
    print()
