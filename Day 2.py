#Question 7
#Write a Python program to remove duplicates from a list.
my_list = ["a","list","of","duplicates","a",123,56,123,"of",123]
no_dup = []
for item in my_list:
	if item not in no_dup:
		no_dup.append(item)
print("List without duplicates", no_dup)

#Alternate
my_list = list(set(my_list))
print("List w/o dupes",my_list)

#Question 8
#Write a Python program to check a list is empty or not.
my_list = []
my_list1 = ['a']
if len(my_list) == 0:
	print("Empty")
else:
	print("Non-Empty")

#Alternate:
if not my_list:
	print("Empty")

#Question 9
#Write a Python program to clone or copy a list.
alist = [1,2,3,4,5,6]
blist = alist #Deep Copy
clist = alist.copy() #Shallow Copy
print(alist)
print(blist)
print(clist)
blist.pop()
print(alist)
print(blist)
print(clist)

#Question 10
#Write a Python program to find the list of words that are 
#longer than n from a given list of words.

words = ["athleisure","squirm","extrapolate","excruciating","fun","enjoy","freedom"]
n = 5
satisfy = []
for item in words:
	if len(item) > n:
		satisfy.append(item)
print("Words that satisfy the condition:", satisfy)

#Question 11
#Write a Python function that takes two lists 
#and returns True if they have at least one common member.
def list_match(list1,list2):
	count = 0
	for item in list1:
		if item in list2:
			count = count +1
	if count > 0:
		print("Both have at least one common entry")
	else:
		print("Nothing common found")

list_match(my_list,my_list1)
list_match(alist,blist)

#Question 12
#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
colors =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors.pop(0)
colors.pop(3)
colors.pop(3)
print(colors)

#Alternate
colors =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors = [x for (i,x) in enumerate(colors) if i not in (0,4,5)]
print(colors)