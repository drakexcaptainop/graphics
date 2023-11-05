import pygame as pg
from proyector import Proyector, np, Mesh
from utils import load_obj
from math_utils import create_rotation_matrix, proyspace2screen
width, height = 800, 800


proy = Proyector( np.deg2rad(60), 100, 1 )
vertices = [ [ -1, 1, 0, 0 ], [ -1, -1, 0, 0 ], [ 1, -1, 0, 0 ] ]
origin = np.array( [ 0, 0, 2, 0 ] )
rot_mat = create_rotation_matrix(np.deg2rad(12*60/1000), axis='y')
screen = pg.display.set_mode( (width, height) )
mesh: Mesh = load_obj(r'C:\Users\juggb\Downloads\testMesh1.obj', 3)


red = np.array([255, 0, 0],dtype=float)
lightSource = np.array([0, 0, -1, 0], float)
while 1:
    for i in range( len(mesh.vertices) ):
        mesh.vertices[i] = rot_mat@mesh.vertices[i]
    
    proyectedMesh = proy.proyect_mesh( mesh, origin )

    screen.fill( 'black' )
    for i in range(0, len(mesh.triangles), mesh.stride):
        verts = proyspace2screen(proyectedMesh[i:i+mesh.stride], width, height ) 
        normal = mesh.get_face_normal( i )
        face2ls = lightSource - mesh.vertices[mesh.triangles[i]] - origin
        face2ls = face2ls/np.linalg.norm(face2ls)
        light_scale = max((np.dot( normal, face2ls )),0)

        if np.dot( mesh.vertices[mesh.triangles[i]] + origin, normal  ) < 0:
            pg.draw.polygon( screen, red*light_scale, [verts[0][:2], verts[1][:2], verts[2][:2]])
        # pg.draw.line( screen,'red', , verts[1][:2] )
        # pg.draw.line( screen, 'red',, verts[2][:2] )
        # pg.draw.line( screen, 'red',, verts[0][:2] )

    for i in pg.event.get():
        pass


    # pg.draw.polygon( screen, 'red', tri_coords)
    pg.display.flip()