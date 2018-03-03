"""
 链表与非连续内存：项的逻辑顺序和内存中的顺序解耦
 自定义实现单链表结构：
 （1）外部的head link
 （2）每一个node由data和link组成，其中link指向下一个node


 （1）
 FORTRAN语言中，唯一的数据结构是数组，所以只有用两个并行的数组共同表示：
 data=[D1，D3，D2，None,D4]和next[2,4,1,None,-1]
 第1个node：由data[0]=D1,next[0]=2表示，其中D1是数据，2是指向下一个节点的标志；由此，第2个node，由data[2]=D2,next[3]=1表示，其中D2是数据，1是指向下一个节点的标志；
 由此，第3个node，由data[1]=D3,next[1]=4表示，其中D3是数据，4是指向下一个节点的标志;
  由此，第4个node，由data[4]=D4,next[4]=-1表示，其中D4是数据，-1表示链表到此结束

  （2）Pascal和C++中，用指针和内建的堆表示，how to？？
  （3）Python语言：包含两个字段的一个对象，程序员不需要考虑分配和回收内存


单链表：
head link单链表的入口，由此访问到整个链条，很容易获取一个项的后继项，但并不容易获取前驱项。
双链表：
除了head link还有tail link，因此可以直接访问最后一项，也容易活取前驱项。
下面来实现链表这种结构，并实现一些操作。

最后一项没有链接：empty link。单链表的最后一项没有后继的链接，双链表除了最后一项没有后继，第一项也没有前驱。
"""

#1 define a singly_linked_node，首先定义Node类，它是链表的组成元素
class Node(object):
	def __init__(self,data,next=None):
		self._data=data
		self._next=next

#create new nodes
# node1=None
# node2=('A',None)
# node3=('B',node2)

#2 create linked_structure using circulation 然后定义SingleLinkedList，真正的链表类

class SingleLinkedList():
	def __init__(self):
		self._head=None  #初始化链表为空表    self._size=0
	#在开头增加一个元素
	def add(self, value):
		new_node=Node(value)
		fist_node=self._head
		new_node._next=fist_node
		self._head=new_node
	#在末尾增加一个元素
	def append(self, value):
		new_node=Node(value,None)
		probe=self._head
		if probe==None:
			self._head = new_node
		else:
			while(probe._next!=None):
				probe=probe._next
			#这样就找到了最后一个node
			last_node=probe
			last_node._next=new_node

	def	add_any(self,value,index):
		#得考虑3种情况:index<0,index在n-1之前和index超出n-1的情况

		probe = self._head
		if probe is None or index<=0:#无论原本有0个元素还是1个元素，new_node的next都会和原head保持一致，#小于0视同等于0，大于n等同为n
			new_node = Node(value,probe)
			self._head=new_node
		else:
			while(index>1 and probe._next!=None):
				probe=probe._next#index为1，经过0轮，probe指向第0元素,probe._next指向1元素；index为2，经过1轮，probe表示第1个元素，probe._next指向2元素
				index-=1
			#此时probe表示第index-1个元素，probe._next指向index元素
			new_node=Node(value,probe._next)
			probe._next=new_node



	#查找是否存在
	def search(self, target):
		probe = self._head
		while (probe != None):
			if probe._data == target:
				return True
			probe = probe._next
		return False
	#遍历访问
	def traversal(self):
		probe=self._head
		while(probe!=None):
			print(probe._data)
			probe=probe._next
	def replace(self,target_value,new_value):
		probe=self._head
		while(probe!=None):
			if probe._data==target_value:
				probe._data=new_value
				return True
			probe=probe._next
		return False
	def delete_head(self):
		if self._head!=None:
			removed_data=self._head._data
			self._head=self._head._next
		return removed_data

	def pop(self):
		probe=self._head
		if probe==None:
			removed_data=None
		elif probe._next==None:
			removed_data=probe._data
		else:
			while(probe._next._next!=None):
				probe=probe._next
			#此时probe就是倒数第2项
			removed_data=probe._next._data
			probe._next=None
		return removed_data
	def delete_any(self,index):

		if self._head==None:#如果一项都没有
			return
		if index<=0:#小于0视同等于0，大于n等同为n
			self._head=self._head._next
		else:
			#找到index-1这一项，让index-1项指向index+1项
			probe=self._head
			while (index>1 and probe._next._next!=None):
				probe=probe._next
				index-=1
			#假如index=1，经过1轮，probe指向第1项，index=2，经过2轮。probe指向第2项，经过index轮，probe指向第n项
			removed_data=probe._next._data
			probe._next=probe._next._next




if __name__=="__main__":

	#用循环创建链表实例
	a_singlelinkedlist=SingleLinkedList()
	for i in range(1,6):#从后往前创建，所以1在后5在前
		a_singlelinkedlist.add(i)#先创建一个Node对象，再让head_obj引用它

	"""
	#遍历刚刚创建的链表（遍历完就删除了
	#从head link开始，head link是链表的唯一入口
	for i in range(1,6):
		print(head._data)
		head=head._next
	#输出为5，4,3，2,1，这是从前往后访问。
	#但这种方式，改变了next的值，循环结束以后，head为None,再也找不到入口的节点了。
	#所以这种情况相当于删除了链表，之后节点不再可用，会被python回收
	"""

	#遍历访问（不删除）
	a_singlelinkedlist.traversal()

	#搜索(由于链表不支持随机访问，所以哪怕是排序号的链表，搜索效率也高不起来
	print('搜索')
	print(a_singlelinkedlist.search(2))

	#替换
	print('替换')
	target_value=4
	new_value=10
	print(a_singlelinkedlist.replace(target_value,new_value))
	a_singlelinkedlist.traversal()

	#在开头插入
	print('在开头插入')
	a_singlelinkedlist.add(30)
	a_singlelinkedlist.traversal()

	#在末尾插入
	print('在末尾插入')
	a_singlelinkedlist.append(100)
	a_singlelinkedlist.traversal()




	#在开头删除
	print('在开头删除')
	print(a_singlelinkedlist.delete_head())
	a_singlelinkedlist.traversal()


	#在末尾删除
	print('在末尾删除')
	print(a_singlelinkedlist.pop())
	a_singlelinkedlist.traversal()

	#在任意位置插入
	print('在任意位置插入')
	a_singlelinkedlist.add_any(80,1)
	a_singlelinkedlist.traversal()

	#在任意位置删除
	print('在任意位置删除')
	a_singlelinkedlist.delete_any(3)
	a_singlelinkedlist.traversal()