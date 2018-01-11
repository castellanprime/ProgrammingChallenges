"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.	

	
1->2->3->4->5->NULL

k = 1: 5->1->2->3->4->NULL
k = 2: 4->5->1->2->3->NULL
k = 3: 3->4->5->1->2->NULL

node_ptr = head
back_ptr = None
while (node_ptr != NULL):
	back_ptr = node_ptr
	node_ptr = node_ptr.next


Algorithm

Initialize two pointers, back_ptr and node_ptr
Move through the list with node_ptr in front and back_ptr catching up
Move the node_ptr to the node before NULL and the back_ptr to the node behind node_ptr
while count < k
	let back_ptr point to NULL
	unlink node_ptr
	let node_ptr point to head
	move head to node_ptr

"""



class List(object):

	class ListNode(object):
		def __init__(self, x):
			self.val = x
			self.next = None

		def __str__(self):
			if self.val != None:
				return "{0}".format(self.val) 

	def __init__(self):
		self.head = None
		self.size = 0

	def add(self, val):
		new_node = self.ListNode(val)
		if self.head == None:
			self.head = new_node
		else:
			#print(new_node)
			new_node.next = self.head
			self.head = new_node
			self.size += 1 

	def display(self, node):
		add_ptr = node 
		st = "" 
		while add_ptr != None:
			st += add_ptr.__str__() + "->"
			add_ptr = add_ptr.next 
		st += "None"
		return st

	def __str__(self):
		add_ptr = self.head
		st = "" 
		while add_ptr != None:
			st += add_ptr.__str__() + "->"
			add_ptr = add_ptr.next 
		st += "None"
		return st

	def add_items(self, l):
		for val in l:
			self.add(val)

class Solution(object):
	@staticmethod
	def rotateRight(head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode 
		"""

		if head == None:
			return None

		node_ptr = head
		back_ptr = None 

		# Naive solution
		"""
		if any([node_ptr.next == None, k <= 0]):
			return head
		else:
			while node_ptr.next != None:
				back_ptr = node_ptr 
				node_ptr = node_ptr.next
			count = 0
			while count < k:
				node_ptr.next = head
				while head.next != node_ptr:
					head = head.next
				head = head.next
				back_ptr.next = None			
				while node_ptr.next != back_ptr:
					node_ptr = node_ptr.next
				new_ptr = node_ptr 
				node_ptr = back_ptr 
				back_ptr = new_ptr
				count += 1
			return head
		"""

		"""
			To optimise, we divide the k by the size of the list.
			The remainder is what we shift by
		"""
		if any([node_ptr.next == None, k <= 0]):
			return head
		else:
			# Get size
			size = 1
			while node_ptr.next != None:
				back_ptr = node_ptr 
				node_ptr = node_ptr.next
				size += 1
			new_k = k % size
			if new_k == 0:
				return head
			count = 0
			while count < new_k:
				node_ptr.next = head
				while head.next != node_ptr:
					head = head.next
				head = head.next
				back_ptr.next = None			
				while node_ptr.next != back_ptr:
					node_ptr = node_ptr.next
				new_ptr = node_ptr 
				node_ptr = back_ptr 
				back_ptr = new_ptr
				count += 1
			return head


if __name__ == '__main__':
	import sys
	try:
		#l = List()
		#l.add_items([5,4,3,2,1])
		#print(l)
		num_of_test_cases = int(sys.stdin.readline().rstrip())
		for num in range(num_of_test_cases):
			print(" \nAdd values:")
			l = List()
			vals = [int(x) for x in list(sys.stdin.readline().rstrip().split())]
			l.add_items(vals)
			print("List before rotation:",  l.__str__())
			print(" \nEnter rotation factor:")
			k = int(sys.stdin.readline().rstrip())
			l.head = Solution.rotateRight(l.head, k)
			print("List after rotation:",  l.__str__())
	except KeyboardInterrupt as e:
		print("Closing")