#X = {A, B, C, B, D, A, B}
#Y = {B, D, C, A, B, A}
#X = {B, C, B, A}

def LCS_length(x, y):
	m = len(x)
	n = len(y)

	b = [[None] * n for i in range(1,m + 1)]
	c = [[None] * (n + 1) for i in range(m + 1)]


	for i in range(1, m + 1):
		c[i][0] = 0

	for j in range(n + 1):
		c[0][j] = 0


	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if(x[i - 1] == y[j - 1]):
				c[i][j] = c[i - 1][j - 1] + 1
				b[i - 1][j - 1] = 'diag'
			elif(c[i - 1][j] >= c[i][j - 1]):
				c[i][j] = c[i - 1][j]
				b[i - 1][j - 1] = 'up'
			else:
				c[i][j] = c[i][j - 1]
				b[i - 1][j - 1] = 'left'

	return c, b 

def Print_LCS(b, x, i, j):
	result = ''
	if(i == 0 or j == 0):
		return 

	if(b[i - 1][j - 1] == 'diag'):
		Print_LCS(b, x, i - 1, j - 1)
		print(x[i - 1])
	elif(b[i - 1][j - 1] == 'up'):
		Print_LCS(b, x, i - 1, j)
	else:
		Print_LCS(b, x, i, j - 1)


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']

memo, traceback = LCS_length(X, Y)
Print_LCS(traceback, X, len(X), len(Y))

