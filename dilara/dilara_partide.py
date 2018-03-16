n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])

needs = input().split()
for k in range(len(needs)):
	needs[k] = float(needs[k])

total = input().split()
for k in range(len(total)):
	total[k] = float(total[k])

computation = [0]*n
while k != 0 :
	for i in range(len(total)):
		computation[i] = (int(total[i]/needs[i]))
	minimum_index = computation.index(min(computation))
	total[minimum_index] += 1
	k -= 1

for i in range(len(total)):
		computation[i] = (int(total[i]/needs[i]))
output = min(computation)
print (output)