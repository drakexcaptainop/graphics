import numpy as np

class Proyector:
    def __init__(self, alpha, fc, ar) -> None:
        self.proyection_matrix = None
        self._build_proyection_matrix( alpha, fc, ar )
       
    
    def _build_proyection_matrix(self, alpha, fc, ar):
        nc = 1/np.tan( alpha )
        A = (fc+nc)/(fc-nc)
        B = 2*nc*fc/(nc-fc)

        self.nc = nc
        self.alpha = alpha
        self.fc = fc 
        self.ar = ar
        self.proyection_matrix = np.array( 
            [ [ nc * ar, 0, 0, 0],
              [ 0, nc, 0 ,0],
              [ 0, 0, A, B],
              [ 0, 0, 1, 0] ]
         )

    def proyect_vec(self, vector):
        pass
    
    def proyect_tri(self, vertices: list[list]):
        v1 = self.proyection_matrix@vertices[0]
        v2 = self.proyection_matrix@vertices[1]
        v3 = self.proyection_matrix@vertices[2]
        
        v1 /= v1[-1]
        v2 /= v2[-1]
        v3 /= v3[-1]

        return v1, v2, v3
    
    def proyect_mesh(self, mesh: 'Mesh', vecOff):
        proyected_coords = []
        for face in mesh:
            if mesh.stride == 3:
                for pv in self.proyect_tri( face + vecOff ):
                    proyected_coords.append( pv )

            if mesh.stride == 4:
                for pv in self.proyect_quad( face + vecOff ):
                    proyected_coords.append( pv ) 
        
        return proyected_coords
    
    def proyect_quad(self, vertices: list[list]):
        v1 = self.proyection_matrix@vertices[0]
        v2 = self.proyection_matrix@vertices[1]
        v3 = self.proyection_matrix@vertices[2]
        v4 = self.proyection_matrix@vertices[3]
        
        v1 /= v1[-1]
        v2 /= v2[-1]
        v3 /= v3[-1]
        v4 /= v4[-1]

        return v1, v2, v3, v4

    def clip(self):
        pass



class Triangle:
    def __init__(self) -> None:
        self.vertices = [0]*3

class Mesh:
    def __init__(self, stride) -> None:
        self.vertices = []
        self.triangles = []
        self.stride = stride

    def add_face(self, tris, offset=-1):
        for i in tris:
            self.triangles.append( i + offset ) 

    def add_vertex(self, vertex):
        self.vertices.append( vertex ) 
    
    def get_face_normal(self, face_start):
        A = self.vertices[self.triangles[ face_start ]][:3]
        B = self.vertices[self.triangles[ face_start + 1 ]][:3]
        C = self.vertices[self.triangles[ face_start + 2 ]][:3]
        N = np.cross( B-A, C-A )
        N /= np.linalg.norm( N )
        return np.array([ *N, 0 ])  
    
    def _get_sub_vertex(self, idxs):
        sub_mesh = []
        for i in idxs:
            sub_mesh.append( self.vertices[i] )
        return sub_mesh
    
    def __iter__(self):
        for i in range(0, len(self.triangles), self.stride):
            vidx = self.triangles[i:i+self.stride]
            yield self._get_sub_vertex( vidx ) 

class Camera:
    pass