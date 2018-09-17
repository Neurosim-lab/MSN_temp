from netpyne import specs

cfg = specs.SimConfig()
cfg.duration = 1500 # Duration of the simulation, in ms
cfg.dt = 0.05 # Internal integration timestep to use
cfg.seeds = {'conn': 1, 'stim': 1, 'loc': 1} 
cfg.createNEURONObj = 1  # create HOC objects when instantiating network
cfg.createPyStruct = 1  # create Python structure (simulator-independent) when instantiating network
cfg.verbose = False  # show detailed messages 

# Recording 
cfg.recordCells = [1]  # which cells to record from
cfg.recordTraces = {'Vsoma_0':{'sec':'soma_0','loc':0.5,'var':'v'}}
cfg.recordStim = True  # record spikes of cell stims
cfg.recordStep = 0.1 # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.hParams = {'v_init': -80.0}

cfg.filename = 'MSN_net'  # Set file output name
cfg.saveJson = True 	
cfg.printPopAvgRates = False
#cfg.analysis['plotRaster'] = {'saveFig': True} 			# Plot a raster
#cfg.analysis['plotSpikeStats']={'include' : ['allCells'], 'timeRange' : None, 'graphType': 'boxplot', 'stats' : ['rate', 'isicv'], 'saveData' : 'stat.json', 'saveFig' : 'spikes', 'showFig' : False}
cfg.analysis['plotRaster'] = {'include' : ['allCells'], 'timeRange' : None, 'maxSpikes' : 1e8, 'orderBy' : 'gid', 'orderInverse' : False, 'labels' : 'legend', 'saveData' : False, 'saveFig' : True, 'showFig' : False}
cfg.analysis['plotTraces'] = {'include': [('D1MSN',0),('D2MSN',0),('FSI',0)],'saveFig': True} 		# Plot recorded traces for this list of cells

# Variable parameters (used in netParams)
cfg.gnmdad1 = 0.001
cfg.gnmdad2 = 0.005
cfg.fred1 = 10
cfg.fred2 = 10
cfg.nmdan01 = 1
cfg.nmdan02 = 1