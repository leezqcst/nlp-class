import re

fp = open("cri.txt")

content = eval(fp.read())
op = open("docs","w")
for doc in content:
	op.write(doc)
	op.write("\n")
op.close()
fp.close()