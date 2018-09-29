#!/usr/bin/python3
try:
    x = input()
    count = dict()
    ele = []
    for i in x.split(' ') :
        if i in count:
            count[i] = count[i] + 1
        else :
            count[i] = 1
            ele.append(i)
    for i in range(len(ele)):
        print(ele[i], i, count[ele[i]])

except EOFError:
    exit()
