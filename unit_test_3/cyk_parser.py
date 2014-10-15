countlist = []
with open('parse_train.counts.out') as openfile:
	for line in openfile:
		countlist.append(line.split(' ')[2:])

print countlist		




