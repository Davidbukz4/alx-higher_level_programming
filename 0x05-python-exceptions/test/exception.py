#!/usr/bin/python3

try:
    f = open('test.txt')
    if f.name == 'test.txt':
        raise Exception
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print('Error!')
else:
	print(f.read())
	f.close()
finally:
    print("Executing Finally...")
