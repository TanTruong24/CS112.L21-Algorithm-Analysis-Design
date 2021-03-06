#reference: https://www.geeksforgeeks.org/program-generate-possible-valid-ip-addresses-given-string/

def is_valid(ip):

	# Splitting by "."
	ip = ip.split(".")
	
	# Checking for the corner cases
	for i in ip:
		if (len(i) > 3 or int(i) < 0 or
						int(i) > 255):
			return False
		if len(i) > 1 and int(i) == 0:
			return False
		if (len(i) > 1 and int(i) != 0 and
			i[0] == '0'):
			return False
			
	return True

# Function converts string to IP address
def convert(s):
	
	sz = len(s)

	# Check for string size
	if sz > 12:
		return []
	snew = s
	l = []

	# Generating different combinations.
	for i in range(1, sz - 2):
		for j in range(i + 1, sz - 1):
			for k in range(j + 1, sz):
				snew = snew[:k] + "." + snew[k:]
				snew = snew[:j] + "." + snew[j:]
				snew = snew[:i] + "." + snew[i:]
				
				# Check for the validity of combination
				if is_valid(snew):
					l.append(snew)
					
				snew = s
				
	return l

# Driver code		
s = input()

ip = convert(s)

for i in ip:
    print(i)
