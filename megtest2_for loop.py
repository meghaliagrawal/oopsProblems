# for loop
code = 34
if code == 1:
	mylist = [1,2,3,4,5,6,7,8,9,10]
	sum = 0
	for num in mylist:
		if (num%2 == 0):
			sum = sum + num
		else:
			sum = sum + num
	print (sum)
	#for loop with if else condition

elif code == 2:
	mylist= [(1,2),(3,4),(5,6),(7,8)]
	for (a,b) in mylist:
		print (a)
		print (b)
	# this is called tuple unpacking
	
elif code == 3:
	d1= {'k1': 23, 'k2': 56, 'k3': 10, 'k4': 33}
	for (values) in d1.values():
		print (values)
		#use of for loop with dictioneries
		
elif code == 4:
	x=0
	while x<11:
		print (x)
		x +=1
	else:
		print ('x is no longer less than 11')
		# use of while loop with else
		
elif code == 5:
	x = [1,2,3,4,5]
	for num in x:
		if (num ==4):
			break
		else:
			print (num)
	#use of break in for loop
	
elif code == 6:
	mystring = ('Meghali')
	for letter in mystring:
		if (letter == 'g'):
			continue
		print (letter)
	#use of continue in for loop
	
elif code == 7:
		for num in range(1,10,2):
			print(num)
elif code == 8:
	list1 = list(range(0,10,2))
	print (list1)
	#use of Range operator
	
elif code ==9:
	count = 0
	word = "abcde"
	for letter in word:
		print('at count {} the letter is {}'.format(count,letter))
		count += 1
		
elif code == 10:
	count = 0
	word = 'abcde'
	for letter in word:
		print(word[count])
		count+=1
	
elif code == 11:
	word = 'abcde'
	a= [1,2]
	for index,letter in enumerate(a):
		print(letter)
	#use of enumerate operator
	
elif code == 12:
	x = (1,2,3)
	print(type(x))
	y = ['a', 'b','c','d']
	list1 = list(zip(x,y))
	print (list1)
	#use of zip operator
	
elif code == 13:
	x = (1,2,3)
	y = ('a', 'b','c','d')
	for p,q in zip(x,y):
		print(q)
		
elif code == 14:
	print('x' in ('x','y'))
	#use of in opeartor
	
elif code ==15:
	mylist = [1,2,3,4]
	print (max(mylist))
	#use of min & max function
	
elif code==16:
	from random import shuffle
	x= [1,2,3,4]
	shuffle(x)
	print (x)
	# importing shuffle function from Random library

elif code==17:
	from random import randint
	print (randint(0,100))
	# importing Randint function from Random library
	
elif code ==18:
	x = float(input('your lucky no:'))
	print (type(x))
	#use of input function

elif code ==19:
	string1 = 'hello'
	list1 = []
	for letter in string1:
		list1.append(letter)
	print(list1)
		#creating a list by normal for loop method

elif code ==20:
	list1 = [values for values in {'k1':'shyam', 'k2':'ram'}.values()]
	print(list1)
	#list comprehension
		
elif code ==21:
	list1 = [x if x%2==0 else 'odd' for x in range(0,11)]
	print(list1)
	#if & else statements in list comprehension
	
elif code ==22:
	list1 = [x*y for x in [1,2,3] for y in [10,100,1000]]
	print(list1)
	#nested loop statements in list comprehension
	
elif code == 23:
	def sum_func(name = 'default'):
		print(f'hello {name}')
	sum_func("mishka")
	'''print using functions'''

elif code == 24:
	def add_sum(a,b):
		return a+b
	print (add_sum(3,4))
	'''return function'''

elif code == 25:
	def evenlist_chk(list1):
		for num in list1:
			if (num%2 == 0):
				return True
			else:
				pass
		return False
	print (evenlist_chk([1,3,5]))
	#chk for even list through functions


elif code ==26:
	def return_evenlist(list1):
		even_num = []
		for num in list1:
			if (num%2 ==0):
				even_num.append(num)
			else:
				pass
		return even_num
	print (return_evenlist([1,2,3,4,5]))
	# return list of even nos with Pythin functions
	
elif code == 27:
	list1= [('mishka',9.8), ('meghali',57.0), ('saurabh',101.2)]
	def weight_person(list1):
		max_weight = 0
		fatty_person = ''
		for name,weight in list1:
			if weight > max_weight:
				max_weight = weight
				fatty_person = name 
			else:
				pass
		return (max_weight, fatty_person)
	print (weight_person(list1))
	#chk max weight of a person using Python functions
	
elif code == 28:
	from random import shuffle
	def shuffle_list():
		list2 = ['','o','']
		shuffle(list2)
		return list2
	
	def user_guess():
		guess = ''
		guess = input ("pick a number 0,1, or 2 ")
		return int(guess)
	
	def check_guess(list2,guess):
		if list2[guess] == 'o':
			print ('correct answer')
			print (list2)
		else:
			print ('wrong answer!')
			print (f'list is {list2}')
		
	mixedup_list = shuffle_list()
	guess = user_guess()
	check_guess (mixedup_list,guess)
			
		
elif code == 29:
	def sum_func(*args):
		print (sum(args))
		for items in args:
			print (items)
	sum_func(1,2,3,4,5,6)
	#use of *args in functions. * args gives arbitrary no of arguments in the form of tuples.
	
elif code == 30:
	def my_func(**kwargs):
		print (type (kwargs))
		if "fruit" in kwargs:
			print('the fruit is {}'.format(kwargs['fruit']))
		else:
			print ('there is no fruit')
	my_func(fruit = 'apple', veggie = 'peas')
	# use of **kwargs which gives arbitrary no of arguments in the form of dictionaries.
	
elif code == 31:
	def my_func(*args,**kwargs):
		print (args)
		print (kwargs)
		print ('i would like to buy {} {}'.format (args[1], kwargs ['fruits']))
	my_func(10,20,30,fruits = 'mangoes',veggies = 'peas')
	
elif code == 32:
	def myfunc(*args):
		even_list = []
		for value in args:
			if value%2 ==0:
				even_list.append(value)
			else:
				pass
		return even_list
	print (myfunc(1,2,3,4,5,6,7,8))	

elif code == 33:
		def myfunc(name):
			list2 = []
			list1 = list(name)
			length =len(list1)
			for i in range (0,length):
				if i%2 == 0:
					list2.append(list1[i].lower())
				else:
					list2.append(list1[i].upper())
			return str(list2)
		print (myfunc('saurabh'))
			
elif code == 34:
	def square(num):
		return num**2
	my_nums = [1,2,3,4,5]
	for items in map(square,my_nums):
		print (items)
			
		
		
	
	