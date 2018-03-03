"""
递归实现Fibonacci，形式简单，但是时间复杂度是指数阶
1、1、2、3、5、8、13、21、34
"""


def fib(n):
	if n>2:
		return fib(n-1)+fib(n-2)
	else :#fib(1)=fib(2)=2
		return 1
print(fib(1))#1
print(fib(2))#1
print(fib(3))#2
print(fib(4))#3
print(fib(5))#5
print(fib(6))#8

"""
复杂度：
假设是满满的平衡树1-2-4-8……，总共调用次数是2+4+8+2^n，合起来是2^(n+1)-2，
虽然调用树是不平衡的，但其形状接近平衡树，因此也会很近似指数阶
用循环来写，解除递归
"""