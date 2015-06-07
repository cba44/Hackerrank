t = int(raw_input())

for x in range(t):
    n,a = map(int,raw_input().split())

    lst = list(map(int,raw_input().split()))

    count = 0

    for x1 in lst:
        if x1<1:
            count = count + 1

    if count < a:
        print "YES"
    else:
        print "NO"