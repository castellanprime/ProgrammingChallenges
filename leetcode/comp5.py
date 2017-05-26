"""
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
	like this: (you may want to display this pattern in a fixed font for better 
	legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R

	And then read line by line: "PAHNAPLSIIGYIR"

	Write the code that will take a string and make this conversion given a number of rows:

	string convert(string text, int nRows):

	Example:
	========
	convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR" 
"""

class Solution(object):
	@staticmethod
	def convert(s, numRows):
		"""

		:type s: str
		:type numRows: int
		:rtype: str
		"""

		if numRows > 1:
			# We need a 2 by 2 grid to write the characters to and to read the characters from
			board = [[] for i in range(numRows)]

			# Strategy
			# On every character read,
			# - if we are starting from the top row, we append that character to the next row on
			#   the board, in turn in a downard direction
			# - if we are starting from the bottom row, we append that character to the next row 
			#   on the board, in turn in an upward direction

			index = 0 				# this index will track which character will be read next
			while index < len(s):
				# Special case is when we start, we append to the top row, row[0]
				if index == 0:
					for row in range(len(board)):
						if index < len(s):	# the string might have been completely read before we reach the end of the loop
							board[row].append(s[index])
							index += 1
						else:
							break						
		
				else:
					# Normal case
					# Going upwards
					for row in range(len(board)-2, -1, -1):	# this begins from the row above the bottom row
						if index < len(s):
							board[row].append(s[index])
							index += 1
						else:
							break

					# Going downwards
					for row in range(1, len(board)):  # this begins from the row below the top row
						if index < len(s):
							board[row].append(s[index])
							index += 1
						else:
							break

			for index, row in enumerate(board):
				print("Row ", index, ":", row)

			intermediate_st = [val for row in board for val in row]
			return "".join(intermediate_st)
		else:
			return s

def main():
	import sys
	num_of_testcases = int(sys.stdin.readline())
	for num in range(num_of_testcases):
		st, rows = sys.stdin.readline().rstrip().split()
		print(Solution.convert(st, int(rows)))

main()



