t = int(raw_input())

for x in range(t):
    n = raw_input()
    lst = map(int,raw_input().split())

    s1 = 0
    s2 = 0

    for y in lst:
        s1 += y
        if y > 0:
            s2 += y

    if min(lst) < 0:
        s1 -= min(lst)

    print "%d %d" %(s1,s2)