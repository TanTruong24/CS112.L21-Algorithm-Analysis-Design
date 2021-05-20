def MaxSubarray(t, res):
    for j in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        max1 = -1000    # the maximum subarray sums
        max2 = -1000    # the maximum subsequence sums
        CheckPositive = False

        #in oder max2 -> add up all positive numbers 
        #If there are no positive numbers, max2 is smallest number
        for i in range(n):
            if (max2 > 0):
                CheckPositive = True
                if (s[i] > 0):
                    max2 += s[i]
            elif (max2 < 0 and s[i] > max2):
                max2 = s[i]

        # use DP find max1, if arr has least 1 positive
        if (CheckPositive):
            for i in range(1, n):
                if (s[i-1] + s[i] > 0):
                    s[i] += s[i-1]
                else:
                    s[i] = 0
        # same as max2, max1 is smallest numbers
        else:
            max1 = max2
        
        # max1 is largest value in arr
        for i in range(n):
            if (s[i] > max1):
                max1 = s[i]

        # add each case to res
        res.append(max1)
        res.append(max2)


t = int(input())
res = []
j = 0
MaxSubarray(t, res)
for i in range(t):
    print (res[j], res[j+1])
    j += 2  # next case


