def MaxSubarray(t, res):
    for j in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        max1 = -1000    
        max2 = -1000    
        CheckPositive = False

        for i in range(n):
            if (max2 > 0):
                CheckPositive = True
                if (s[i] > 0):
                    max2 += s[i]
            elif (max2 < 0 and s[i] > max2):
                max2 = s[i]


        if (CheckPositive):
            for i in range(1, n):
                if (s[i-1] + s[i] > 0):
                    s[i] += s[i-1]
                else:
                    s[i] = 0

        else:
            max1 = max2

        for i in range(n):
            if (s[i] > max1):
                max1 = s[i]

        res.append(max1)
        res.append(max2)


t = int(input())
res = []
j = 0
MaxSubarray(t, res)
for i in range(t):
    print (res[j], res[j+1])
    j += 2 