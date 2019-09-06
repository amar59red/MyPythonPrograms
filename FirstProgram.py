# Patterns printing

#----------------
# *
# **
# ***
# *****


def spaces ():
    for i in range(2):
        print()

for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()

spaces()

# #opposite of above
# # ****
# # ***
# # **
# # *
n= int(input("enter the number of:- "))
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
