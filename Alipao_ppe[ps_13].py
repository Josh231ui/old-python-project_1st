x,y = 2,4

first_result = x + y
second_result = first_result - (x/2)
third_result = second_result*(x/2)
fourth_result = third_result/(x/2)
fifth_result = fourth_result%(x/2)
sixth_result = fifth_result**(x/2)
results = [first_result, second_result, third_result, fourth_result, fifth_result, sixth_result]
dictionary_results = {}
for result in results:
	dictionary_results[hex(id(result))] = result
	print(f"{result} is located on {hex(id(result))}")
print(dictionary_results)