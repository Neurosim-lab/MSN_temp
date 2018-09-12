# To run this, first, run source .bashrc & source .bash_profile to load up neuron library in python

from neuron import hoc,h
from netpyne import specs, sim

try:
    from __main__ import cfg  # import SimConfig object with params from parent module
except:
    from MSN_cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module



###############################################################################
# NETWORK PARAMETERS
#cellRule = netParams.importCellParams(label='PT5B_full', conds={'cellType': 'PT', 'cellModel': 'HH_full'},
#	  fileName='cells/PTcell.hoc', cellName='PTcell', cellArgs=[ihMod2str[cfg.ihModel], cfg.ihSlope], soma_0AtOrigin=True)
#	nonSpiny = ['apic_0', 'apic_1']
#netParams.popParams['PT5B'] = {'cellModel': 'HH_full', 'cellType': 'PT', 'ynormRange': layer['5B'], 'numCells':1}
###############################################################################

# Population parameters
netParams = specs.NetParams()   # object of class NetParams to store the network parameters
netParams.sizeX = 500 # x-dimension (horizontal length) size in um
netParams.sizeY = 500
netParams.popParams['D1MSN'] = {'cellModel': 'MSN', 'cellType': 'D1', 'numCells': 100,'xRange': [0,500],'yRange': [0,500]} # add dict with params for this pop 
cellRule_d1=netParams.importCellParams(label='D1MSN', conds={'cellType': 'D1', 'cellModel': 'MSN'}, fileName='d1msn.py', cellName='WTD1')
#cellRule_d1['secs']['soma_0']['spikeGenLoc'] = 0.5
netParams.cellParams['D1MSN'] = cellRule_d1

netParams.popParams['D2MSN'] = {'cellModel': 'MSN', 'cellType': 'D2', 'numCells': 100,'xRange': [0,500],'yRange': [0,500]} # add dict with params for this pop 
cellRule_d2=netParams.importCellParams(label='D2MSN', conds={'cellType': 'D2', 'cellModel': 'MSN'}, fileName='d2msn.py', cellName='WTD2')
#cellRule_d2['secs']['soma_0']['spikeGenLoc'] = 0.5
netParams.cellParams['D2MSN'] = cellRule_d2 

netParams.popParams['FSI'] = {'cellModel': 'FSI', 'cellType': 'Inh', 'numCells': 10} # add dict with params for this pop 
cellRule_fsi=netParams.importCellParams(label='FSI', conds={'cellType': 'Inh', 'cellModel': 'FSI'}, fileName='fsi.py', cellName='FSI')
netParams.cellParams['FSI'] = cellRule_fsi

netParams.lengthConst = 95

# Synaptic mechanism parameters
netParams.synMechParams['AMPAd1'] = {'mod': 'AMPAd1', 'tau_r': 2.2933, 'tau_d': 1.7977, 'gbar': 0.00021}
netParams.synMechParams['GABAd1'] = {'mod': 'GABAd1', 'tau_r': 6.08314833, 'tau_d': 5.16873033,'gbar':0.00144454}
netParams.synMechParams['NMDAd1'] = {'mod': 'NMDAd1', 'tau_r': 2.2312, 'tau_d': 56, 'gbar': cfg.gnmdad1}
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn'}  # excitatory synaptic mechanism
#netParams.synMechParams['GABAd1'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}
netParams.stimSourceParams['AMPAd1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['AMPAd1->D1MSN'] = {'source': 'AMPAd1', 'sec': 'soma_0','conds': {'pop': 'D1MSN'}, 'synsPerConn':6,'synMech':'AMPAd1'}
netParams.stimTargetParams['AMPAd1->D1MSN'] = {'source': 'AMPAd1', 'sec': 'prox','conds': {'pop': 'D1MSN'}, 'synsPerConn':12,'synMech':'AMPAd1'}
netParams.stimTargetParams['AMPAd1->D1MSN'] = {'source': 'AMPAd1', 'sec': 'mid','conds': {'pop': 'D1MSN'}, 'synsPerConn':24,'synMech':'AMPAd1'}
netParams.stimTargetParams['AMPAd1->D1MSN'] = {'source': 'AMPAd1', 'sec': 'dist','conds': {'pop': 'D1MSN'}, 'synsPerConn':54,'synMech':'AMPAd1'}
netParams.stimSourceParams['GABAd1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['GABAd1->D1MSN'] = {'source': 'GABAd1', 'sec':'soma_0','conds': {'pop': 'D1MSN'}, 'synsPerConn':6,'synMech':'GABAd1'}
netParams.stimTargetParams['GABAd1->D1MSN'] = {'source': 'GABAd1', 'sec':'prox','conds': {'pop': 'D1MSN'}, 'synsPerConn':12,'synMech':'GABAd1'}
netParams.stimTargetParams['GABAd1->D1MSN'] = {'source': 'GABAd1', 'sec':'mid','conds': {'pop': 'D1MSN'}, 'synsPerConn':24,'synMech':'GABAd1'}
netParams.stimTargetParams['GABAd1->D1MSN'] = {'source': 'GABAd1', 'sec':'dist','conds': {'pop': 'D1MSN'}, 'synsPerConn':54,'synMech':'GABAd1'}
netParams.stimSourceParams['NMDAd1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['NMDAd1->D1MSN'] = {'source': 'NMDAd1', 'sec':'soma_0','conds': {'pop': 'D1MSN'}, 'synsPerConn':18,'synMech':'NMDAd1'}
netParams.stimTargetParams['NMDAd1->D1MSN'] = {'source': 'NMDAd1', 'sec':'prox','conds': {'pop': 'D1MSN'}, 'synsPerConn':36,'synMech':'NMDAd1'}
netParams.stimTargetParams['NMDAd1->D1MSN'] = {'source': 'NMDAd1', 'sec':'mid','conds': {'pop': 'D1MSN'}, 'synsPerConn':72,'synMech':'NMDAd1'}
netParams.stimTargetParams['NMDAd1->D1MSN'] = {'source': 'NMDAd1', 'sec':'dist','conds': {'pop': 'D1MSN'}, 'synsPerConn':138,'synMech':'NMDAd1'}


netParams.synMechParams['AMPAd2'] = {'mod': 'AMPAd2', 'tau_r': 2.3739, 'tau_d': 1.930833, 'gbar': 0.0023}
netParams.synMechParams['GABAd2'] = {'mod': 'GABAd2', 'tau_r': 2.357801, 'tau_d': 7.774735,'gbar':0.0080164}
netParams.synMechParams['NMDAd2'] = {'mod': 'NMDAd2', 'tau_r': 2.2312, 'tau_d': 56, 'gbar': cfg.gnmdad2}
#netParams.synMechParams['GABAd2'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}
netParams.stimSourceParams['AMPAd2'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['AMPAd2->D1MSN'] = {'source': 'AMPAd2', 'sec': 'soma_0','conds': {'pop': 'D2MSN'}, 'synsPerConn':6,'synMech':'AMPAd2'}
netParams.stimTargetParams['AMPAd2->D1MSN'] = {'source': 'AMPAd2', 'sec': 'prox','conds': {'pop': 'D2MSN'}, 'synsPerConn':12,'synMech':'AMPAd2'}
netParams.stimTargetParams['AMPAd2->D1MSN'] = {'source': 'AMPAd2', 'sec': 'mid','conds': {'pop': 'D2MSN'}, 'synsPerConn':24,'synMech':'AMPAd2'}
netParams.stimTargetParams['AMPAd2->D1MSN'] = {'source': 'AMPAd2', 'sec': 'dist','conds': {'pop': 'D2MSN'}, 'synsPerConn':58,'synMech':'AMPAd2'}
netParams.stimSourceParams['GABAd2'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['GABAd2->D1MSN'] = {'source': 'GABAd2', 'sec':'soma_0','conds': {'pop': 'D2MSN'}, 'synsPerConn':6,'synMech':'GABAd2'}
netParams.stimTargetParams['GABAd2->D1MSN'] = {'source': 'GABAd2', 'sec':'prox','conds': {'pop': 'D2MSN'}, 'synsPerConn':12,'synMech':'GABAd2'}
netParams.stimTargetParams['GABAd2->D1MSN'] = {'source': 'GABAd2', 'sec':'mid','conds': {'pop': 'D2MSN'}, 'synsPerConn':24,'synMech':'GABAd2'}
netParams.stimTargetParams['GABAd2->D1MSN'] = {'source': 'GABAd2', 'sec':'dist','conds': {'pop': 'D2MSN'}, 'synsPerConn':54,'synMech':'GABAd2'}
netParams.stimSourceParams['NMDAd2'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['NMDAd2->D1MSN'] = {'source': 'NMDAd2', 'sec':'soma_0','conds': {'pop': 'D2MSN'}, 'synsPerConn':18,'synMech':'NMDAd2'}
netParams.stimTargetParams['NMDAd2->D1MSN'] = {'source': 'NMDAd2', 'sec':'prox','conds': {'pop': 'D2MSN'}, 'synsPerConn':36,'synMech':'NMDAd2'}
netParams.stimTargetParams['NMDAd2->D1MSN'] = {'source': 'NMDAd2', 'sec':'mid','conds': {'pop': 'D2MSN'}, 'synsPerConn':72,'synMech':'NMDAd2'}
netParams.stimTargetParams['NMDAd2->D1MSN'] = {'source': 'NMDAd2', 'sec':'dist','conds': {'pop': 'D2MSN'}, 'synsPerConn':138,'synMech':'NMDAd2'}


netParams.synMechParams['AMPAf'] = {'mod': 'AMPAf', 'tau_r': 0.67, 'tau_d': 1, 'gbar': 0.000364}
netParams.synMechParams['GABAf'] = {'mod': 'GABAf', 'tau_r': 1.33, 'tau_d': 4,'gbar':0.00005}
netParams.stimSourceParams['AMPAf'] = {'type': 'NetStim', 'rate': 20, 'noise': 0.5, 'start': 1}
netParams.stimSourceParams['GABAf'] = {'type': 'NetStim', 'rate': 20, 'noise': 0.5, 'start': 1}
netParams.stimTargetParams['GABAf->FSI'] = {'source': 'GABAf', 'sec':'soma_0','conds': {'pop': 'FSI'}, 'synsPerConn':93,'synMech':'GABAf'}
netParams.stimTargetParams['AMPAf->FSI'] = {'source': 'AMPAf', 'sec':'soma_0','conds': {'pop': 'FSI'}, 'synsPerConn':127,'synMech':'AMPAf'}

#netParams_d1.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': 100, 'dur': 1000, 'amp': 0.2}
#netParams_d1.stimTargetParams['Input_1->D1MSN'] = {'source': 'Input_1', 'sec':'soma_0', 'loc': 0.8, 'conds': {'pop':'D1MSN', 'cellList': range(10)}}

netParams.stimSourceParams['Input_4'] = {'type': 'NetStim', 'rate': 10, 'number': 2, 'start': 1, 'noise': 0.2,'dur': 250}
netParams.stimSourceParams['Input_down1'] = {'type': 'NetStim', 'rate': 1, 'number': 2, 'start': 1, 'noise': 0.2,'dur': 250}
netParams.stimSourceParams['Input_d'] = {'type': 'NetStim', 'rate': 10, 'number': 2, 'start': 500, 'noise': 0.2,'dur':250}
netParams.stimSourceParams['Input_down2'] = {'type': 'NetStim', 'rate': 1, 'number': 2, 'start': 750, 'noise': 0.2,'dur': 250}
netParams.stimSourceParams['Input_d2'] = {'type': 'NetStim', 'rate': 10, 'number': 2, 'start': 1000, 'noise': 0.2,'dur':250}
netParams.stimSourceParams['Input_down3'] = {'type': 'NetStim', 'rate': 1, 'number': 2, 'start': 1250, 'noise': 0.2,'dur': 250}
#netParams.stimTargetParams['Input_4->D1MSN'] = {'source': 'Input_4', 'sec':'soma_0', 'conds': {'pop':'D1MSN', 'cellList': range(20)},'synMech': 'exc'}
#netParams.stimTargetParams['Input_4->D2MSN'] = {'source': 'Input_4', 'sec':'soma_0','conds': {'pop':'D2MSN', 'cellList': range(20)},'synMech': 'exc'}
netParams.stimTargetParams['Input4->FSI'] = {
        'source': 'Input_4',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'FSI', 'cellList': range(10)},
        'synPerConn':1,
        'synMech': 'AMPAf','dur': 250}
        
netParams.stimTargetParams['Input4->D1'] = {
        'source': 'Input_4',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
		'synsPerConn':cfg.ampan01,'synMech': 'AMPAd1','dur': 250}

netParams.stimTargetParams['Input4->D2'] = {
        'source': 'Input_4',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
		'synsPerConn':cfg.ampan02,'synMech': 'AMPAd2','dur': 250}

netParams.stimTargetParams['Input4->D1'] = {
        'source': 'Input_4',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan01,'synMech': 'NMDAd1','dur': 250}

netParams.stimTargetParams['Input4->D2'] = {
        'source': 'Input_4',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan02,'synMech': 'NMDAd2','dur': 250}

netParams.stimTargetParams['Input_d->FSI'] = {
        'source': 'Input_d',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'FSI', 'cellList': range(10)},
        'synPerConn':1,
        'synMech': 'AMPAf','dur': 250}
        
netParams.stimTargetParams['Input_d->D1'] = {
        'source': 'Input_d',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.ampan01,'synMech': 'AMPAd1','dur': 250}

netParams.stimTargetParams['Input_d->D2'] = {
        'source': 'Input_d',
        'sec':'soma_0',
        'delay': 1,
        'weight':1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.ampan02,'synMech': 'AMPAd2','dur': 250}

netParams.stimTargetParams['Input_d->D1'] = {
        'source': 'Input_d',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan01,'synMech': 'NMDAd1','dur': 250}

netParams.stimTargetParams['Input_d->D2'] = {
        'source': 'Input_d',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan01,'synMech': 'NMDAd2','dur': 250}

netParams.stimTargetParams['Input_d2->FSI'] = {
        'source': 'Input_d2',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'FSI', 'cellList': range(10)},
        'synPerConn':1,
        'synMech': 'AMPAf','dur': 250}
        
netParams.stimTargetParams['Input_d2->D1'] = {
        'source': 'Input_d2',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.ampan01,'synMech': 'AMPAd1','dur': 250}

netParams.stimTargetParams['Input_d2->D2'] = {
        'source': 'Input_d2',
        'sec':'soma_0',
        'delay': 1,
        'weight':1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.ampan02,'synMech': 'AMPAd2','dur': 250}

netParams.stimTargetParams['Input_d2->D1'] = {
        'source': 'Input_d2',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan01,'synMech': 'NMDAd1','dur': 250}

netParams.stimTargetParams['Input_d2->D2'] = {
        'source': 'Input_d2',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan02,'synMech': 'NMDAd2','dur': 250}
    
netParams.stimTargetParams['Input_down1->FSI'] = {
        'source': 'Input_down1',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'FSI', 'cellList': range(10)},
        'synPerConn':1,
        'synMech': 'AMPAf','dur': 250}
        
netParams.stimTargetParams['Input_down1->D1'] = {
        'source': 'Input_down1',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.ampan01,'synMech': 'AMPAd1','dur': 250}

netParams.stimTargetParams['Input_down1->D2'] = {
        'source': 'Input_down1',
        'sec':'soma_0',
        'delay': 1,
        'weight':1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.ampan02,'synMech': 'AMPAd2','dur': 250}   

netParams.stimTargetParams['Input_down1->D1'] = {
        'source': 'Input_down1',
        'sec':'soma_0',
        'delay': 1,
        'conds': {'pop':'D1MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan01,'synMech': 'NMDAd1','dur': 250}

netParams.stimTargetParams['Input_down1->D2'] = {
        'source': 'Input_down1',
        'sec':'soma_0',
        'delay': 1,
        'weight':1,
        'conds': {'pop':'D2MSN', 'cellList': range(100)},
        'synsPerConn':cfg.nmdan02,'synMech': 'NMDAd2','dur': 250}   

# netParams.stimTargetParams['Input_down2->FSI'] = {
#         'source': 'Input_down2',
#         'sec':'soma_0',
#         'delay': 1,
#         'conds': {'pop':'FSI', 'cellList': range(10)},
#         'synPerConn':127,
#         'synMech': 'AMPAf','dur': 250}
        
# netParams.stimTargetParams['Input_down2->D1'] = {
#         'source': 'Input_down2',
#         'sec':'soma_0',
#         'delay': 1,
#         'conds': {'pop':'D1MSN', 'cellList': range(100)},
#         'synsPerConn':96,'synMech': 'AMPAd1','dur': 250}

# netParams.stimTargetParams['Input_down2->D2'] = {
#         'source': 'Input_down2',
#         'sec':'soma_0',
#         'delay': 1,
#         'weight':1,
#         'conds': {'pop':'D2MSN', 'cellList': range(100)},
#         'synsPerConn':96,'synMech': 'AMPAd2','dur': 250} 

# netParams.stimTargetParams['Input_down2->D1'] = {
#         'source': 'Input_down2',
#         'sec':'soma_0',
#         'delay': 1,
#         'conds': {'pop':'D1MSN', 'cellList': range(100)},
#         'synsPerConn':96,'synMech': 'NMDAd1','dur': 250}

# netParams.stimTargetParams['Input_down2->D2'] = {
#         'source': 'Input_down2',
#         'sec':'soma_0',
#         'delay': 1,
#         'weight':1,
#         'conds': {'pop':'D2MSN', 'cellList': range(100)},
#         'synsPerConn':96,'synMech': 'NMDAd2','dur': 250} 

# netParams.stimTargetParams['Input_down3->FSI'] = {
#         'source': 'Input_down3',
#         'sec':'soma_0',
#         'delay': 1,
#         'conds': {'pop':'FSI', 'cellList': range(10)},
#         'synPerConn':127,
#         'synMech': 'AMPAf','dur': 250}
        
# netParams.stimTargetParams['Input_down3->D1'] = {
#         'source': 'Input_down3',
#         'sec':'soma_0',
#         'delay': 1,
#         'conds': {'pop':'D1MSN', 'cellList': range(100)},
#         'synsPerConn':96,'synMech': 'AMPAd1','dur': 250}

# netParams.stimTargetParams['Input_down3->D2'] = {
#         'source': 'Input_down3',
#         'sec':'soma_0',
#         'delay': 1,
#         'weight':1,
#         'conds': {'pop':'D2MSN', 'cellList': range(100)},
#         'synsPerConn':96,'synMech': 'AMPAd2','dur': 250}   

# netParams.stimTargetParams['Input_down3->D1'] = {
#         'source': 'Input_down3',
#         'sec':'soma_0',
#         'delay': 1,
#         'conds': {'pop':'D1MSN', 'cellList': range(100)},
#         'synsPerConn':264,'synMech': 'NMDAd1','dur': 250}

# netParams.stimTargetParams['Input_down3->D2'] = {
#         'source': 'Input_down3',
#         'sec':'soma_0',
#         'delay': 1,
#         'weight':1,
#         'conds': {'pop':'D2MSN', 'cellList': range(100)},
#         'synsPerConn':264,'synMech': 'NMDAd2','dur': 250}   
# netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.1}
# netParams.stimTargetParams['bkg->D1'] = {'source': 'bkg', 'conds': {'celltype':'D1'}, 'sec':'soma_0','synsPerConn':10,'synMech': 'exc'}
# netParams.stimTargetParams['bkg->D2'] = {'source': 'bkg', 'conds': {'celltype':'D2'}, 'sec':'soma_0','synsPerConn':10,'synMech': 'exc'}
# netParams.stimTargetParams['bkg->FSI'] = {'source': 'bkg', 'conds': {'celltype':'Inh'},'synMech': 'exc','weight':0.5}
# Connectivity parameters
netParams.connParams['D1MSN->D1MSN'] = {
    'preConds': {'pop': 'D1MSN'}, 
    'postConds': {'pop': 'D1MSN'},
    'sec':'soma_0',
    'synsPerConn':1,
    'synMech':'GABAd1',                    # weight of each connection
    'delay': '5',     # delay min=0.2, mean=13.0, var = 1.4
    'probability': 'exp(-dist_2D/lengthConst)'}
    
netParams.connParams['D2MSN->D2MSN'] = {
    'preConds': {'pop': 'D2MSN'}, 
    'postConds': {'pop': 'D2MSN'},
    'sec':'soma_0',
    'synsPerConn':1,
    'synMech':'GABAd2',                    # weight of each connection
    # delay min=0.2, mean=13.0, var = 1.4
    'probability': 'exp(-dist_2D/lengthConst)'}

netParams.connParams['D1MSN->D2MSN'] = {
    'preConds': {'pop': 'D1MSN'}, 
    'postConds': {'pop': 'D2MSN'},
    'sec':'soma_0',
    'synsPerConn':1,
    'synMech':'AMPAd2',                   # weight of each connection
    # delay min=0.2, mean=13.0, var = 1.4
    'probability': 'exp(-dist_2D/lengthConst)'}

netParams.connParams['D1MSN->D2MSN'] = {
    'preConds': {'pop': 'D1MSN'}, 
    'postConds': {'pop': 'D2MSN'},
    'sec':'soma_0',
    'synsPerConn':5,
    'synMech':'NMDAd2',                   # weight of each connection
     # delay min=0.2, mean=13.0, var = 1.4
    'probability': 'exp(-dist_2D/lengthConst)'}

netParams.connParams['FSI->D1MSN'] = {
    'preConds': {'pop': 'FSI'}, 
    'postConds': {'pop': 'D1MSN'},
    'sec':'soma_0',
    'synsPerConn':1,
    'synMech':'GABAd1',                   # weight of each connection
     # delay min=0.2, mean=13.0, var = 1.4
    'probability': 0.55}

netParams.connParams['FSI->D2MSN'] = {
    'preConds': {'pop': 'FSI'}, 
    'postConds': {'pop': 'D2MSN'},
    'sec':'soma_0',
    # 'weight':10,
    'synsPerConn':1,
    'synMech':'GABAd2',                    # weight of each connection
                    # delay min=0.2, mean=13.0, var = 1.4
    'probability': 0.55}

# netParams.connParams['bg->FSI'] = {
#         'preConds': {'pop': 'background'},
#         'postConds': {'pop':'FSI'}, # background -> S,M with ynrom in range 0.1 to 0.6
#         'synsPerConn':10,
#         'synMech':'exc',                    # target synaptic mechanism
#         'weight': 1}                                        # synaptic weight

# netParams.connParams['bg->D2MSN'] = {
#         'preConds': {'pop': 'background'},
#         'postConds': {'pop':'D2MSN'},
#         'sec':'soma_0', # background -> S,M with ynrom in range 0.1 to 0.6
#         'synsPerConn':10,
#         'synMech':'AMPAd2',                    # target synaptic mechanism
#         'weight': 10                                        # synaptic weight
#         }

# netParams.connParams['bg->D1MSN'] = {
#         'preConds': {'pop': 'background'},
#         'postConds': {'pop':'D1MSN'},
#         'sec':'soma_0', # background -> S,M with ynrom in range 0.1 to 0.6
#         'synsPerConn':10,
#         'synMech':'AMPAd1',                    # target synaptic mechanism
#         'weight': 10                                        # synaptic weight
#         }

