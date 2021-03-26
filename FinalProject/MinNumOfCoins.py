def findMinMoney(N):
  
	deno = [1, 2, 5, 10, 20, 50, 100] # Các mệnh giá được xét trong bài toán này
	n = len(deno)
	res = [] # list lưu trữ kết quả
	# duyệt qua tất cả mệnh giá 
	i = n - 1
	while(i >= 0):
   
		while (N >= deno[i]):
			N -= deno[i]
			res.append(deno[i])
   
		i -= 1
	for i in range(len(res)):
		print(res[i], end = " ")
   
# xét bài toán với số tiền cần trả là 24k
n = 24
print("Số tờ tiền ít nhất cần để trả cho ", n, ": ", end = "")
findMinMoney(n)
