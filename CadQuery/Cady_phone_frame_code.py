#Cady_Phone_Frame

import cadquery as cq
from cadquery import exporters


result = (cq.Workplane("XY")
    .box(3, 3, 0.5)
    .edges("|Z")
    .fillet(0.125))

show_object(result)