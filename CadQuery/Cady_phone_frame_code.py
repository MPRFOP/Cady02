#Cady_Phone_Frame

#Tento kód vám vygeneruje rámeèek pro váš telefon, který po vložení do Cady zajistí pøesné lícvání telefonu s USB-C konektorem

#Upravte následující promìnné
width = 72.7        #šíøka telefonu v milimetrech
portHeight = 4.8    #výška od zad telefou ke spodní èásti UBS-C portu v milimetrech
cameraBump = False  #pokud má váš telefon vystouplý modul kamery, nastavte na "True"

clearance = 0.5     #volitelná promìnná pro nastavení vùle souèástek na základì seøízení 3D tiskárny, mùžete ponechat bezezmìny

#Do následuící èásti kódu nezasahujte, pouze vyrendrujte a exportujte na základì zadaných údajù
import cadquery as cq
from cadquery import exporters

x = 77.5 - clearance
y = 170 - clearance
z = 11 - clearance
conHeig = 6
thick = conHeig - portHeight

if (cameraBump == True):
    y = y*0.7

result = (cq.Workplane("XY")
    .rect(x,y/2).extrude(z -thick)
    .rect(width + clearance, y/2).cutThruAll()
    .faces("<Z").center(0,y/4).workplane().rect(x,y).extrude(thick)
    .faces(">Z").center(0,y/2).workplane().rect(20,40).cutThruAll()
    .faces(">Z").center(0,y/1.8).workplane().rect(width-20,y/1.5).cutThruAll()
    .edges("Z").fillet(0.5).edges("-Z").fillet(0.5)


)

show_object(result)