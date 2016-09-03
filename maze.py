#!/usr/bin/python -tt

import sys
import logging

def size(path1, path2) :

    current_x = 0
    current_y = 0
    direction = "D"
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for c in path1 :
        if c == "W" :
            if direction == "D":
                current_y = current_y - 1
                if min_y > current_y :
                    min_y = current_y
            elif direction == "U":
                current_y = current_y + 1
                if max_y < current_y :
                    max_y = current_y
            elif direction == "L":
                current_x = current_x - 1
                if min_x > current_x :
                    min_x = current_x
            elif direction == "R":
                current_x = current_x + 1
                if max_x < current_x :
                    max_x = current_x
            else :
                print "Error! Unknown Direction : %s" %(direction)

        elif c == "L" :
            if direction == "D" :
                direction = "R"
            elif direction == "U" :
                direction = "L"
            elif direction == "L" :
                direction = "D"
            elif direction == "R" :
                direction = "U"
        elif c == "R" :
            if direction == "D" :
                direction = "L"
            elif direction == "U" :
                direction = "R"
            elif direction == "L" :
                direction = "U"
            elif direction == "R" :
                direction = "D"


    exit_direction = direction
    if direction == "D" :
        direction = "U"
    elif direction == "U" :
        direction = "D"
    elif direction == "L" :
        direction = "R"
    elif direction == "R" :
        direction = "L"


    for c in path2 :
        if c == "W" :
            if direction == "D":
                current_y = current_y - 1
                if min_y > current_y :
                    min_y = current_y
            elif direction == "U":
                current_y = current_y + 1
                if max_y < current_y :
                    max_y = current_y
            elif direction == "L":
                current_x = current_x - 1
                if min_x > current_x :
                    min_x = current_x
            elif direction == "R":
                current_x = current_x + 1
                if max_x < current_x :
                    max_x = current_x
            else :
                print "Error! Unknown Direction : %s" %(direction)

        elif c == "L" :
            if direction == "D" :
                direction = "R"
            elif direction == "U" :
                direction = "L"
            elif direction == "L" :
                direction = "D"
            elif direction == "R" :
                direction = "U"
        elif c == "R" :
            if direction == "D" :
                direction = "L"
            elif direction == "U" :
                direction = "R"
            elif direction == "L" :
                direction = "U"
            elif direction == "R" :
                direction = "D"

    if exit_direction == "D" :
        column = max_x - min_x + 1
        row = max_y - min_y - 1
        corner_x = min_x
        corner_y = min_y + 1
    elif exit_direction == "U" :
        column = max_x - min_x + 1
        row = max_y - min_y
        corner_x = min_x
        corner_y = min_y
    elif exit_direction == "L" :
        column = max_x - min_x
        row = max_y - min_y
        corner_x = min_x + 1
        corner_y = min_y
    elif exit_direction == "R" :
        column = max_x - min_x
        row = max_y - min_y
        corner_x = min_x
        corner_y = min_y
    start_x = - corner_x
    start_y = - corner_y

    logging.debug(" min_x = %d , max_x = %d , min_y = %d , max_y = %d " %(min_x, max_x, min_y , max_y))
    return (column, row, start_x, start_y)


def making_list (column, row) :
    a = []
    for j in range(0, column):
        b = []
        for i in range(0, row):
            b.append("U")
        a.append(b)
    return a

def direction_change (cur_dir, path):
    if cur_dir == "D":
        if path == "R":
            new_dir = "L"
        elif path == "L":
            new_dir = "R" 
    elif cur_dir == "U":
        if path == "R":
            new_dir = "R"
        elif path == "L":
            new_dir = "L" 
    elif cur_dir == "R":
        if path == "R":
            new_dir = "D"
        elif path == "L":
            new_dir = "U" 
    elif cur_dir == "L":
        if path == "R":
            new_dir = "U"
        elif path == "L":
            new_dir = "D" 
    return new_dir

def save_data (path, current_x, current_y, direction, N, S, W, E) :

    logging.debug(current_x)
    logging.debug(current_y)
    logging.debug(N)
    logging.debug(direction)

    if direction == "D":
        current_y = current_y - 1
        N[current_x][current_y] = 1
    elif direction == "U":
        current_y = current_y + 1
        S[current_x][current_y] = 1
    elif direction == "L":
        current_x = current_x - 1
        E[current_x][current_y] = 1
    elif direction == "R":
        current_x = current_x + 1
        W[current_x][current_y] = 1

    for c in path[1:len(path)-1]:
        if c == "W" :
            if direction == "D":
                S[current_x][current_y] = 1
                if E[current_x][current_y] == "U":
                    E[current_x][current_y] = 0
                current_y = current_y - 1
                N[current_x][current_y] = 1
            elif direction == "U":
                N[current_x][current_y] = 1
                if W[current_x][current_y] == "U":
                    W[current_x][current_y] = 0
                current_y = current_y + 1
                S[current_x][current_y] = 1
            elif direction == "L":
                W[current_x][current_y] = 1
                if S[current_x][current_y] == "U":
                    S[current_x][current_y] = 0
                current_x = current_x - 1
                E[current_x][current_y] = 1
            elif direction == "R":
                E[current_x][current_y] = 1
                if N[current_x][current_y] == "U":
                    N[current_x][current_y] = 0
                current_x = current_x + 1
                W[current_x][current_y] = 1
        elif c == "R" :
            if direction == "D":
                if S[current_x][current_y] == 1:
                    logging.error("oops! my assumption2 is wrong!")
                S[current_x][current_y] = 0
            elif direction == "U":
                if N[current_x][current_y] == 1:
                    logging.error("oops! my assumption2 is wrong!")
                N[current_x][current_y] = 0
            elif direction == "L":
                if W[current_x][current_y] == 1:
                    logging.error("oops! my assumption2 is wrong!")
                W[current_x][current_y] = 0
            elif direction == "R":
                if E[current_x][current_y] == 1:
                    logging.error("oops! my assumption2 is wrong!")
                E[current_x][current_y] = 0
            direction = direction_change(direction, c)
        elif c == "L":
            direction = direction_change(direction, c)


    if direction == "D":
        S[current_x][current_y] = 1
        current_y = current_y - 1
    elif direction == "U":
        N[current_x][current_y] = 1
        current_y = current_y + 1
    elif direction == "L":
        W[current_x][current_y] = 1
        current_x = current_x - 1
    elif direction == "R":
        E[current_x][current_y] = 1
        current_x = current_x + 1

    return [current_x, current_y, direction]


#logging.basicConfig(level=logging.DEBUG)

count = input()

i = 0

while i < count:
    i = i + 1
    line = sys.stdin.readline()
    words = line.split()

    if len(words) != 2:
        print "error: invalid input %s" % (line)

    maze_size = size(words[0], words[1])
    print "Case #%d:" %(i)

    start_x = maze_size[2]
    start_y = maze_size[3]
    column = maze_size[0]
    row = maze_size[1]

    N = making_list(column,row)
    S = making_list(column,row)
    W = making_list(column,row)
    E = making_list(column,row)

    info = save_data(words[0], start_x, start_y, "D", N, S, W, E)
    if info[2] == "D" :
        info[2] = "U"
    elif info[2] == "U" :
        info[2] = "D"
    elif info[2] == "L" :
        info[2] = "R"
    elif info[2] == "R" :
        info[2] = "L"
    
    save_data(words[1], info[0], info[1], info[2], N, S, W, E)

    j = 0
    while j < column-1:
        k = 0
        while k < row:
            if E[j][k] == 1 or W[j+1][k] == 1:
                E[j][k] = 1
                W[j+1][k] = 1
            elif E[j][k] == 0 or W[j+1][k] == 0:
                E[j][k] = 0
                W[j+1][k] = 0
            k = k +1
        j = j +1


    l = 0
    while l < column:
        m = 0
        while m < row-1:
            if N[l][m] == 1 or S[l][m+1] == 1:
                N[l][m] = 1
                S[l][m+1] = 1
            elif N[l][m] == 0 or S[l][m+1] == 0:
                N[l][m] = 0
                S[l][m+1] = 0
            m = m + 1
        l = l + 1


    n = 0
    while n < column:
        N[n][row-1] = 0
        S[n][0] = 0
        n = n + 1

    p = 0
    while p < row:
        W[0][p] = 0
        E[column-1][p] = 0
        p = p +1


    N[start_x][start_y - 1] = 1
    if info[2] == "U":
        S[info[0]][info[1]+1] = 1
    elif info[2] == "D":
        N[info[0]][info[1]-1] = 1
    elif info[2] == "L":
        E[info[0]-1][info[1]] = 1
    elif info[2] == "R":
        W[info[0]+1][info[1]] = 1
    

    for x in range(column):
        for y in range(row):
            if N[x][y] == "U": N[x][y] = 0
            if S[x][y] == "U": S[x][y] = 0
            if W[x][y] == "U": W[x][y] = 0
            if E[x][y] == "U": E[x][y] = 0

    logging.debug(N)
    logging.debug(S)
    logging.debug(W)
    logging.debug(E)


    result = making_list(column,row)

    q = 0
    while q < column:
        r = 0
        while r < row:
            if E[q][r] == 0:
                if W[q][r] == 0:
                    if S[q][r] == 0:
                        result[q][r] = 1
                    else:
                        if N[q][r] == 0:
                            result[q][r] = 2
                        else:
                            result[q][r] = 3
                else:
                    if S[q][r] == 0:
                        if N[q][r] == 0:
                            result[q][r] = 4
                        else:
                            result[q][r] = 5
                    else:
                        if N[q][r] == 0:
                            result[q][r] = 6
                        else:
                            result[q][r] = 7
            else:
                if W[q][r] == 0:
                    if S[q][r] == 0:
                        if N[q][r] == 0:
                            result[q][r] = 8
                        else:
                            result[q][r] = 9
                    else:
                        if N[q][r] == 0:
                            result[q][r] = "a"
                        else:
                            result[q][r] = "b"
                else:
                    if S[q][r] == 0:
                        if N[q][r] == 0:
                            result[q][r] = "c"
                        else:
                            result[q][r] = "d"
                    else:
                        if N[q][r] == 0:
                            result[q][r] = "e"
                        else:
                            result[q][r] = "f"
            r = r + 1
        q = q + 1


    logging.debug(result)


    s = row
    while s > 0 :
        s = s - 1
        t = 0
        while t < column :
            sys.stdout.write(str(result[t][s]))
            t = t + 1
        print ""
     
