title=input('What is your Favorite Movie:')
print('Capitalize:',title.capitalize())
print('lower case and center:',title.lower().center(50).ljust(30))
substring='a'
count=title.count(substring)
print('substring:',count)
index=title.index('e')
print('index:',index)