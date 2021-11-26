from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_15_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.15: Ph 30, 14.00 Monday Feb 28, 2022")
p.makeGrid(2,2)
p.gridText(0,0,r"""

** QIC.14 Summary **

**Sr atom array initialisation**


""", fontSize = 1.0)

p.gridText(1,0,r"""


$\bbox[5px, border: 2px solid orange]{\rm DVC1: Initialisation}$

$\bbox[5px, border: 2px solid gray]{\rm DVC2: Gates}$ 
$\bbox[5px, border: 2px solid orange]{\rm Single-qubit}$ 
$\bbox[5px, border: 2px solid red]{\rm Two-qubit}$

$\bbox[5px, border: 2px solid orange]{\rm DVC3: Read out}$

$\bbox[5px, border: 2px solid lime]{\rm DVC4: Decoherence}$

$\bbox[5px, border: 2px solid gray]{\rm DVC5: Scaling}$

""", fontSize = 0.5)



p.gridImage(1,1,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 150)

########################################
p.newSlide()
p.title("QIC.15: Outline")

p.makeGrid(2,2)


p.gridText(0,0,r"""

Rb, Cs atom array initialisation

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC11_Cs_energy_levels_4.png", height = 150)


p.gridText(1,0,r"""

* Optical pumping

* Polarization selection rules


""", fontSize = 0.5)


p.gridImage(1,1,"./QIC_Figures/QIC15_optical_pumping_1.png", height = 150)


########################################
p.newSlide()
p.title("Alkali atom: States ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC15_optical_pumping_1.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC15_optical_pumping_2.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Selection rules ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC11_Cs_energy_levels_3.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Polarization selection rules ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/H1s2p.jpg", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/H1s2p_lin.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(2,3,"./QIC_Figures/H1s2p_circ.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Polarization selection rules ")

p.makeGrid(4,4)


p.gridImage(2,3,"./QIC_Figures/QIC15_MOT_bad.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Optical pumping I")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC15_Kastler.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC15_optical_pumping_3.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Optical pumping II")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC15_optical_pumping_4.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title(r"""**Rb/Cs atom quantum computer?**""")

p.makeGrid(2,2)

p.gridText(0,0,
r"""

$\bbox[5px, border: 2px solid orange]{\rm DVC1: Initialisation}$

$\bbox[5px, border: 2px solid gray]{\rm DVC2: Gates}$ 
$\bbox[5px, border: 2px solid red]{\rm Single-qubit}$ QIC.16 
$\bbox[5px, border: 2px solid red]{\rm Two-qubit}$ QIC.17-18

$\bbox[5px, border: 2px solid orange]{\rm DVC3: Read out}$

$\bbox[5px, border: 2px solid lime]{\rm DVC4: Decoherence}$

$\bbox[5px, border: 2px solid gray]{\rm DVC5: Scaling}$


""", fontSize = 0.5)


p.gridImage(0,1,"./QIC_Figures/QIC16_readout_1.png", height = 100)
p.gridImage(1,1,"./QIC_Figures/QIC16_readout_3.png", height = 100)




########################################
p.newSlide()
p.title("QIC.15 Summary")
p.leftText(r"""
** QIC.15 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Explain why labeling a laser beam $\sigma_-$, $\pi$, or $\sigma_+$ does not make sense.
* Work out what configuration of laser beam polarizations and propagation directions are needed to drive particular transitions and hence optically pump atoms into a particular state.
* Sketch optical pumping diagrams for different cases.

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_15.html")

