stk = [ 'this', 'is', 123 ]
def list():
	for a in stk:
		print(a)
	print('---------------------------')
while True:
	list()
	v = input('> ')
	stk.append(v)
