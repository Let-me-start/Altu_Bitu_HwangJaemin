#빈 집합을 만들어서 케이스마다 일일이 넣고빼면 시간초과 발생
#배열+import sys

import sys

m = int(input())
s = [0]*20
all = [1]*20
for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        if s[int(command[1])-1] == 1:
            continue
        else:
            s[int(command[1])-1] =1
    elif command[0] == 'remove':
        if s[int(command[1])-1] == 0:
            continue
        else:
            s[int(command[1])-1] = 0
    elif command[0] == 'check':
        if s[int(command[1])-1] == 1:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if s[int(command[1])-1] == 1:
            s[int(command[1])-1] = 0
        else:
            s[int(command[1])-1] = 1
    elif command[0] == 'all':
        s = all
    elif command[0] == 'empty':
        s = [0]*20
