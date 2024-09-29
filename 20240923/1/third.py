while N := int(input()):
	for row in range(3):
        	line = ""
		for col in range(3):
			i = N + row
            		j = N + col
            		product = i * j

            		if product == 6:
                		line += f"{i} * {j} = :)  "
            		else:
                		line += f"{i} * {j} = {product}  "
       	print(line)

