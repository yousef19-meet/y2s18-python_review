# def twice(x):
# 	return x * 2

# my_money = 100
# my_money = twice(my_money)
# print(my_money)

def interest(x):
	# Defines total money after getting
	# interest.
	if x < 150:
		x = x*1.05
	if 150 <= x <= 300:
		x = x*1.1
	if x > 300:
		x = x*1.2
	return x

x = 200.
print(interest(x))
