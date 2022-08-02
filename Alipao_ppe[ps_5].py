sentence = input("Sentence: ")
counts = {i:0 for i in 'aeiouAEIOU'}
for char in sentence:
  if char in counts:
  	   counts[char] += 1
for kv in counts.items():print(kv)
