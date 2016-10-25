import sys
import string
import math as m
import time
# import numpy as np
# import scipy as sp
# from sp.special import lambertw

start_time = time.time()

print ("Φ(n) =  'nth' prime number")
n = input("n = ")

# n = 10000

if 0: #allows for the program to be scaled up
	def ln(x): #defines a natural log
	    n = 1000000.0
	    return n * ((x ** (1/n)) - 1)

	def log(x): #defines a log (base 10)
		k = (ln(10))**(-1)
		return ln(x)*k

	if 0: #defins the product of log function in two differnt ways-- both are rather slow 
		if 0:
			def W(x): #defines the product log function (Newton's Method)
				ε = 0.00000001 # max error allowed
				w = x
				while True:
					ew = m.exp(w)
					wNew = w - (w*ew - x)/(w*ew + ew)
					if abs(w - wNew) <== ε: break
				return w
		
		if 0:
			def W(x): #defines the product of log function (numpy & scipy)
				import numpy
				import scipy as sp
				from sp.special import lambertw
				w = lambertw(x, k = 0)
				return w * np.exp(w)

	def frequency_of_primes(x):
		# return int(-x*W(-1/x))
		return int(x*(log(x)**(-1)))

	NaturalNumbers = list(range(frequency_of_primes(n)*10)) #creates list of NaturalNumbers that will have the 'nth' prime number
	# print ("list of natural numbers created...")

if 1:
	NaturalNumbers = list(range(1000 * n)) #non optimal list, but no modules required

def Lucas(k): #this block defines a Lucas number 
    a, b = 2, 1
    for i in range(k):
        a, b = b, a + b
    return a

LucasNumbers = [Lucas(k) for k in NaturalNumbers] #creates a list of the LucasNumbers that appear in the set of NaturealNumbers
# print ("list of Lucas Numbers created...")

def prime(n): #this block defines a prime number
	for i in range(n):
		if (n != 1) and ((LucasNumbers[n] - 1)%n == 0):
			return n 

PrimeNumbers0 = [prime(k) for k in NaturalNumbers] #creates a list of PrimeNumbers that appear in the set of Natural Numbers

# PrimeNumbers = []
# for i in range(100000):
# 	if prime(i):
# 		PrimeNumbers.append(i)
# 	if len(PrimeNumbers0) == n:
# 		break

PrimeNumbers = [s.strip('None') for k in PrimeNumbers0]

print (PrimeNumbers[n - 1]) #this displays the 'nth' prime number

print("---%s seconds ---" % (time.time() - start_time))

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# def prime(n): #this block defines a prime number
# 	for i in range(n):
# 		if (n = 1):
# 			# print ("This is not a prime number.")
# 			hmmm = "proably should make this if statement better"
# 		else:
# 			if ((LucasNumbers[n] - 1)%n != 0):
# 				# print ("This is not a prime number.")
# 				hmmm = "proably should make this if statement better"
# 			else:
# 				# print ("This is a prime number.")
# 				return n

# def prime(n): #this block defines a prime number
# 	for i in range(n):
# 		if (n != 1) and ((LucasNumbers[n] - 1)%n == 0):
# 			return n 
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------


if 0: #the Scott method
	n= input('Which prime number would you like? ')
	n= int(n)

	pList = []
	a, b, c, d, e = 1, 0, 0, 0, 1000000000

	for i in range(e + 1):
	    pList.append(i+2)    

	for x in range(1, e):
	   # print (x)
	    d = pList[x]
	    #print(d)
	    b = 0
	    for y in range(a):
	        c = pList[y]
	       # print (c)
	        if d%c != 0:
	            b = b + 1
	        if b == a:
	            b = 0
	            pList[a] = d
	            a = a + 1
	           # print('stored')
	           # print (d)
	           # print('a=')
	           # print (a)
	    if a == n:
	        print(str(pList[n-1]) + " is the " + str(n) + "th " + "prime number!");
	        quit()