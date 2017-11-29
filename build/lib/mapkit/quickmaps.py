import pandas as pd
import math
import random
import numpy as np

# function that returns a list of 51 gradient blue to red heatmap 
def get_heatmap51():
	list = ['#0030E5', '#0042E4', '#0053E4', '#0064E4', '#0075E4', '#0186E4', '#0198E3', '#01A8E3', '#01B9E3', '#01CAE3', '#02DBE3', '#02E2D9', '#02E2C8', '#02E2B7', '#02E2A6', '#03E295', '#03E184', '#03E174', '#03E163', '#03E152', '#04E142', '#04E031', '#04E021', '#04E010', '#09E004', '#19E005', '#2ADF05', '#3BDF05', '#4BDF05', '#5BDF05', '#6CDF06', '#7CDE06', '#8CDE06', '#9DDE06', '#ADDE06', '#BDDE07', '#CDDD07', '#DDDD07', '#DDCD07', '#DDBD07', '#DCAD08', '#DC9D08', '#DC8D08', '#DC7D08', '#DC6D08', '#DB5D09', '#DB4D09', '#DB3D09', '#DB2E09', '#DB1E09', '#DB0F0A']
	return list

# from the size of range list makes the colorlist
def make_colorlist(rangelist):
	rangelist = rangelist[:-1]

	if len(rangelist) == 1:
		return [get_heatmap51()[0]]
	elif len(rangelist) == 1:
		return []

	ogcolorlist = get_heatmap51()
	sizedelta = float(len(ogcolorlist)) / float(len(rangelist)-1)

	current = 0.0
	sizebool = False
	newlist = [ogcolorlist[0]]
	while sizebool == False:
		current += sizedelta


		if current >= 50.0  and len(newlist) != len(rangelist):
			newlist.append(ogcolorlist[-1])
		
			sizebool = True
		elif len(newlist) == rangelist and current <= 50.0:
			newlist = newlist[:-1] + ogcolorlist[-1]
			sizebool = True
		elif len(newlist) != rangelist and current >= 50.0:
			newlist.append(ogcolorlist[-1])
			sizebool = True
		else:
			#print len(newlist),len(rangelist),current
			newlist.append(ogcolorlist[int(round(current,0))-1])
	if len(newlist) == len(rangelist):
		return newlist

# creates a random set of numbers within a certain size
def create_ints(size):
	newlist = []
	mydict = {}
	while len(newlist) < size:
		number = random.randint(0,size*1000)
		if mydict.get(number,'') == '':
			newlist.append(number)
			mydict[number] = 1
	return newlist

# makes uniqus from string or categorical data
def make_uniques(data,column):
	# getting uniques
	uniques = data[column].unique()

	# creating dictionary of each hash entry
	keys = create_ints(len(uniques))
	mydict = dict(zip(keys,uniques))
	
	# sorting each hash entry
	keys = sorted(keys)

	# taking the sorted hash entries against the list to make a non-sequential unique list
	# sometimes sequential unique sets lead to multiple objects on the map
	# being the same color or similiir shade due to the sorting mechanism
	uniques = [mydict[i] for i in keys]
	numlists = math.ceil(float(len(uniques)) / 51.0) + 1

	colorlist = []
	colorlistint = get_heatmap51()
	random.shuffle(colorlistint)
	for i in range(int(numlists)):
		colorlist += colorlistint
	colorlist = colorlist[:len(uniques)]

	# creating the colordictionary that will be mapped
	colordict = dict(zip(uniques,colorlist))

	# mapping the colordict onto the corresponding field
	data['COLORKEY'] = data[column].map(lambda x:colordict[x])

	return data

# getting exponents
def get_expons(val):
	if val == 0:
		return [-1,0]
	count = 0
	for i in range(-32,32):
		if count == 0:
			count = 1
		else:
			print 10 ** oldi,10 ** i,val
			if val >= 0:
				if 10 ** oldi <=  val and 10 ** i >= val:
					return [oldi,i]
			else:
				#print val,10 ** abs(oldi),
				if -1 * 10 ** oldi <=  val and -1 * 10 ** i >= val:
					return oldi,i
		oldi = i

#print get_expons(0)

# making exponent numericals rangelist
def make_numeric_exp(data,column,exp_size=2):
	# getting min and max val
	minval,maxval = data[column].min(),data[column].max()
	#minval,maxval = float(minval) - 10 ** -32,float(maxval) + 10 ** -32

	# getting the minimium and maximum exponent
	minexp,maxexp = get_expons(minval)[0],get_expons(maxval)[1]

	# default exp size set at 2
	rangelist = np.linspace(minval,maxval,(((maxexp-minexp) * 2)+1))

	# getting colorlist 
	colorlist = make_colorlist(rangelist.tolist())

	# adding colorkey to list
	data['COLORKEY'] = pd.cut(data[column],bins=rangelist,labels=colorlist)
	data['COLORKEY'] = data.COLORKEY.astype(str)
	return data

# making exponent numericals rangelist
def make_numeric_linear(data,column):
	# getting min and max val
	minval,maxval = data[column].min(),data[column].max()

	# getting the minimium and maximum exponent
	minexp,maxexp = get_expons(minval)[0],get_expons(maxval)[1]

	# default exp size set at 2
	rangelist = np.linspace(minval,maxval,52)

	# getting colorlist 	
	colorlist = get_heatmap51()

	# adding colorkey to list
	data['COLORKEY'] = pd.cut(data[column],bins=rangelist,labels=colorlist)
	data['COLORKEY'] = data.COLORKEY.astype(str)
	return data

# makes colorkey from input of kwargs assumes categorical at first
# has 4 options: make_uniques(),make_numeric_exp(),make_numeric_linear(),make_dict_key()
def make_colorkey(data,column,linear=False,exp=False,dict_key=False,exp_size=2):
	# logic for linear
	if linear == True:
		return make_numeric_linear(data,column)
	elif exp == True:
		return make_numeric_exp(data,column,exp_size=2)
	elif dict_key == True:
		# mapping the colordict onto the corresponding field
		data['COLORKEY'] = data[column].map(lambda x:colordict[x])
		return data
	else:
		return make_uniques(data,column)



