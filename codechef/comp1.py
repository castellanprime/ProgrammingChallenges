#!/usr/bin/python
"""
The annual snake festival is upon us, and all the snakes of the kingdom have gathered to 
participate in the procession. Chef has been tasked with reporting on the procession, 
and for this he decides to first keep track of all the snakes. When he sees a snake first, 
it'll be its Head, and hence he will mark a 'H'. The snakes are long, and when he sees the 
snake finally slither away, he'll mark a 'T' to denote its tail. In the time in between, 
when the snake is moving past him, or the time between one snake and the next snake, he 
marks with '.'s. Because the snakes come in a procession, and one by one, a valid report 
would be something like "..H..T...HTH....T.", or "...", or "HT", whereas "T...H..H.T", 
"H..T..H", "H..H..T..T" would be invalid reports (See explanations at the bottom).

Formally, a snake is represented by a 'H' followed by some (possibly zero) '.'s, and then 
a 'T'. A valid report is one such that it begins with a (possibly zero length) string of 
'.'s, and then some (possibly zero) snakes between which there can be some '.'s, and then 
finally ends with some (possibly zero) '.'s.

Chef had binged on the festival food and had been very drowsy. So his report might be invalid. You need to help him find out if his report is valid or not.

Input
=====
    The first line contains a single integer, R, which denotes the number of reports to be 
    checked. The description of each report follows after this.
    The first line of each report contains a single integer, L, the length of that report.
    The second line of each report contains a string of length L. The string contains only 
    the characters '.', 'H', and 'T'.

Output
======
    For each report, output the string "Valid" or "Invalid" in a new line, depending on 
    whether it was a valid report or not.

Constraints
==========
    1 ≤ R ≤ 500
    1 ≤ length of each report ≤ 500

Example
=======
Input:
6
18
..H..T...HTH....T.
3
...
10
H..H..T..T
2
HT
11
.T...H..H.T
7
H..T..H

Output:
Valid
Valid
Invalid
Valid
Invalid
Invalid


Notes
+++++
Characters indicate time
Snake head = 'H'
Snake tail = 'T'
Time between 'H' and 'T' is '.' or time between one snake and 
another is '.'

Regex
+++++
Valid configurations are 
(.*(H.*T)*.*)*
"""

def main():
 	import sys
 	import re
 	num_of_reports = int(sys.stdin.readline())
 	reports = []
 	match_re = re.compile("((\.)*[H](\.)*[T](\.)*)*")
 	for index in range(0, num_of_reports):
 		report_length = int(sys.stdin.readline())
 		report = sys.stdin.readline().rstrip()
 		if match_re.match(report):
 			print("Valid")
 		else:
 			print("Invalid")

# Finite state machine
def _FSM(st):
	startState, headState = True, False
	for char in st:
		if startState:
			if char == '.':
				continue
			if char == 'H':
				startState=False
				headState=True
			if char == 'T':
				return False
		elif headState:
			if char == 'T':
				headState= False
				startState=True
			if char == 'H':
				return False
			if char == '.':
				continue
	if headState:
		return False
	return True

def main2():
 	import sys
 	num_of_reports = int(sys.stdin.readline())
 	if num_of_reports < 1 or num_of_reports > 500:
 		print("The num of reports to checked has to be in between 1 and 500")
 		return
 	for index in range(0, num_of_reports):
 		report_length = int(sys.stdin.readline())
 		if report_length < 1 or report_length > 500:
 			print("The length of your report has to be in between 1 and 500")
 			return
 		report = sys.stdin.readline().rstrip()
 		while len(report) != report_length:
 			print("Your report is not of the required length")
 		if _FSM(report):
 			print("Valid")
 		else:
 			print("Invalid") 

main()
#main2()
 	



