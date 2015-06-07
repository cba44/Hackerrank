n = int(raw_input())

lst = map(int,raw_input().split())

lst.sort()

k = 0

for x in range(0,n-1,2):
    if lst[x] != lst[x+1]:
        print lst[x]
        k = 1
        break

if k == 0:
    print lst[n-1]