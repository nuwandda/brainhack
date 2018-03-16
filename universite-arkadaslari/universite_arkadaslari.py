c_t = input().split()
c = int(c_t[0])
t = int(c_t[1])
routes = []
for i in range(t):
	inp = input().split()
	for k in range(len(inp)):
		inp[k] = int(inp[k])
	routes.append(inp)
for i in range(len(routes)): #by transitive relation
	if routes[i][1] == routes[i+1][0]:
		routes.append([routes[i][0],routes[i+1][1],(routes[i][2]+routes[i+1][2])])
prices = []
p = input().split()
for i in range(len(p)):
	p[i] = int(p[i])
	prices.append(p[i])

path_matrix = [[0 for x in range(c)] for y in range(c)]
matrix = [[0 for x in range(c)] for y in range(c)]

index_1 = [0,0]
for i in path_matrix:
	for j in i:
		if index_1[0] != index_1[1]:
			for t in routes:
				path_matrix[t[0]-1][t[1]-1] = t[2]
				path_matrix[t[1]-1][t[0]-1] = t[2]
		index_1[0] += 1
	index_1[1] += 1
	index_1[0] = 0

result = []
index_matrix = [0,0]
index_prices = 0
for i in matrix:
	for j in i:
		if path_matrix[index_matrix[1]][index_matrix[0]] == 0:
			matrix[index_matrix[1]][index_matrix[0]] = prices[index_matrix[1]]
			index_matrix[0] += 1
			index_prices += 1
		else:
			matrix[index_matrix[1]][index_matrix[0]] = 2*path_matrix[index_matrix[1]][index_matrix[0]] + prices[index_prices]
			index_prices += 1				
			index_matrix[0] += 1
	result.append(min(matrix[index_matrix[1]]))
	index_matrix[1] += 1
	index_matrix[0] = 0
	index_prices = 0
for i in range(len(result)):
	result[i] = str(result[i])
result_main = " ".join(result)
print (result_main)