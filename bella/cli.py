stk = [ 'this', 'is', 123, 456 ]
def list():
	for a in stk:
		print(a)
	print('---------------------------')
while True:
	list()
	v = input('> ')
	if v == 'd':
	   stk = stk[:-1]
	elif v == '+':
	   s = int(stk[-1]) + int(stk[-2])
	   stk = stk[:-2]
	   stk.append(s)
	else:
	   stk.append(v)
