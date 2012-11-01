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
			n = n+1
		if(m%2==1) :
			m = m+1
		self.n   = n
		self.m   = m
		for i in range(t):
			self.map = [[0 for x in xrange(n*10)] for x in xrange(m*10)]
			self.core();

	def options(self):
		print self.n

	def core(self):
		turtle.screensize(10000,10000)
		turtle.clearscreen()
		q = self.n/2
		p = self.m/2
		x = 0
		while(self.map[p][q]!=1) :
			self.map[p][q]=1
			if(x!=0) :
				if(x==1) :
					turtle.setheading(0)
					print "droit"
				if(x==2) :
					turtle.setheading(270)
					print "bas"
				if(x==3) :
					turtle.setheading(180)
					print "gauche"
				if(x==4) :
					turtle.setheading(90)
					print "haut"
				turtle.fd(100);
			x = random.randint(1, 4)
			if(x==1) :
				q += 1
			if(x==2) :
				p -= 1
			if(x==3) :
				q -= 1
			if(x==4) :
				p += 1
		print x

if __name__ == '__main__':
	ia = IATron(5, 5, 5)
	try:
	    mode=int(raw_input('Input:'))
	except ValueError:
	    print "Not a number"