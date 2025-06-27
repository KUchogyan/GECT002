import random

#----------
"""def MakeZero(prow, pcol, direction, m, n):
    if direction == 1:
        for i in range(n):
            arr[prow][pcol + i] = 0

    if direction == 2:
        for i in range(n):
            arr[prow + i][pcol] = 0

    if direction == 3:
        for i in range(n):
            arr[prow][pcol - i] = 0

    if direction == 4:
        for i in range(n):
            arr[prow - i][pcol] = 0



def Count0(prow, pcol, direction, n):
    count = 0
    if direction == 1:
        for i in range(n):
            if arr[prow][pcol + i] == 0:
                count = count + 1

    if direction == 2:
        for i in range(n):
            if arr[prow + i][pcol] == 0:
                count = count + 1

    if direction == 3:
        for i in range(n):
            if arr[prow][pcol - i] == 0:
                count = count + 1

    if direction == 4:
        for i in range(n):
            if arr[prow - i][pcol] == 0:
                count = count + 1

    return count

def Check1xN(prow, pcol, direction, n):
    sum = 0

    if direction == 1:
        for i in range(n):
            sum += arr[prow][pcol + i]

    if direction == 2:
        for i in range(n):
            sum += arr[prow + i][pcol]

    if direction == 3:
        for i in range(n):
            sum += arr[prow][pcol - i]

    if direction == 4:
        for i in range(n):
            sum += arr[prow - i][pcol]

    return sum

def Check2x2(row, col):
    sum = arr[row][col] + arr[row][col + 1] + arr[row + 1][col] + arr[row + 1][col + 1]
    return sum"""
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

"""def Count_0(row, col, n):
    sum = 0
    for i in range(n):
        if arr[row][col + i] == 0:
            sum = sum + 1

    return sum"""

def MakeZeroR(row, col, n):
    for i in range(n):
        arr[row][col + i] = 0

def MakeZeroD(row, col, n):
    for i in range(n):
        arr[row + i][col] = 0
#----------

row = int(input("row >> "))
col = int(input("col >> "))

global arr
arr = [[random.randint(1, 9) for i in range(col)] for j in range(row)]

for i in range(0, row, 1):
    for j in range(0, col, 1):
        arr[i][j] = random.randint(1, 9)
        print(f"{arr[i][j]}", end=" ")
    print()

#up = 0; down = 0; right = 0; left = 0
"""s_index = 0
s_x = []
s_y = []
s_d = []
s_size_n = []
s_size_m = []"""
'''while did_change != 0:
    did_change = 0
    #starting computing like matrix > ij, i(j+2), ...
    for i in range(0, row, 1):
        for j in range(i % 2, col, 2):
            #set limits
            up = i
            down = row - i - 1
            right = col - j - 1
            left = j

            # (1 x n) check
            for n in range(2, 11):
                for k in range(1, 5):   #check 4 directions

                    #if range is bigger than matrix' size, end the loop
                    match k:
                        case 1:
                            if(n - 1 > right): continue
                        case 2:
                            if(n - 1 > down): continue
                        case 3:
                            if(n - 1 > left): continue
                        case 4:
                            if(n - 1 > up): continue


                    tempsum = Check1xN(i, j, k, n)

                    #end the loop if sum of 1xn is bigger than 10
                    if(tempsum > 10):
                        #print("out", end="->")
                        continue

                    if tempsum == 10:
                        """s_x.append(i)
                        s_y.append(j)
                        s_d.append(k)
                        s_size_m.append(1)
                        s_size_n.append(n)
                        s_index += 1"""
                        #test
                        #print(f"{i} {j} {k} 1 {n} : {tempsum}")

                        score += n - Count0(i, j, k, n)

                        MakeZero(i, j, k, 1, n)
                        did_change = 1

                    #checking the detecting code
                    #print(f"{i} {j} {k} : {tempsum}")'''


#check with nxm form
for i in range(row):
    for j in range(col):
        # 1 x N form
        for n in range(2, col - j + 1):
            result = CheckR(i, j, n)
            if result == 10:
                MakeZeroR(i, j, n)
                continue

        # N x 1 form
        for n in range(2, row - i + 1):
            result = CheckD(i, j, n)
            if result == 10:
                MakeZeroD(i, j, n)




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