#declaring area
import random
from operator import truediv


def CheckR(row, col, n):
    sum = 0
    for i in range(n):
        sum += arr[row][col + i]
    return sum

def CheckD(row, col, n):
    sum = 0
    for i in range(n):
        sum += arr[row + i][col]
    return sum

def Checknxm(row, col, n, m):
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += arr[row + i][col + j]
    return sum


def MakeZeroR(row, col, n):
    for i in range(n):
        arr[row][col + i] = 0

def MakeZeroD(row, col, n):
    for i in range(n):
        arr[row + i][col] = 0

def MakeZeronxm(row, col, n, m):
    for i in range(n):
        for j in range(m):
            arr[row + i][col + j] = 0


#main area
#creating random matrix
row = int(input("row >> "))
col = int(input("col >> "))

global arr
arr = [[random.randint(1, 9) for i in range(col)] for j in range(row)]

for i in range(0, row, 1):
    for j in range(0, col, 1):
        arr[i][j] = random.randint(1, 9)
        print(f"{arr[i][j]}", end=" ")
    print()


#check with n x m form
change = True

while change != False:
    change = False

    for i in range(row):
        for j in range(col):
            """"# 1 x N form
            for n in range(2, col - j + 1):
                result = CheckR(i, j, n)
                if result == 10:
                    MakeZeroR(i, j, n)
                    change = True


            # N x 1 form
            for n in range(2, row - i + 1):
                result = CheckD(i, j, n)
                if result == 10:
                    MakeZeroD(i, j, n)
                    change = True"""
            # test: 2 x 2 form
            for n in range(1, row - i + 1):
                for m in range(1, col - j + 1):
                    if (col - 1) - j >= (n - 1) and (row - 1) - i >= (n - 1):
                        result = Checknxm(i, j, n, m)
                        if result == 10:
                            MakeZeronxm(i, j, n, m)
                            change = True
                            #print(f"2x2 form activated in [{i}][{j}]")


#making results
print()

score = 0
for i in range(row):
    for j in range(col):
        value = arr[i][j]
        print(f"{value}", end=" ")

        if(value == 0):
            score = score + 1
    print()

print(f"score is {score}")