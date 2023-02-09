from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/PintOfScience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)


########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("The miniature mysteries of lights")

p.spanCenterImage("./Figures/dark_side.png", height = 400, textAbove = r"Light stories",textBelow = r"Where to start?", fontSize = 1.0) 


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
*My introduction to light...*

From Rochdale ... to ...

Professor of Physics at Durham University, 

April 12, 2022.
""")

p.spanCenterImage("./Figures/dark_side.png", height = 400) 
p.spanCenterIFrame("./Figures/time.mp3") 


########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Experimentum Crucis")
p.makeGrid(5,4)
p.gridText(0,0,r"""
Isaac Newton (1642-1726) 
""")
p.gridImage(0,1,"./Figures/Newton.jpg", height = 180)
p.gridText(0,2,r"""
Seires of experiments between 1672 and 1722.
""",fontSize = 0.5)
p.gridImage(0,3,"./Figures/newton.png", height = 180, textBelow = r"*Optiks* Paris Edition, 1722", fontSize = 0.5)
p.gridText(2,0,r"""
James Gregory (1638-1675) 
""")
p.gridImage(2,1,"./Figures/Gregory1.jpg", height = 180)
p.gridImage(2,2,"./Figures/Gregory2.jpg", height = 180, textBelow = r"*Optica Promota*  1663", fontSize = 0.5)
p.gridText(2,3,r"""*Let in the sun's rays by a small hole to a darkened house, and at the hole place a feather (the more delicate and white the better for this purpose), and it shall direct to a white wall or paper opposite to it a number of small circles and ovals (if I mistake them not) whereof one is somewhat white (to wit, the middle which is opposite the sun) and all the rest severally coloured. I would gladly hear Mr Newton's thoughts of it.* St Andrews, 1673
""",fontSize = 0.5)

########################################
############# New slide ##############
########################################

p.newSlide()

p.title("Gregory's feather: Diffraction grating")

p.spanCenterIFrame("./Figures/Grating.html",height = 600)







########################################
############# NEW slide ##############
########################################
p.newSlide()
p.title("Solar spectrum: Fraunhofer lines ")

p.spanCenterImage("./QIC_Figures/QIC17_Rydberg_1.png", height = 400, textBelow = "Matter has discrete energy state - light is emitted in quanta!", fontSize = 0.5)



########################################
############# NEW slide ##############
########################################
p.newSlide()
p.title("Discrete emission events: photons ")

p.spanCenterImage("./Figures/JC_cavity.PNG", height = 400)



########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Light is both wave and particle")
p.leftText(r"""

* Young's double slit: photon by photon

* G. I. Taylor (1886-1975)

* Interference fringes with feeble light

* Proc. Camb. Phil. Soc. 15, 114 (1909).
 
""")

p.rightImage("./Figures/4aiZ.gif", height = 300, textAbove = r""", 
""", textBelow = "https://www.sps.ch/artikel/progresses/wave-particle-duality-of-light-for-the-classroom-13/", fontSize = 0.5) 


########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Light properties")
p.makeGrid(5,5)

p.gridText(0,0,r"""Colour """)
p.gridImage(1,0,"./Figures/DarkSideSmall.png", height = 180)
p.gridText(0,2,r"""Interference""")
p.gridImage(1,2,"./Figures/Interference.png", height = 180)
p.gridText(0,4,r"""Polarization""")
p.gridImage(1,4,"./Figures/PolSmall.png", height = 180)

p.gridText(3,2,r"""Colour and interference - same!""",fontSize=1.0)





########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Light: Three properties")
p.makeGrid(5,5)

p.gridText(0,0,r"""Wavelength """)
p.gridImage(1,0,"./Figures/DarkSideSmall.png", height = 180)
p.gridText(0,4,r"""Polarization""")
p.gridImage(1,4,"./Figures/PolSmall.png", height = 180)

p.gridText(0,2,r"""Quanta""",fontSize=1.0)
p.gridImage(1,2,"./Figures/Photons.png", height = 180)





########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Polarization")
p.makeGrid(4,4)


p.gridText(0,0, r"""

* Etienne Malus 1775-1812

* 1808 From his house in the Rue l'Enfer, looked through a quartz crystal at 
Sunlight reflected off the windows in the Palais du Luxembourg.

* Malus' law.

""", fontSize = 0.5)

p.gridImage(0,1,"./Figures/Malus.jpg", height = 200) 

p.gridText(0,2,r"""
$~~$ Blue sky
""")
p.gridImage(1,2,"./Figures/scatter.PNG", height = 140)

p.gridImage(0,3,"./Figures/sky_HV.PNG", height = 140)





########################################
############# NEW slide ############## SUGAR
########################################

p.newSlide()
p.title("Light propagating through sugar")
p.leftText(r"""
* Jean-Baptiste Biot

* 1774-1862

* Polarimetry

* Discovery of **chiral** chemistry

* Louis Pasteur 1848
 
""")

#p.rightImage("./figures/sugar_biot.PNG", height = 400, textBelow=r"**Figure**: Sugar test") # lower res
p.rightImage("./Figures/sugar_biot.PNG",  textBelow=r"**Figure**: Sugar test") # lower res



########################################
p.newSlide()
p.title("**Wheeler's Delayed-choice experiment and the quantum eraser**")
p.makeGrid(2,2)


p.gridText(0,0,r"""


John A Wheeler 1911 - 2008
 
*In any field, find the strangest thing and then 
explore it.* 

J Gleick, *Genius: the Life and Science of Richard Feynman* (1993)

""", fontSize = 1.0)


p.gridImage(0,1,"./QIC_Figures/QIC10_wheeler_1.jpg", height = 400)

########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Light: Three properties")
p.makeGrid(5,5)

p.gridText(0,0,r"""Wavelength """)
p.gridImage(1,0,"./Figures/DarkSideSmall.png", height = 180)
p.gridText(0,4,r"""Polarization""")
p.gridImage(1,4,"./Figures/PolSmall.png", height = 180)

p.gridText(0,2,r"""Quanta""",fontSize=1.0)
p.gridImage(1,2,"./Figures/Photons.png", height = 180)


########################################
p.newSlide()
p.title("**Wheeler's delayed-choice experiment**")

p.makeGrid(2,2)


p.gridText(0,0, r"""

Test of complementarity

* We can measure wave-like or particle-like properties but not both at the same time.

* In an interferometer, either which-way or interence, not both.

""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/interferometer_eraser_2.png", height=240, textBelow = r"(a) Interference experiment. (b) Use polarization to 'label' paths - interference disappears.", fontSize = 0.5)


########################################
p.newSlide()
p.title("**Wheeler's delayed-choice experiment**")

p.leftText(r"""

Test of complementarity

* We measure wave-like or particle-like properties but not both at the same time.

* In an interferometer, either which-way or interence, not both.

* Delayed choice: we can decide whether to measure path or interference after the 'event'.


""", fontSize = 1.0)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)


########################################
############# NEW slide ############## 
########################################

p.newSlide()
p.title(" **Quantum entanglement**")
p.leftText(r"""

* We can encode the information about path in another photon.

* **Two-photon emission:**

* Propagating in same direction
\begin{eqnarray}
\vert \Psi^+\rangle & = & \textstyle{1\over \sqrt{2}}
\left(\vert {\sf L_+}  {\sf R_+} \rangle  + \vert  {\sf R_+} {\sf L_+} \rangle \right)
\end{eqnarray}



* Propagating in opposite directions
\begin{eqnarray}
\vert \Phi^+\rangle & = & \textstyle{1\over \sqrt{2}}
\left(\vert {\sf L_+}  {\sf L_-} \rangle  + \vert  {\sf R_+} {\sf R_-} \rangle \right)
\end{eqnarray}

\begin{eqnarray}
\vert \Phi^+\rangle & = & \textstyle{1\over \sqrt{2}}
\left(\vert {\sf H}  {\sf H} \rangle  + \vert  {\sf V}  {\sf V} \rangle \right)
\end{eqnarray}
""", fontSize = 0.5)

p.rightImage("./Figures/Ca_2_photon_decay.png", height = 400, textBelow=r"**Figure**: Two photons emitted: polarizations are correlated - **quantum entanglement**", fontSize = 0.5) 


########################################
p.newSlide()
p.title("**The quantum eraser**")

p.makeGrid(3,2)


p.gridImage(0,0,"./Figures/Ca_2_photon_decay.png", height = 200)


p.gridText(1,0,r"""
* You rotate your polarizer and look for interference fringes with your blue photons but you can no longer see them.

* But if I measure polarization of the red photon and tell what measurements I make you can recover the 'hidden' fringes.

""", fontSize = 0.5)

#p.gridIFrame(1,0,"./QIC_Figures/Quantum_Erasure.html", height=500)
########################################
p.newSlide()
p.title("**The quantum eraser**")

p.makeGrid(3,2)


p.gridImage(0,0,"./Figures/Ca_2_photon_decay.png", height = 200)

p.gridText(1,0,r"""
* You rotate your polarizer and look for interference fringes with your blue photons but you can no longer see them.

* But if I measure polarization of the red photon and tell what measurements I make you can recover the 'hidden' fringes.

""", fontSize = 0.5)

#p.gridIFrame(1,0,"./QIC_Figures/Quantum_Erasure.html", height=500)

p.gridText(1,1,r"""*a man, in the year 1000, might have died of a cancer initiated by a unique irradiation originating from the decay of a uranium nucleus... He survived... and died only thirty years later... In the meantime, he had a child who was among the ancestors of Napoleon and also of Doctor Babbit, who now teaches quantum mechanics. [A] measurement made by the intergalactic jokers... contains a component of the nucleus decay products such that the old man died in the year 1000... The extraterrestials show their results on TV news and Mister Babbit is asked to explain them. What will he say? Necessarily that there is no doubt that he himself exists and does not exist, that many books on history are both right and wrong. In a nutshell: facts don't exist as facts and truth is an empty notion.* Roland Omnes, *The interpretation of quantum mechanics*, (Princeton University Press 1994)""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC10_Science_307_875_2005.png", height=250)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("What Richard Feynman said!")

p.makeGrid(4,4)


p.gridText(0,0,r"""
** Richard Feynman **
> *Probability and uncertainty - the quantum mechanical view of nature*  

Messenger Letures, Cornell, November 18th, 1964.""", fontSize =0.5
)

p.gridImage(0,1,"./Figures/Feynman.png", height=200)

p.gridText(0,2,r"""
*Don't keep asking yourself, but how can it be like that.....*  
""", fontSize =0.5
)

#p.gridIFrame(2,2,"./Figures/nobody2.mp4", height=50) # picture does not appear


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("What Richard Feynman said!")

p.makeGrid(4,4)


p.gridText(0,0,r"""
** Richard Feynman **
> *Probability and uncertainty - the quantum mechanical view of nature*  

Messenger Letures, Cornell, November 18th, 1964.""", fontSize =0.5
)

p.gridImage(0,1,"./Figures/Feynman.png", height=200)

p.gridText(0,2,r"""
*Don't keep asking yourself, but how can it be like that.....*  
""", fontSize =0.5
)

p.gridIFrame(2,2,"./Figures/nobody2.mp4", height=50) # picture does not appear


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"Quantum computing: photon Controlled-NOT gate")

p.leftText(r"""
Linear optics quantum computing (KLM), 

Knill et al. Nature **409**, 46 (2001).


* Entanglement is not separable!


* *If you can see it, it is not quantum*

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/CNOT_interactive_v5.html", height=600)




########################## SAVE
p.save("./PintOfScience.html")


'''

# Pre-Newton stuff


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

p.spanCenterImage("./Figures/Bosch.jpg", height = 400) 

########################################
p.newSlide()
p.title("**Delayed-choice quantum eraser: Can we erase the past?**")

p.leftImage("./QIC_Figures/QIC10_Science_cover.jpg", height=400)

p.rightImage("./QIC_Figures/QIC10_Science_307_875_2005.png", height=400)





'''



