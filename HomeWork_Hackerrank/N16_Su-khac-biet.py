n = int(input())
arr =[]
for i in range(n):
    s = list(map(int, input().split()))
    arr.append(max(s))
    arr.append(min(s))

print (max(arr) - min(arr))
