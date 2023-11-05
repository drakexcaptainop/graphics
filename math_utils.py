import numpy as np

def create_rotation_matrix( alpha, axis='x' ):
    B = np.sin( alpha )
    A = np.cos( alpha )
    if axis == 'x':
        matrix = np.array(
            [[1, 0, 0, 0],
             [0, A, B, 0],
             [0, -B, A, 0],
             [0, 0, 0, 1]]
        ) 
    elif axis == 'y':
        matrix = np.array(
            [[A, 0, B, 0],
             [0, 1, 0, 0],
             [-B, 0, A, 0],
             [0, 0, 0, 1]]
        ) 
    elif axis == 'z':
        matrix = np.array(
            [[A, B, 0, 0],
             [-B, A, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        ) 
    else:
        raise Exception( f'Invalid {axis=}, only "x, y, z" are valid' )
    
    return matrix

def proyspace2screen( coords, w, h ):
    scale_factors = np.array( [ w/2, h/2 ] )
    if np.iterable( coords[0] ):
        for i in range(len(coords)):
            coords[i][:2] = (coords[i][:2] + 1)*scale_factors
        return coords
    else:
        return (coords + 1)*scale_factors
