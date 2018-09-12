import sys
from neuron import h, hoc
from math import sqrt, pi, log, exp
Ra=100
ek=-90
ena=45

class FSI:
	def __init__(self):
		self.create_cell()

		self.optimize_nseg()
		self.settopo()
		self.add_all()
		self.setchannels()


	def create_cell(self):
		self.soma = [h.Section(name='soma[%d]' % i) for i in xrange(1)]
		
		h.pt3dclear(sec = self.soma[0])
		h.pt3dadd(0,0,0,1, sec = self.soma[0])
		h.pt3dadd(15,0,0,1, sec = self.soma[0])

	def optimize_nseg (self):
		self.all=h.SectionList()
		for section in self.soma:
			self.all.append(sec=section)
		
		for sec in self.all:
			sec.Ra=100
			sec.cm=1		
	
	def settopo(self):
		#### set L and diam
		self.soma[0].L=10
		self.soma[0].diam=10
  
	def add_all(self):
		for sec in self.all:
			sec.insert('pas')
			#sec.insert('naffsi')
			sec.insert('nas')
			sec.insert('kv')
			sec.insert('kdrfsi')
		
	def setchannels(self):
		for sec in self.all:
			sec.g_pas=0.0004
			sec.e_pas=-75
			#sec.gna_naffsi=0.1125
			sec.gna_nas=1.4
			sec.gkdr_kdrfsi=0.02
			sec.gkv_kv=0.00375



	    
	    
    	
    		
    	
    	
    	
        
        
        
        
        
        
        
