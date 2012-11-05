# -*- coding:utf-8 -*- #
# :(){:&:};:

import sys
import turtle
import random

class IATron : 
	def __init__(self, n, m, t, z):
		print '>>> IA TRON LOADING .........'
		if(n%2==1) :
			n += 1
		if(m%2==1) :
			m += 1
		self.n   = n
		self.m   = m
		self.t   = t
		self.z   = z
		self.c   = 0
		self.v   = 0
		self.s   = []
		for i in range(t):
			self.map = [[0 for x in xrange(n*10)] for x in xrange(m*10)]
			self.core();

	def display(self, x):
		if(x!=0) :
			turtle.setheading(x)
			turtle.fd(self.z*10);

	def randomMode(self, mode):
		return random.randint(1, 360)

	def core(self):
		turtle.screensize(10000,10000)
		turtle.clearscreen()
		turtle.bgcolor("black")

		# select the origin in middle of the map
		q = self.n/2
		p = self.m/2
		
		# origin
		turtle.pencolor("red")
		turtle.fill(True)
		for _ in range(3): turtle.forward(5); turtle.left(120)
		turtle.fill(False)
		
		# init
		x = 0
		y = 0
		
		#while(self.map[p][q]!=1) :
		while(True) :
			self.map[p][q]+=1
			
			# current color
			t = 0;
			if(self.map[p+1][q+1]==1) : t+=1
			if(self.map[p+1][q-1]==1) : t+=1
			if(self.map[p-1][q-1]==1) : t+=1
			if(self.map[p-1][q+1]==1) : t+=1
			if(t==0) : turtle.pencolor("white")
			if(t==1) : turtle.pencolor("green")
			if(t==2) : turtle.pencolor("blue")
			if(t==3) : turtle.pencolor("purple")
			if(t==4) : turtle.pencolor("red")

			# display progression with tk and turtle
			self.display(x)

			# random value
			x = self.randomMode(1)
			if(x>0 and x<=90):
				p += 1
				q += 1
			elif(x>90 and x<=180):
				p += 1
				q -= 1
			elif(x>180 and x<=270):
				p -= 1
				q -= 1
			elif(x>270 and x<=360):
				p -= 1
				q += 1
			else : print '>>>> ERROR !!!'


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
	z = int(raw_input('zoom : '))
	i = IATron(n, m, t, z)
