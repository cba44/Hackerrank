t = int(raw_input())

for x in range(t):
    a = int(raw_input())
    b = bin(a)
    c = b[2:].zfill(32)

    num = "0b"

    for x1 in c:
        if x1 == "1":
            num += "0"
        else:
            num += "1"

    print int(num,2)