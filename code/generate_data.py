import os
import numpy as np
import topy
from sampler import random_config

DIR_TO_SAVE = './TOP4040'
NUM_SAMPLES = 1
topy.Logger.verbose = False

def optimize(t):
    desvars = []

    for i in range(t.numiter):
        # Main operations
        t.fea()
        t.sens_analysis()
        t.filter_sens_sigmund()
        t.update_desvars_oc()

        desvars.append(t.desvars)
        
    return np.array(desvars)


if __name__ == "__main__":

    if not os.path.exists(DIR_TO_SAVE):
        os.mkdir(DIR_TO_SAVE)

    n_sample = 0
    while n_sample < NUM_SAMPLES:
        try:        
            topology = topy.Topology(config=random_config())
            topology.set_top_params()
            sample = optimize(topology)
        except BaseException: # For the incorrect constraints
            continue
        
        path = os.path.join(DIR_TO_SAVE, str(n_sample))
        np.savez_compressed(path, sample)
        n_sample += 1

