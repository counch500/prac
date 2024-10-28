def biased(init):
	print("QQ")
	bias = yield init
	while bias:
		init += bias
		bias = yield init

