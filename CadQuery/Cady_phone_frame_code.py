#Cady_Phone_Frame

#Tento k�d v�m vygeneruje r�me�ek pro v� telefon, kter� po vlo�en� do Cady zajist� p�esn� l�cv�n� telefonu s USB-C konektorem

#Upravte n�sleduj�c� prom�nn�
width = 72.7        #���ka telefonu v milimetrech
portHeight = 4.8    #v��ka od zad telefou ke spodn� ��sti UBS-C portu v milimetrech
cameraBump = False  #pokud m� v� telefon vystoupl� modul kamery, nastavte na "True"

clearance = 0.5     #voliteln� prom�nn� pro nastaven� v�le sou��stek na z�klad� se��zen� 3D tisk�rny, m��ete ponechat bezezm�ny

#Do n�sledu�c� ��sti k�du nezasahujte, pouze vyrendrujte a exportujte na z�klad� zadan�ch �daj�
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