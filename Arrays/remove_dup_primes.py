# Removes duplicates using multiplication of 
# distinct primes in array 
def removeDups(vect):
	prod = vect[0] 
	res_ind = 1
	i = 1
	while (i < len(vect)):
		if (prod % vect[i] != 0):
			vect[res_ind] = vect[i] 
			res_ind += 1
			prod *= vect[i] 
		i += 1
	return vect[:res_ind] 
	
# Driver code 
vect = [3,5,7,3,5,7,11,13,11,19]
vect = removeDups(vect) 
for i in range(len(vect)):
	print(vect[i], end =" ")

