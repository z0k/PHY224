num = input('Enter a number: ')
unit = raw_input('Enter a unit: ')
if unit == 'lb':
    print num, 'lb is ', num/2.20462, 'kg'
elif unit == 'kg':
    print num, 'kg is ', num*2.20462, 'lb'
else:
    print 'Incompatible units.'
