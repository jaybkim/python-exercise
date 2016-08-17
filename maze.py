#!/usr/bin/python -tt

import sys

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

    print " min_x = %d , max_x = %d , min_y = %d , max_y = %d " %(min_x, max_x, min_y , max_y)
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

    print current_x
    print current_y
    print N
    print direction

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
                current_y = current_y - 1
                N[current_x][current_y] = 1
            elif direction == "U":
                N[current_x][current_y] = 1
                current_y = current_y + 1
                S[current_x][current_y] = 1
            elif direction == "L":
                W[current_x][current_y] = 1
                current_x = current_x - 1
                E[current_x][current_y] = 1
            elif direction == "R":
                E[current_x][current_y] = 1
                current_x = current_x + 1
                W[current_x][current_y] = 1
        else :
            if direction == "D":
                S[current_x][current_y] = 0
            elif direction == "U":
                N[current_x][current_y] = 0
            elif direction == "L":
                W[current_x][current_y] = 0
            elif direction == "R":
                E[current_x][current_y] = 0
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

N = input()

i = 0

while i < N:
    i = i + 1
    line = sys.stdin.readline()
    words = line.split()

    if len(words) != 2:
        print "error: invalid input %s" % (line)

    maze_size = size(words[0], words[1])
    print "Case #%d: %d * %d" %(i, maze_size[0] , maze_size[1] )

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
    
    info = save_data(words[1], info[0], info[1], info[2], N, S, W, E)

    print N
    print S
    print W
    print E

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

    print N
    print S
    print W
    print E    
