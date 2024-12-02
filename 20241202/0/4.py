import struct

with open("file4", "wb") as f:
	a = struct.pack("f3sif3sif3si", 0.1,bytes([1,2,3]), 11, 0.2, bytes([2,3,4]), 12, 0.3, bytes([3,4,5]), 13)
	f.write(a)
with open("file4", "rb") as f:
	record = f.read(struct.calcsize("!f3si"))
	b = struct.unpack("!f3si", record)
	print(a)
