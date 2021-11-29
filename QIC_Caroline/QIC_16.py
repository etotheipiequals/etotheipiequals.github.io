from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_16_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.16: Ph 30, 14.00 Thursday Mar 3, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.15 Summary **


""", fontSize = 1.0)

p.gridText(1,0,r"""

**Rb/Cs atom array initialisation**

* Polarization selection rules: $\Delta m_F = 0,\pm 1$

* Optical pumping


""", fontSize = 0.5)


p.gridImage(1,2,"./QIC_Figures/H1s2p_lin.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/H1s2p_circ.png", height = 100, textBelow="", fontSize = 0.5)


p.gridImage(2,2,"./QIC_Figures/QIC15_optical_pumping_3.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(2,3,"./QIC_Figures/QIC15_optical_pumping_4.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("QIC.16: Outline")

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


p.gridText(1,0,
r"""


$\bbox[5px, border: 2px solid lime]{\rm Single-qubit \; gates}$ Stimulated Raman transitions


""", fontSize = 0.5)
p.gridImage(1,1,"./QIC_Figures/QIC16_Raman_2.png", height = 100)

########################################
p.newSlide()
p.title("Stimulated-Raman transitions")

p.makeGrid(2,2)

p.gridText(0,0,
r"""

$\bbox[5px, border: 2px solid lime]{\rm Single-qubit \; gates}$ 

""", fontSize = 1.0)
p.gridImage(0,1,"./QIC_Figures/QIC16_Stim_Raman_2.png", height = 200)


########################################
p.newSlide()
p.title("Stimulated-Raman transitions ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC16_Raman_1.png", height = 200, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Stimulated-Raman transitions ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC16_Raman_2.png", height = 150, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Stimulated-Raman transitions ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC16_Raman_2.png", height = 150, textBelow="", fontSize = 0.5)



########################################
p.newSlide()
p.title("Stimulated-Raman transitions: Spontaneous emission ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC16_Raman_spont_em.png", height = 150, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Stimulated-Raman transitions: Example ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC16_Raman_Cs.png", height = 150, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("QIC.16 Summary")
p.leftText(r"""
** QIC.16 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Understand the principle of stimulated Raman transition, how the effective Rabi frequency depends on the laser power and detuning.
* Derive an expression for the probability of spontaneous emission during a single-qubit rotation.
* Identify states that could be used for stimulated Raman transitions in, for example, Rb and Cs.
* Work out the configuration of laser beam polarizations and propagation directions needed to drive a particular transition.

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_16.html")

