# -*- coding:utf-8 -*- #
# :(){:&:};:

import sys
import turtle
import random

class IATron : 
	def __init__(self, t, z):
		
		# initial params
		# t : times
		# z : zoom

		self.n     = 20
		self.m     = 20
		self.t     = t
		self.z     = z
		self.trace = []
		for i in range(t):
			self.map = [[0 for x in xrange(self.n*10)] for x in xrange(self.m*10)]
			self.core();

	def display(self, x):
		if(x!=0) :
			# Direction of turtle
			if(x==1) :
				turtle.setheading(0)
			if(x==2) :
				turtle.setheading(270)
			if(x==3) :
				turtle.setheading(180)
			if(x==4) :
				turtle.setheading(90)
			# Mouvement of turtle
			turtle.fd(self.z*10);

	def randomMode(self, mode):
		return random.randint(1, 4);

	def ia(self):
		return True

	def addTrace(self, p, q):
		if(len(self.trace)==10) :
			(self.trace).pop(0)
		(self.trace).append([p, q])

	def core(self):
		turtle.clearscreen()
		p = v = 100
		q = z = 100
		# 
		x = 0
		# mouvement
		while(self.map[p][q]!=1) :
			if(x!=0):
				if(len(self.trace)!=0) :
					for l in self.trace :
						b = True;
						if([v, z]==l):
							b = False
					if(b) :
						p = v
						q = z
						self.map[p][q]=1
						self.addTrace(p, q)
						self.display(x)
					else :
						v = p
						q = z
				else :
					self.map[p][q]=1
					self.addTrace(p, q)
					self.display(x)

			x = self.randomMode(1)
			if(x==1) :
				v += 1
			if(x==2) :
				z -= 1
			if(x==3) :
				v -= 1
			if(x==4) :
				z += 1

if __name__ == '__main__':
	t = int(raw_input('times : '))
	z = int(raw_input('zoom : '))
	i = IATron(t, z)
