"""
	Given an arraylist of nodes, with each node having an ID and a parent ID, 
	determine whether this list is in preorder.

	Examples

		[2/3, 2/4, 5/2, 7/6, 7/8, 5/7, null/5] = preorder 
		[2/3, 5/2, 2/4, null/5, 7/6, 5/7, 7/8] = not preorder

		[3/2, 3/4, 3/5, 6/3, 8/7, 8/9, 8/10, 6/8, 12/11, 12/13, 12/14, 6/12, null/6] = preorder

"""
		
class Solution(object):
	@staticmethod
	def isPreOrder(nodelist):
		"""
        :type nodelist: List[Node]
        :rtype: bool
        """

        # This example accounts for the fact when the tree is not a binary tree

        # Node = namedtuple('Node', ['parentid', 'nodeid'])
        # Each node is written as parentid:nodeid
        # Examples are written in this form:
        # [parentid1:nodeid1, parentid2:nodeid2, parentid3:nodeid3, ...] 

        # Solution
		# (a) Scan the nodelist from left to right.
		# (b) If the parent id of the first node is null or 0, then it is a postorder. Reject and 
		# declare that it is postorder.  
		# (c) If the parent id is not null or 0, then store the parent id as p.
		# (d) Scan the nodelist till the id of the current node being scanned matches p.
		# (e) Check the following node. If the node's parent id matches p, then reject and declare 
		# that it is inorder. Otherwise, declare that it is preorder

    
		if nodelist[0].parentid == 0:
			print("Postorder")
			return False

		parent_to_check = nodelist[0].parentid

		for count in range(1, len(nodelist)):
			if nodelist[count].nodeid == parent_to_check:
				if nodelist[count + 1].parentid == parent_to_check:
					print("Inorder")
					return False
				else:
					print("Preorder")
					return True

def main():
	import sys, os
	try:
		from collections import namedtuple
		num_of_testcases = int(sys.stdin.readline().rstrip())
		Node = namedtuple('Node', ['parentid', 'nodeid'])
		for num in range(0, num_of_testcases):
			string_to_test = sys.stdin.readline().rstrip()
			l = string_to_test.split(",")
			nodelist = []
			for item in l:
				parent, node = item.split(':')
				n = Node(parentid=parent, nodeid=node)
				nodelist.append(n)
			print(Solution.isPreOrder(nodelist))
	except KeyboardInterrupt as e:
		print("Closing")

main()
