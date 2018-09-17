from netpyne import specs
from ModBatch import Batch
import numpy as np
def Synnmda():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()
        desc = np.dtype([('gnmdad1', float), ('gnmdad2', float), ('freq1', float),
                 ('freq2', float), ('conn1', int),('conn2', int)])
        data = np.genfromtxt('curr_population.dat', dtype=desc)     
        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['gnmdad1']=list(data['gnmdad1'])
        params['gnmdad2']=list(data['gnmdad2'])
        params['fred1']=list(data['freq1'])
        params['fred2']=list(data['freq2'])
        params['nmdan01']=list(data['conn1'])
        params['nmdan02'] = list(data['conn2'])
        groupedParams = ['gnmdad1', 'gnmdad2', 'fred1', 'fred2', 'nmdan01', 'nmdan02']
        
        # create Batch object with paramaters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='MSN_cfg.py', netParamsFile='MSN_params.py',groupedParams=groupedParams)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'synNMDA'
        b.saveFolder = 'MSN_data'
        b.method = 'grid'
        b.runCfg = {'type': 'hpc_slurm',
                        'allocation': 'msm110',
                        'script': 'MSN_init.py',
                        'walltime': '1:00:00',
                        'nodes': 1,
                        'coresPerNode': 24,
                        'mpiCommand': 'srun --mpi=pmi2',
                        'folder': '/home/hsong1/MSN_temp/',
                        'skip': True}

        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        Synnmda()