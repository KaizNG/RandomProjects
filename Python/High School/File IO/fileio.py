days_file = open('days.txt','r')
days = days_file.read()
new_file = open('new_days.txt','w')

title = 'Days of the Week\n'
days = 'Mon\nTues\nWed\nThurs\nFri\nSat\nSun'
new_file.write(title)
print(title) # let our_file be a file object
new_file.write(days)
print(days) # let our_file be a file object

days_file.close()
new_file.close()
