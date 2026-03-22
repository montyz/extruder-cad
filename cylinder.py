# /// script
# dependencies = [
#   "cadquery",
# ]
# ///

import cadquery as cq
from cadquery.func import torus,box, cylinder

# measurements are in mm, hence the *25.4
die_OD = 4.2/2.0*25.4 # Radius of the plate
thickness = 1.0*25.4  # Thickness of the plate
wall_thickness = 3/8*25.4
fin_thickness = 1/8*25.4
cylinder_OD = 4.0/2.0*25.4 # Radius of extruded cylinder

t = torus(cylinder_OD-wall_thickness/2.0,wall_thickness/2.0)
b = box(cylinder_OD,fin_thickness,thickness/2.0)+box(fin_thickness,cylinder_OD,thickness/2.0)
c = cylinder(cylinder_OD-wall_thickness,thickness).translate((0,0,-thickness/2.0))
d = (cylinder(die_OD,thickness) - cylinder(cylinder_OD,thickness)).translate((0,0,-thickness/2.0))
result = b-t+c+d

show_object(result)