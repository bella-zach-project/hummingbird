number = int(input("Enter a number you would like to factor: "))
m = number
t = 0
i = 2
while True:

	t = t + 1
	if t == 1000000: 
		t = 0
		print('({0})'.format(i))
	while (m % i) == 0:
		m = int(m / i)
		print(i, m)

	i = i + 1
	if i * i > m:
		break
if m != 1: 
	print(m)
