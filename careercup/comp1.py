"""
	Write a function that given a string would print the expanded version of it.
	Note: The number before the opening and closing square brackets is the multiplier for the characters
	within the square brackets

	Examples:
		a2[bc2[c]]d == abcccbcccd
		bc2[d2[ef]2[gh2[i]k]]l = bcdefefghiikghiikdefefghiikghiikl
"""

class Solution(object):
	@staticmethod
	def expand(str):

		from collections import deque


		# Solution
		# We are going to use two datastructures:
		#	- a stack for reading the characters from the original string
		# 	- a queue for multiplying the characters in the square brackets
		# (a) Push characters from the original string upon the stack until you reach the first 
		#  right brace
		# (b) Pop off characters from the stack and enqueue from the end of the queue. Do this until 
		# you reach the first left brace.
		# (c) Pop off the left brace and then pop off the number following it. If you do not get a number,
		# print malformed string and return.
		# (d) Use the number you popped off to multiply the characters in the queue.
		# (e) Add the characters back to the stack.
		# (f) Repeat (a) until you have reached the end of the string.
		# (g) Pop off characters from the stack and enqueue from the end of the queue.

			
		char_read_list = deque()
		char_multiply_list = deque()

		for char in str:
			if char == ']':
				current_char = char_read_list.pop()
				while current_char.isdigit() == False:
					if current_char != '[':
						char_multiply_list.appendleft(current_char)
					current_char = char_read_list.pop()
				if current_char.isdigit() == True:
					num_to_repeat = int(current_char)
					l = list(char_multiply_list) 
					l[:] = l * num_to_repeat
					for item in l:
						char_read_list.append(item)
					char_multiply_list.clear()
			else:
				char_read_list.append(char)

		str_to_return = "".join(list(char_read_list))
		return str_to_return


def main():
    import sys, os
    try:
        num_of_testcases = int(sys.stdin.readline().rstrip())
        for num in range(0, num_of_testcases):
            string_to_test = sys.stdin.readline().rstrip()
            print(Solution.expand(string_to_test))
    except KeyboardInterrupt as e:
        print("Closing")

main()


