import androidhelper

droid = androidhelper.Android()

import math


#definiranje klase tocka
class Tocka (object):

	def __init__(self,rbr,y,x,z):
		
		self.rbr = str(rbr)
		self.y = float(y)
		self.x = float(x)
		self.z = float(z)

	def smjerni(self,other):
		
		dy = (other.y)-(self.y)
		dx = (other.x)-(self.x)

		if dx==0.:
		
			if dy==0.:
				s_kut=0.
				return s_kut

			elif other.y<self.y:
				s_kut=math.pi/2.
				return s_kut

			elif self.y<other.y:
				s_kut=math.pi+math.pi/2.
				return s_kut

	#1. kvadrant dy+  dx+
		elif dy>=0. and dx>=0. :
			s_kut=math.atan(dy/dx)
			return s_kut
		

	#2. kvadrant dy+  dx-
		elif dy>=0. and dx<=0.:
			s_kut=math.atan(dy/dx)+math.pi
			return s_kut
		

	#3. kvadrant dy-  dx-
		elif dy<=0. and dx<=0.:
			s_kut=math.atan(dy/dx)+math.pi
			return s_kut
		

	#4. kvadrant dy-  dx+
		elif dy<=0. and dx>=0. :
			s_kut=math.atan(dy/dx)+math.pi*2.
			return s_kut

	#definiranje funkcije duljine
	def duljina(self,other):
		
		dy=(other.y)-(self.y)
		dx=(other.x)-(self.x)
		duljina=math.sqrt(dy**2+dx**2)
		return duljina

	#definiranje zbroja
	def __add__(self,other):
		zbroj = Tocka("zbroj:"+str(self.rbr)+"_"+str(other.rbr), self.y+other.y, self.x+other.x, self.z+other.z)
		return zbroj

	#definiranje printanja tocke
	def __str__(self):
		return str(self.rbr)+" "+str(self.y)+" "+str(self.x)+" "+str(self.z)

	#definiranje oduzimanja
	def __sub__(self, other):
		minus = Tocka("minus:"+str(self.rbr)+"_"+str(other.rbr), self.y-other.y, self.x-other.x, self.z-other.z)
		return minus


A = droid.dialogGetInput("Stajaliste","ime,y,x,h","").result
A_lista = A.split(",")

A = Tocka(A_lista[0],A_lista[1],A_lista[2],A_lista[3])


B = droid.dialogGetInput("Orijentacija","ime,y,x,h","").result
B_lista = B.split(",")

B = Tocka(B_lista[0],B_lista[1],B_lista[2],B_lista[3])


C = droid.dialogGetInput("Detalj","ime,y,x,h","").result
C_lista = C.split(",")

C = Tocka(C_lista[0],C_lista[1],C_lista[2],C_lista[3])


alfa = A.smjerni(C)-A.smjerni(B)

#uvjeti pravca prema detalju
if alfa==0.:
	alfa=0.
elif alfa<0.:
	alfa+=math.pi*2
elif alfa>=2*math.pi:
	alfa-=math.pi*2


d=round(A.duljina(C),3)

kut_DEG=alfa*180/math.pi
kut_D=int(kut_DEG)
temp=60*(kut_DEG-kut_D)
kut_M=int(temp)
kut_S=int(math.ceil(60*(temp-kut_M)))
kut=str(kut_D)+"-"+str(kut_M)+"-"+str(kut_S)

print "duljina  ",d
print "kut  ", kut