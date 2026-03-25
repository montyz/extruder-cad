# /// script
# dependencies = [
#   "cadquery",
# ]
# ///

import cadquery as cq
from ocp_vscode import *

cyl = cq.Workplane("XY").circle(100).extrude(20).transformed(rotate=(0, 180, 0)).text(
    "Cone Packs",       # The text string
    fontsize=15,    # Size of the text
    distance=1,    # Extrusion distance (depth)
    combine=True
)
result = cyl

show(result)