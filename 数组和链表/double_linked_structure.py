"""
链表的辩题：
带有额外的指针，能够提高性能并简化代码
"""

from singly_linked_structure import Node
class TwoWayNode(Node):
	def __init__(self,data,previous=None,next=None):
		Node.__init__(self,data,next)#注意这种写法……
		self._previous=previous

class DoubleLinkedList():
	def __init__(self):
		self._head=None
		self._tail=None
	#遍历访问
	def traversal(self):
		probe=self._head
		while(probe!=None):
			print(probe._data)
			probe=probe._next
	def traversal_reverse(self):
		probe=self._tail
		while(probe!=None):
			print(probe._data)
			probe=probe._previous
	def append(self, value):
		# 先新建节点
		new_node=TwoWayNode(value,self._tail,None)
		#修改tail指针指向
		self._tail=new_node
		#修改head指针指向
		probe = self._head
		if probe == None:
			self._head = new_node
		else:
			while (probe._next != None):
				probe = probe._next
			# 这样就找到了最后一个node
			last_node = probe
			last_node._next = new_node


d=DoubleLinkedList()
d.append('a')
d.append('b')
#print(d)
d.traversal()
d.traversal_reverse()