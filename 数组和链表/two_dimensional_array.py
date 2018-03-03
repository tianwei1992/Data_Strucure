"""
基于一维数组，建立二维数组

重点关注Grid类的__init__方法和__getitem__(self, index)方法的写法

"""

from one_dimensional_array import Array
class Grid(object):
	def __init__(self,rows,colums,fillValue=None):
		self._data=Array(rows)#先定义行，每行是一个元素，这个二维数组一共有rows行
		for row in range(rows):#对每一个元素，变成长度为colums的一维数组，
			self._data[row]=Array(colums,fillValue)
	def getHeight(self):
		return len(self._data)
	def getWidth(self):
		return len(self._data[0])
	def __getitem__(self, index):
		return self._data[index]
	def __str__(self):
		result=''
		for row in range(self.getHeight()):
			for col in range(self.getWidth()):
				result+=str(self._data[row][col])+' '
			result+='\n'
		return result


"""
使用实例
"""
table=Grid(3,5,0)
print(table)
#通过遍历改变每个元素的值
for row in range(table.getHeight()):
	for column in range(table.getWidth()):
		table[row][column]=str(row)+str(column)
print(table)#调用了这个方法：__str__(self)

"""
00 01 02 03 04 
10 11 12 13 14 
20 21 22 23 24 
"""