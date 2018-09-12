from netpyne import specs
from ModBatch import Batch
import numpy as np

def Synnmda():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        #params['gnmdad1'] = list(np.linspace(0.001,0.05,20))
        #params['gnmdad2'] = list(np.linspace(0.01,0.02,20))
        params['ampan01'] = [1,2,3]
        params['ampan02'] = [1,2,3]
        # params['nmdan01'] = [1,2,3,4,5]
        # params['nmdan02'] = [1,2,3,4,5]
        # create Batch object with paramaters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='MSN_cfg.py', netParamsFile='MSN_params.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'synNMDA'
        b.saveFolder = 'MSN_data'
        b.method = 'grid'
        b.runCfg = {'type': 'hpc_slurm',
                        'allocation': 'shs100',
                        'script': 'MSN_init.py',
                        'walltime': '1:00:00',
                        'nodes': 1,
                        'coresPerNode': 24, 
                        'mpiCommand': 'ibrun',
                        'folder': '/u/salvadord/MSN/',
                        'skip': True}

        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        Synnmda()
          
                            