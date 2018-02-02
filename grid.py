import numpy as np


def read_nodes(path):
    """
    Read data example and save it
    
    >>> read_nodes("examples/nodes1.csv") 
    array([1, 2, 3, 1, 2, 3, 1, 2])
    """
    arr = np.genfromtxt(path, delimiter = "'", dtype = np.int32)
#    arr = arr.reshape(shape)
    return arr

def gen_edges3d(shape):
    """
    Generate edges
    """
    assert len(shape) == 3
    this_id = 0
    edges = []
    edge_id = np.array(range(np.prod(shape))).reshape(shape)
    for k in range(shape[2]):
        for j in range(shape[1]):
            for i in range(shape[0]):
                new_edges = [(i + 1, j, k), (i - 1, j, k), (i, j + 1, k), (i, j - 1, k), (i, j, k - 1), (i, j, k + 1)]
                new_edges = [(x, y, z) for x, y, z in new_edges if x >= 0 and y >= 0 and z >= 0]
                new_edges = [(x, y, z) for x, y, z in new_edges if x < shape[0] and y < shape[1] and z < shape[2]]
                for x, y, z in new_edges:
                    edges.append([this_id, edge_id[x, y, z]])
                this_id += 1
    return np.array(edges, np.int32)
        

def validate_grid3d_input(nodes):
    """
    Validate grid3d input
    """
    assert isinstance(nodes, np.ndarray), "nodes should be a numpy array"
    assert nodes.ndim == 1, "nodes must have dimension 1"
    

class grid3d:
    """
    A class to contain grids
    
    >>> grid = grid3d(np.arange(24), (2, 3, 4)) # compatible shape
    >>> grid = grid3d(np.arange(24), (2, 3, 5)) 
    Traceback (most recent call last):
        ...
    AssertionError: incompatible shape
    """
    
    """
    Initializer
    """
    def __init__(self, nodes, shape):
        validate_grid3d_input(nodes)
        assert np.prod(shape) == len(nodes), "incompatible shape"
        self.nodes = nodes
        self.edges = gen_edges3d(shape)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        

        
    
    
        
