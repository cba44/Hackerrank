t = int(raw_input())

for x in range(t):
    a = raw_input()
    b = raw_input()

    set1 = set(a)
    set2 = set(b)

    if not set1.intersection(set2):
        print "NO"
    else:
        print "YES"