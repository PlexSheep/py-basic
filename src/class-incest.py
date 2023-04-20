#!/usr/bin/env python3
class Root():
	a = "Root"
	def f(self):
		print(self.a)
	pass

class A(Root):
	a = "A"
	def f(self):
		print(self.a)
		super().f()
	pass

class B(Root):
	a = "B"
	def f(self):
		print(self.a)
		super().f()
	pass

class C(A, B):
	# C is a child of A and B, which are siblings. Therefore incest.
	# You may laugh now.
	def f(self):
		print("C")
		super().f()
		print(C.__mro__) # Method Resolution Order(MRO) 
	pass

def main():
	o = C()
	o.f()

if __name__ == "__main__":
	main()
