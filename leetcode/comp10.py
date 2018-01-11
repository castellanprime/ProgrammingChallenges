"""
	Given a list of non negative integers, arrange them such that they form the largest number.

	For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

	Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution(object):
	@staticmethod
	def largestNumber(nums):

		results_list, copy_nums = [], []
		in_count = 0
		out_count = 0

		##### Wrong implementation: need to find all combinations of the array
		# convert the list elements into a number
		first_num = int(''.join([str(v) for v in nums]))
		results_list.append(first_num)

		for out_count in range(len(nums)):
			copy_nums = [v for v in nums]
			for in_count in range(out_count, len(nums)):
				#swap
				num_str = copy_nums[in_count]
				print("Out_count=", out_count, " in_count=", in_count)
				swap_num = (in_count + 1) % len(nums)
				print("Swap num=", swap_num, " len(nums)=", len(nums))
				copy_nums[in_count] = copy_nums[swap_num]
				copy_nums[swap_num] = num_str 
				num_str_conv = int(''.join([str(v) for v in copy_nums]))
				results_list.append(num_str_conv)

		results_list.sort()
		str_to_return = str(results_list[len(results_list) - 1])
		return str_to_return

if __name__ == '__main__':
	import sys
	try:
		num_of_test_cases = int(sys.stdin.readline().rstrip())
		for num in range(num_of_test_cases):
			print(" \nAdd values:")
			vals = [int(x) for x in list(sys.stdin.readline().rstrip().split())]
			print(" Actual value list=", vals)
			print("Largest number=", Solution.largestNumber(vals))
	except KeyboardInterrupt as e:
		print("Closing")