s = int(raw_input())

lst = map(int, raw_input().split())


def insSort(lst):
    count = 0
    for x in range(1, len(lst)):
        if lst[x] < lst[x - 1]:
            tmp = lst[x]
            for x1 in range(x, 0, -1):
                if lst[x1] < lst[x1 - 1]:
                    lst[x1] = lst[x1 - 1]
                    lst[x1 - 1] = tmp
                    count += 1
    return count

print insSort(lst)