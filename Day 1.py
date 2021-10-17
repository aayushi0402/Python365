#What are Python Lists?

#A a valid list can contain Data Types of the following types : Strings, Lists, Tuples, Dictionaries, Sets, Numeric

#How to create Python Lists?

#Following are the ways to create Python Lists

#Method 1:

my_list = ["Hello","Strings",12,99.9,(1,"Tuple"),{"a": "dictionary"}, ["another","list"],{"a","set"}]
print(type(my_list))

#Method 2:
#Using list() function
#From a tuple

my_list2 = list(("a","list","from","tuple"))
print(type(my_list2))

#From a set
#Note that the order of the elements might or might not change randomly
#The abstract concept of a set does not enforce order, so the immplementation is not required to maintain order.
my_list3 = list({"from","a","set","dtype"}) 
print(type(my_list3))
print(my_list3)

#From a dictionary
my_list4 = list({"only":"dictionary","keys_of_dict":"value","are":"used","list_values":"YEAH!"})
print(type(my_list4))
print(my_list4)


#Question 1:
#Write a Python program to sum all the items in a list
marks_list = [90,91,98,79,68,90,99,87,69]
marks_sum = 0
for item in marks_list:
	marks_sum = item + marks_sum
print("Sum of every item in the list:", marks_sum)

#Question 2:
#Write a Python program to multiply all the items in a list.
marks_list = [90,91,98,79,68,90,99,87,69]
marks_prod = 1
for item in marks_list:
	marks_prod = marks_prod * item
print("Product of every item in the list:", marks_prod)


#Question 3:
#Write a Python program to get the largest number from a list.
list_items = [1233,4566,789,345,6770,7896,23455,9064,2334]
largest = list_items[0]
for item in list_items:
	if item > largest:
		largest = item
print("Largest item in the list is:", largest)


#Question 4:
#Write a Python program to get the smallest number from a list.
list_items = [1233,4566,789,345,6770,7896,23455,9064,2334]
smallest = list_items[0]
for item in list_items:
	if item < smallest:
		smallest = item
print("Smallest item in the list is:", smallest)

#Question 5:
#Write a Python program to count the number of strings where the string length is 2 or more 
#and the first and last character are same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

stri = "Malayalam"
alist = ["Length","of","strings","Hippopotamus","Dinosaurs","Malayalam","1221"]
count = 0
for item in alist:
	if (len(item) > 2) and (item[0].lower() == item[len(item) - 1].lower()):
	    count = count + 1
print(count)

#Question 6:
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

unsort = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
first = []
second = []
sort_list = []
for item in unsort:
	first.append(item[0])
	second.append(item[1])
for item in unsort:
	sort_list.append((first[second.index(min(second))],min(second)))
	del first[second.index(min(second))]
	del second[second.index(min(second))]
	
print(sort_list)

#Alternate way of doing it
print(sorted(unsort,key=lambda x:x[1]))