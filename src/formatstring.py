import datetime
# {:d} integer value
# print('{:d}'.format(10.5)) # '10'
print('{:.2f}'.format(0.5)) # '0.50'
print('{:<6s}'.format('Py')) #  'Py    '
print('{:>6s}'.format('Py') ) #  '    Py'
print('{:^6s}'.format('Py') ) #  '  Py  '
print('{:*^6s}'.format('Py') ) #  '  Py  '
print('The valueof pi is: {:.5f}'.format(3.141592))
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total)) # 'Correct answers: 86.36%'
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d)) # '2010-07-04 12:15:58'