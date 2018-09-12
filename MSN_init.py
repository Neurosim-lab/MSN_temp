from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='MSN_cfg.py', netParamsDefault='MSN_params.py')					

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)