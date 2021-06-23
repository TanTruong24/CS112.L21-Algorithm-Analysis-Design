def train(arr, dep, l):
    arr.sort()
    dep.sort()
    i =1
    j = 0
    count = 1
    station = 1
    while(i < l and j < l):
        if(arr[i] <= dep[j]):
            count += 1
            i += 1
        else:
            if(count > station):
                station = count
            count -= 1
            j += 1
            
        if (count > station):
            station = count

    return station


arr = list(map(int, input().split()))
dep = list(map(int, input().split()))
len_arr = len(arr)
print (train(arr, dep, len_arr))
