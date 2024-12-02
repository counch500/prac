import pickle
class SerCls:
	lst = []
	dct = {}
	num = 0
	st = ""

ser = SerCls()
ser.lst = [1,2,3]
ser.dct = {4,5,6}
ser.num = 8
ser.st = "cute"

res = pickle.dumps(ser)
del ser
ser1 = pickle.loads(res)
print(ser1.lst)
print(ser1.dct)
print(ser1.num)
print(ser1.st)
