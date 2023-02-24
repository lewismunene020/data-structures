import time
def sum(n):
	start = time.time()
	the_sum = 0
	for i in range(1, n+1):
		the_sum = the_sum + i
	end = time.time()
	return the_sum,end-start

x = int(input("Enter the value of x : "))

print("The sum is  %d  and required %f seconds to execute"%sum(x))