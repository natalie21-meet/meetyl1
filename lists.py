def common_numbers(list1, list2):
	commonlist=[]
	for number in list1:
		if number in list2:
			commonlist.append(number)
	return commonlist
b=input("write numbers")
c=input("write numbers")
a=common_numbers(b,c)
print(a)