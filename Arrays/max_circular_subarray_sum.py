
def maxCircularSum(a, n):
	if (n == 1):
		return a[0]
	sum = 0
	for i in range(n):
		sum += a[i]
	curr_max = a[0]
	max_so_far = a[0]
	curr_min = a[0]
	min_so_far = a[0]
	for i in range(1, n):
	
		# Kadane's Algorithm to find Maximum subarray sum.
		curr_max = max(curr_max + a[i], a[i])
		max_so_far = max(max_so_far, curr_max)

		# Kadane's Algorithm to find Minimum subarray sum.
		curr_min = min(curr_min + a[i], a[i])
		min_so_far = min(min_so_far, curr_min)
	if (min_so_far == sum):
		return max_so_far

	return max(max_so_far, sum - min_so_far)

a = list(map(int,input().split()))
n = len(a)
print("Maximum circular sum is", maxCircularSum(a, n))