''''
*
 * *
  * * *
   * * * *
    * * * * *
   * * * *
  * * *
 * *
*
Logic: run two loop of riw i.e, 1st for upper part from range(0,N+1) and print * for i no of times
2nd loop of i for lower part in range(N+1,2*N+1) and print * for j in range(N,j>=i-1,N-i)
'''
N= int(input("input:"))
for i in range(0,N+1):
    for k in range(0,i):
        print("*",end =" ")
    print()
for i in range(N+1,2*N):
    j=N
    for j in range(N,j>=i-1,N-i): #as j=N and as i increase j value should decrease
        print("*", end=" ")
    print()

