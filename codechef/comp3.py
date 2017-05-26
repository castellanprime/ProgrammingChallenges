"""
Consider a 2d-grid. That is, each cell is identified by (i,j). You have received reports of two 
snake-sightings on this grid. You want to check whether they could be partial sightings of the 
same snake or not.

Each of the snake sightings correspond to a straight, axis-parallel line segment in the grid, 
and the starting and ending cells for each are given to you. Now consider a graph, where each 
cell in the 2d-grid is a vertex. And there is an edge between 2 vertices if and only if the 
cells corresponding to these two vertices are consecutive cells in at least one of the two 
snakes. That is, at least in one of the snakes, when you go from one end point to the other 
end point, these two cells should occur consecutively.

The two sightings/snakes are said to be same, if both these conditions are satisfied:

    - The union of the set of cells in the first snake and the set of cells in the second snake, 
    should form a connected component in this graph.
    - No vertex should have degree more than 2 in the graph.

In other words, the induced subgraph on the union set must be a path graph.

Input
=====
    - The first line contains a single integer, T, which is the number of testcases. The 
    description of each testcase follows.
    - The first line of each testcase contains four integers: X11, Y11, X12, Y12. This 
    represents the fact that the first snake's end points are (X11, Y11) and (X12, Y12).
    - The second line of each testcase contains four integers: X21, Y21, X22, Y22. This 
    represents the fact that the second snake's end points are (X21, Y21) and (X22, Y22).

Output
======
    For each testcase, output "yes" if the snakes are the same, as per the definition given 
    above. Output "no" otherwise.

Constraints
===========
    - 1 ≤ T ≤ 105
    - -109 ≤ Xij,Yij ≤ 109
    - The two end points of every snake is guaranteed to be either on the same row or on the 
    same column. Thus, the snake occupies all the cells between these cells, including the end points.

 
Example
=======
Input:
4
2 1 8 1
11 1 7 1
2 1 8 1
11 1 9 1
2 1 8 1
3 1 3 -2
2 1 8 1
2 1 2 -2
Output:
yes
no
no
yes

"""

class Point(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def _isYEqual(self, other):
		return self.y == other.y

	def _isXEqual(self, other):
		return self.x == other.x

	def isYEquals(self, points):
		for point in points:
			if self._isYEqual(point) is False:
				return False
		return True

	def isXEquals(self, points):
		for point in points:
			if self._isXEqual(point) is False:
				return False
		return True

	def __eq__(self, other):
		return self._isXEqual(other) and self._isYEqual(other)

	def __ne__(self, other):
		return not self.__eq__(other)

	def getValues(self):
		return [self.x, self.y]

	def __repr__(self):
		return "X:{0}, Y:{1}".format(self.x, self.y)

# P1 = p1_line1
# P2 = p2_line1
# P3 = p1_line2
# P4 = p2_line2
def _test(p1_line1, p2_line1, p1_line2, p2_line2):
	# P1 == P3 or P1 == P4
	if (p1_line1 == p1_line2) or (p1_line1 == p2_line2):
		return True
	# P2 == P3 or P2 == P4	
	elif (p2_line1 == p1_line2) or (p2_line1 == p2_line2): 	
		return True
	else:
		coords, all_nums_in_line1, all_nums_in_line2 = None, None, None
		if p1_line1.isYEquals([p2_line1, p1_line2, p2_line2]):
			coords = [p1_line1.x, p2_line1.x, p1_line2.x, p2_line2.x]
		elif p1_line1.isXEquals([p2_line1, p1_line2, p2_line2]):
			coords = [p1_line1.y, p2_line1.y, p1_line2.y, p2_line2.y]
		else:
			return False

		"""Now we have a fixed picture, think of the points on the number line"""
		"""P1.....P2......P3.......P4"""
		# Rename the coords 
		P1,P2, P3, P4 = None, None, None, None
		if coords[0] >= coords[1]:
			P1 = coords[1]
			P2 = coords[0]
		elif coords[0] < coords[1]:
			P1 = coords[0]
			P2 = coords[1]

		if coords[2] >= coords[3]:
			P3 = coords[3]
			P4 = coords[2]
		elif coords[2] < coords[3]:
			P3 = coords[2]
			P4 = coords[3]

		"""Thinking them as two lines. P1 === P2  and P3 === P4"""
		"""Since they are horizontal, we determine that """
		if P1 < P3:
			if P3 < P2:
				return True
		else:
			if P1 < P4:
				return True

		return False

		""" Too big(naive solution)- Memory too large
		we are generating too many numbers
		if coords[0] >= coords[1]:
			all_nums_in_line1 = [val for val in range (coords[1], coords[0]+1)]
		elif coords[0] < coords[1]:
			all_nums_in_line1 = [val for val in range (coords[0], coords[1]+1)]

		if coords[2] >= coords[3]:
			all_nums_in_line2 = [val for val in range (coords[3], coords[2]+1)]
		elif coords[2] < coords[3]:
			all_nums_in_line2 = [val for val in range (coords[2], coords[3]+1)]

		common = set(all_nums_in_line1).intersection(all_nums_in_line2)
		if common:
			return True
		else:
			return False
		"""

def main():
	import sys
	num_of_testcases = int(sys.stdin.readline())
	for index in range(0, num_of_testcases):
		line1_x1, line1_y1, line1_x2, line1_y2 = sys.stdin.readline().rstrip().split()	
		line2_x1, line2_y1, line2_x2, line2_y2 = sys.stdin.readline().rstrip().split()
		pt1_line1 = Point(int(line1_x1), int(line1_y1))
		pt2_line1 = Point(int(line1_x2), int(line1_y2))
		pt1_line2 = Point(int(line2_x1), int(line2_y1))
		pt2_line2 = Point(int(line2_x2), int(line2_y2))
		if _test(pt1_line1, pt2_line1, pt1_line2, pt2_line2):
			print("yes")
		else:
			print("no") 

main()