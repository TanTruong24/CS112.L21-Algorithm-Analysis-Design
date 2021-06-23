def luckBalance(n, k, lst):

    x = lst

    x.sort(key=lambda x: x[0])
    x = x[::-1]
    s = 0
    for i in range(n):
        if x[i][1] == 0:
            s += x[i][0]
        else:
            if k != 0:
                s += x[i][0]
                k -= 1
            else:
                s -= x[i][0]
    return s

n, k = map(int, input().split())
lst = []
for i in range(n):
    l = list(map(int, input().split()))
    lst.append(l)

print (luckBalance(n, k, lst))
