from proyector import Mesh, np, Proyector
# Blender 3.6.5
# www.blender.org
# mtllib testMesh1.mtl
# o Cube
# v -1.000000 1.000000 1.000000
# v -1.000000 -1.000000 1.000000
# f 4 3 7 8
# f 8 7 5 6
# f 6 2 4 8
# f 2 1 3 4
# f 6 5 1 2

def load_obj( path, stride ):
    mesh = Mesh( stride )
    with open( path, 'r' ) as f:
        for line in f:
            if line[0] == 'v':
                vert = [float(v) for v in line.split(' ')[1:]]
                mesh.add_vertex( np.array([*vert, 0]) )
            elif line[0] == 'f':
                tris_index = [int(i) for i in line.split(' ')[1:]]
                mesh.add_face( tris_index )
    return mesh


