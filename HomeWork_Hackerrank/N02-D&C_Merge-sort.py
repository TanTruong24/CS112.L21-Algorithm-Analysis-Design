
"""
s = list(map(int, input().split()))
s.sort()
print(' '.join(str(x) for x in s))
"""

def mergeSort(s):
    if len(s) > 1:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            s[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            s[k] = right[j]
            j += 1
            k += 1


s = list(map(int, input().split()))
mergeSort(s)
print(' '.join(str(x) for x in s))

