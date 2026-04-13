import cadquery as cq
from cadquery.func import torus,box, cylinder, chamfer
from ocp_vscode import *

# measurements are in mm, hence the *25.4
die_radius = 4.2/2.0*25.4 # Radius of the plate
thickness = 1.0*25.4  # Thickness of the plate
wall_thickness = 3/8*25.4
fin_thickness = 1/8*25.4
cylinder_radius = 4.0/2.0*25.4 # Radius of extruded cylinder outer wall
chamfer_size = 10.0
chamfer_depth = 20.0

result = ( cq.Workplane("XY")
        .circle(cylinder_radius - wall_thickness)
        .extrude(thickness)
        .tag("base")
        .edges(">Z").chamfer(chamfer_depth, chamfer_size)
        .transformed(rotate=(0, 180, 0))
        .text(
                """4.0" dia. tube\n3/8" thick""",       # The text string
                fontsize=12,    # Size of the text
                distance=0.33,    # Extrusion distance (depth)
                combine=True
            )
        .faces("<Z", tag="base").workplane()
        .transformed(rotate=(0, 180, 0))
        .circle(die_radius)
        .circle(cylinder_radius)
        .extrude(thickness)
        .faces(">Z", tag="base").workplane()
        .transformed(offset=(0,0,-0.125*thickness))
        .box(cylinder_radius*2,fin_thickness,thickness/4.0)
        .edges("|X and <Z").chamfer(3, fin_thickness/2.5)
)

result4 = cq.Workplane("XY").box(cylinder_radius*2.0,fin_thickness,thickness/4.0).edges("|X and <Z").chamfer(3, fin_thickness/2.5)


show(result)