import datetime

# create a new date object for the 1st of January 2001
new_millenium = datetime.date(2001, 1, 1)

# you might also see datetimes parsed from strings in different ways:
new_millenium = datetime.date.fromisoformat('2001-01-01')
new_millenium = datetime.datetime.strptime('2001-01-01', '%Y-%m-%d')

# we can format the date object into a string using the strftime method and specifying the format
# in this case, we are using the format 'A' to get the full name of the day of the week
# look up python documentation to see all the available format codes.
print("the first day of the new millenium was a:")
print(new_millenium.strftime('%A'))
