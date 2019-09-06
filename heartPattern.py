
#heart printing program

for row in range(6): #i want 5 rows
    for col in range(7):   # i want 6 coloums

        #for first part
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col ==2 )or(row+col ==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()
