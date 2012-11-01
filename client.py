# -*- coding:utf-8 -*- #
# :(){:&:};:

import sys
import turtle
import json
import uuid	
import numpy
import random

class IATron : 
	def __init__(self, n, m, t):
		print '>>> IA TRON LOADING .........'
		if(n%2==1) :
			n += 1
		if(m%2==1) :
			m += 1
		self.n   = n
		self.m   = m
		self.t   = t
		self.c   = 0
		self.v   = 0
		self.s   = []
		for i in range(t):
			self.map = [[0 for x in xrange(n*10)] for x in xrange(m*10)]
			self.core();

	def statistics(self):		
		print '        STATISTIQUES        '
		print '============================'
		(self.s).sort()
		r = (len(self.s)*[0])
		j = 0;
		for i in range(len(self.s)):
			j += 1
			while((self.s).count(i)!=0):
				(self.s).remove(i)
				r[j]=r[j]+1
		for i in range(len(r)):
			if(r[i]!=0):
				print ' @ '+str(i-1)+' : '+str(r[i])

		print '>>> '+str(self.c)+' test'
		print '>>> '+str((self.v)/(self.c))+' coups moyenne'

	def display(self, x):
		if(x!=0) :
			if(x==1) :
				turtle.setheading(0)
			if(x==2) :
				turtle.setheading(270)
			if(x==3) :
				turtle.setheading(180)
			if(x==4) :
				turtle.setheading(90)
			turtle.fd(100);

	def core(self):
		turtle.screensize(10000,10000)
		turtle.clearscreen()
		q = self.n/2
		p = self.m/2
		x = 0
		y = 0
		while(self.map[p][q]!=1) :
			self.map[p][q]=1
			self.display(x)
			x = random.randint(1, 4)
			if(x==1) :
				q += 1
			if(x==2) :
				p -= 1
			if(x==3) :
				q -= 1
			if(x==4) :
				p += 1
			y += 1
		print '>>> ESSAI '+str(self.c)
		print '>>> Nombre de coups : '+str(y)
		(self.s).append(y)
		self.v += y
		self.c += 1
		self.t -= 1

if __name__ == '__main__':
	n = int(raw_input('n     : '))
	m = int(raw_input('m     : '))
	t = int(raw_input('times : '))
	i = IATron(n, m, t)
	i.statistics()