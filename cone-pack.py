# /// script
# dependencies = [
#   "cadquery",
# ]
# ///

import cadquery as cq

# measurements are in mm, hence the *25.4
circle_radius = 4.2/2.0*25.4 # Radius of the plate
thickness = 0.175*25.4  # Thickness of the plate
rectangle_width = 25.4  # Width of rectangular hole in cylindrical plate
rectangle_length = 7.0/16.0*25.4  # Length of rectangular hole in cylindrical plate

result = (
    cq.Workplane("front")
    .circle(circle_radius)
    .text(
    "Cone Packs",       # The text string
    fontsize=5,    # Size of the text
    distance=thickness+1.0,    # Extrusion distance (depth)
    combine=True  # Do not combine with the base object yet
)
    .center(0.0, circle_radius/3)
    .rect(rectangle_width, rectangle_length)
    .center(0.0, -circle_radius/3*2)
    .rect(rectangle_width, rectangle_length)
    .extrude(thickness)
)
cq.exporters.export(result, "conepack.stl")