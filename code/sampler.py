import numpy as np

# Grid resolution
width = 40
height = 40

# The boundary nodes are more probable to be fixed
# The probability to fix the boundary node is P_b
# The probability to choose the inner node is P_i
# These probabilities are defined as follows
# P_b = prob_factor * P_i
prob_factor = 100.0

basic_config = {
    'DOF_PN': 2,
    'ELEM_K': 'Q4',
    'ETA': '0.5',
    'FILT_RAD': 1.5,
    'NUM_ELEM_Z': 0,
    'NUM_ELEM_X': width,
    'NUM_ELEM_Y': height,
    'PROB_TYPE': 'comp',
    'NUM_ITER': 100,
    'P_FAC': 3.0,
}

        
def random_nodes(n):
    shape = (height + 1, width + 1)
    n_max = shape[0] * shape[1]
    node_args = np.arange(1, n_max + 1)
    
    p_matrix = np.full(shape=shape, fill_value=prob_factor)
    p_matrix[1:-1, 1:-1] = 1.0
    p_matrix /= p_matrix.sum()
    
    probs = p_matrix.T.ravel()
    nodes = np.random.choice(node_args, size=n, 
                             replace=False, p=probs)
    return nodes


def random_config():
    n_fxtr_x = np.random.poisson(2)
    n_fxtr_y = np.random.poisson()
    n_load_y = np.random.poisson()

    config = basic_config.copy()
    config['FXTR_NODE_X'] = random_nodes(n_fxtr_x)
    config['FXTR_NODE_Y'] = random_nodes(n_fxtr_y)
    config['LOAD_NODE_Y'] = random_nodes(n_load_y)
    config['LOAD_VALU_Y'] = [-1] * n_load_y # Augmentation helps
    config['VOL_FRAC'] = np.random.normal(0.5, 0.1)

    return config
