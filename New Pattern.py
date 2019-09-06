n = int(input("enter number :"))
for row in range(n):
    for col in range(n,row+1,-1):
        print(" ",end="")
    for i in range(row+1):
        print("*",end="")
    print()