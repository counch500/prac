class Sender():
	p = True
	@classmethod
	def report(cls):
		if cls.p:
			print("Greetings!")
			cls.p = False
		else:
			print("Go away!")

class Asker:
	@staticmethod
	def askall(lst):
		for i in lst:
			i.report()

a, b, c = Sender(), Sender(), Sender()
Asker().askall([a,b,c,a,b,c])
