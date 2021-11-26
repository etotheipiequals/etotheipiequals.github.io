from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/Lumiere.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
*God is light*; 

*in him there is no darkness* ... 

John 1:5
""")

p.spanCenterImage("./Figures/dark_side.png", height = 400) 


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
# Optics I

C. S. Adams

Professor of Physics, Durham University, 

September 2021.
""")

p.spanCenterImage("./Figures/dark_side.png", height = 400) 
p.spanCenterIFrame("./Figures/time.mp3") 


########################################
#############  New slide  ############## Grid with text 
########################################
p.newSlide()
p.title("History of optics")
p.makeGrid(5,4)
p.gridText(0,0,r"""
 $~~$  **Ibn Sahl**
 
 $~~$  Baghdad  940 - 1000
""", fontSize = 0.5)
p.gridImage(0,1,"./Figures/ibn_sahl_1.png", height = 120)
p.gridText(2,0,r"On burning lenses 984",fontSize = 0.5)
p.gridImage(2,1,"./Figures/ibn_sahl_2.jpg", height = 180)

p.gridText(0,2,r"""
$~~$  **Ibn al Haytham**

$~~$ Basra 965 - Cairo 1040
""", fontSize = 0.5)
p.gridImage(0,3,"./Figures/Hazan.png", height = 120)
p.gridText(2,2,r"Book of optics 1020" ,fontSize = 0.5)
p.gridImage(2,3,"./Figures/hazan_mirrors.jpg", height = 180)


########################################
#############  New slide  ############## Grid with text 
########################################
p.newSlide()
p.title("Ibn al Haytham: Camera obscura")
p.leftImage("./Figures/camera_obscura.png", height = 250,textBelow=r"Credits: © Ali Amro / MuslimHeritageImages.com",fontSize = 0.5)
#p.rightImage("./Figures/Inferior_Mirage_green_flash.jpg", height = 200,textBelow=r"**Photo credit**:  Inferior Mirage.",fontSize = 0.5)

########################################
#############  New slide  ############## Grid with text 
########################################
p.newSlide()
p.title("Ibn al Haytham: Camera obscura")
p.leftImage("./Figures/camera_obscura.png", height = 250,textBelow=r"Credits: © Ali Amro / MuslimHeritageImages.com",fontSize = 0.5)
p.rightImage("./Figures/Inferior_Mirage_green_flash.jpg", height = 200, textBelow=r"**Photo credit**:  Inferior Mirage.",fontSize = 0.5)


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
 *Benedictin Breviary* St. Denis 1350 Bodleian
""")

p.spanCenterImage("./Figures/magnificat_0.jpg", height = 400, textBelow=r"""**Magnificat anima mea Dominum**:  My soul does magnify the lord.""",fontSize = 0.5) 

########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
# Benedictin Breviary from St. Denis 1350 Bodleian
""")

p.spanCenterImage("./Figures/magnificat_1.jpg", height = 400, textBelow=r"""**Magnificat anima mea Dominum**:  My soul does magnify the lord.""",fontSize = 0.5) 


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
# Jan van Eyck 1390 - 1441
""")

p.spanCenterImage("./Figures/van_Eyck_glasses.jpg", height = 400) 

########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
# Hieronymus Bosch 1450 - 1516
""")

p.spanCenterImage("./Figures/Bosch_2.jpg", height = 400) 



########################################

########################## SAVE
p.save("./Lumiere.html")



