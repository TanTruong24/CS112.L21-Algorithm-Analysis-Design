
#Cách Đệ quay
def find_recursive(s, n, sum):
    #Cơ sở
    if (sum == 0):
        return True
    if (n == 0):
        return False

    if (s[n - 1] > sum):
        return find_recursive(s, n - 1, sum)
 
    return find_recursive(s, n-1, sum) or find_recursive(s, n-1, sum-s[n-1])

def find_DP(nums, k):
    d = {0:1}
    sums = 0
    count = 0

    for i in range(len(nums)):

        sums+= nums[i]
        
        if sums-k in d:
            count+= d[sums-k]
            
        if sums in d:
            d[sums]+=1
            
        else:
            d[sums] = 1
    
    return count

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))

    if (sum(s) % 2 != 0):
        print ("False")
    else:
        # dùng đệ quy
        print (find_recursive(s, n, sum(s)/2))

        # Dùng Quy hoach động
        if (find_DP(s, sum(s)/2) > 1):
            print ("True")
        else:
            print ("False")


"""
Vào dịp tết nguyên đán, 2 anh em nhà Tèo được mẹ cho 1 số tiền đi chơi tết, 
mẹ vừa chuẩn bị một số tiền gồm N tờ, để đảm bảo tính công bằng cho hai anh em 
thì mẹ quyết định chia só tiền đấy thành hai phần bằng nhau. 
Xác định xem mẹ có khả năng chia 2 số tiền đó thành 2 phần bằng nhau hay không?
"""

"""
Input:
5
1 2 3 4 5
Output:
False
"""


