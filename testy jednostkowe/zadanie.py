#!/usr/bin/env python3.4
from math import acos
from math import sin
from math import pi


# Wypisuje liczby pierwsze z danego zakresu
class Primary:
	def __init__(self,number):
		self.x=1
		self.number = number;

	def isPrime(self,n):
		return n > 1 and all(n%i for i in range(2,n))

	def __iter__(self):
		return self

	def __next__(self):
		self.x+=1
		while(self.isPrime(self.x)==False):
			self.x+=1
		if self.x > self.number:
			raise StopIteration
		return self.x


class Pascal_Triangle:
	def __init__(self,rows):
		self.row=[1.0]
		self.n=0
		self.rows = rows

	def __iter__(self):
		return self

	def __next__(self):
		line = [1.0]
		for k in range(self.n):
			line.append(line[k] * (self.n-k) / (k+1))
		self.n+=1
		if self.n>self.rows:
			raise StopIteration
		return line


#Zwraca losowe liczby od 0 do 1
class montecarlo:
	def __init__(self):
		self.a=44485709377909
		self.m=2**48
		self.c = 0
		self.x=1
		self.n=0.0

	def __iter__(self):
		return self

	def __next__(self):
		self.x=(self.a * self.x + self.c)%self.m
		self.n+=1
		return self.x/self.m



class monte_use:
	def __init__(self):
			TOL = 1e-7
			c=0
			n=1
			mc = montecarlo()

			integra=100
			while abs(2-integra) > TOL:
				x = next(mc)*pi
				y = next(mc)
				if 0<y<=self.func(x):
					c+=1
				if 0>y>=self.func(x):
					c-=1
				integra = pi*(c/n)
				n+=1
			print('\nWynik obliczania calki')
			print(integra)
			print('\nIlosc iteracji, potrzebnych do obliczenia')
			print(n)

	#Funkcja, ktora obliczamy
	def func(self,x):
		return sin(x)


