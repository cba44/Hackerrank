def partition(ar):
    lst1 = []
    lst2 = []
    for x in range(1,len(ar)):
        if ar[0] > ar[x]:
            lst1 += [ar[x]]
        else:
            lst2 += [ar[x]]
    lst3 = lst1 + [ar[0]] + lst2
    for x in lst3:
        print x,


m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
