def callMe(number, mylist):
	if number < 10:
		mylist.append(number+1)
		return callMe(number+1, mylist)



mylist = []
callMe(2, mylist)
print mylist