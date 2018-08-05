# Write your solution for 1.4 here!


def is_prime(x):
	i=2
	#pass
	while i<x:
		if x%i==0:
			print("it's not a prime number")
			print(i)
			return False
		#return True
		i+=1
	print("its a prime number")

	return True
	
test=5191

is_prime(test)