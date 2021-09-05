driving = input('have you drivern a car: ')
if driving != 'yes' or 'no':
	print('you can only enter yes or no')
	raise SystemExit
age = input ('please enter your age: ')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('you passed')
	else:
		print('weird! How comes you could drive a car')
elif driving == 'no':
	if age >= 18:
		print('you should be able to have a driving licence')
	else:
		print('good! you can do it several years later')
else:
	print('you can only enter yes or no')