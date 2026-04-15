import cadquery as cq
from cadquery.func import torus,box, cylinder, chamfer
from ocp_vscode import *

# measurements are in mm, hence the *25.4
die_radius = 4.2/2.0*25.4 # Radius of the plate
thickness = 1.0*25.4  # Thickness of the plate
wall_thickness = 5/16*25.4
fin_thickness = 1/8*25.4
cylinder_radius = 4.0/2.0*25.4 # Radius of extruded cylinder outer wall
chamfer_size = 10.0
chamfer_depth = 20.0

part1 = (
    cq.Workplane("XY")
    .circle(cylinder_radius - wall_thickness)
    .extrude(thickness)
    .edges(">Z")
    .chamfer(chamfer_depth, chamfer_size)
)

text1 = (
    cq.Workplane("XY")
    .text(
        """4.0" dia. tube\n5/16" thick""",  # The text string
        fontsize=12,  # Size of the text
        distance=-0.33,  # Extrusion distance (depth)
    )
    .val()
    .moved(ry=180)
)
part1 = part1.cut(text1)


part2 = (
    (
        cq.Workplane()
        .box(
            cylinder_radius * 2,
            fin_thickness,
            thickness / 2.0,
            centered=(True, True, False),
        )
        .edges("|X and <Z")
        .chamfer(3, fin_thickness / 2.5)
    )
    .val()
    .moved(z=thickness - thickness / 2.0)
)

part3 = (
    (
        cq.Workplane()
        .box(
            fin_thickness,
            cylinder_radius * 2,
            thickness / 2.0,
            centered=(True, True, False),
        )
        .edges("|Y and <Z")
        .chamfer(3, fin_thickness / 2.5)
    )
    .val()
    .moved(z=thickness - thickness / 2.0)
)



part4 = cq.Workplane().circle(die_radius).circle(cylinder_radius).extrude(thickness)

result = part1.union(part2).union(part3).union(part4)

show(result)
cq.exporters.export(result, "hollow_cylinder_4in.stl")