# Affichage de la liste des nombre premiers d'un intervalle de valeurs

print(''' 
           Exercice 2
    
    ''')

# Python3 program to find the prime 
# numbers between a given interval

if __name__ == '__main__':
	
	# Declare the variables
	a, b, i, j, flag = 0, 0, 0, 0, 0

	# Ask user to enter lower value of interval
	print("Enter first value of the interval:", 
									end = "")
	a = int(input()) # Take input
	print(a)
	
	# Ask user to enter upper value of interval
	print("Enter second vakue of the interval:", 
									end = "")
	b = int(input()) # Take input
	print(b)
	
	# Print display message
	print("Prime numbers between", a, "and", 
						b, "are:", end = "")

	
	for i in range(a, b + 1):

		
		if (i == 1):
			continue

		
		flag = 1
		
		for j in range(2, i // 2 + 1):
			if (i % j == 0):
				flag = 0
				break
			
		
		if (flag == 1):
			print(i, end = " ")
			

