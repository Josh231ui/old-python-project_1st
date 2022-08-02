numbers = []
while True:
	num_collector = int(input("Enter a number: "))
	if num_collector != 0:
		numbers.append(num_collector)
	else:
		break
average = sum(numbers)/len(numbers)
print(average)