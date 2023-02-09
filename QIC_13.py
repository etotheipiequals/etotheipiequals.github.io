from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_13_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.13: Atomic qubit arrays: Optical tweezers")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.12 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

""", fontSize = 1.0)

p.gridText(1,1,r"""

**Light forces**


* Spontaneous force


* Optical dipole force


""", fontSize = 0.5)


p.gridImage(1,2,"./QIC_Figures/QIC12_light_forces_1.png", height = 300)

########################################
p.newSlide()
p.title(r"""**Initialisation (DVC1)**""")



p.makeGrid(2,2)

p.gridText(0,0,r"""
 
* Prepare atom array in state $\vert 0\rangle$
 
* Use lasers [QIC.12-14]

* QIC.13 Trapping: use far-detuned laser with $\Delta \gg \Omega$.

* QIC.14 Slowing and optical pumping: use near-resonant laser $\Delta \sim \Omega \sim \Gamma$ 
""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC7_Sr_tweezer_0.png", height = 300)


p.gridImage(1,1,"./QIC_Figures/QIC1_Rydberg_array.png", height = 200, textBelow="Barredo et al, Nature  **561**, 79 (2018)", fontSize = 0.5)



########################################
p.newSlide()
p.title("QIC.13 Outline")
p.leftText(r"""

* Derive an expression for the trapping potential in 3D using gaussian beam optics.

* Derive expressions for the spatial extent of atomic wave packet assuming it can be cooled to the motional ground state.
 
* Estimate the population in the excited state and the rate of spontaneous scattering for particular trap parameters. 

""", fontSize = 0.5)


p.rightIFrame("./QIC_Figures/Tweezer_interactive.html", height=800)


########################################
p.newSlide()
p.title("Optical tweezer potential")

########################################
p.newSlide()
p.title("Optical tweezer potential")

########################################
p.newSlide()
p.title("Optical tweezer vibrational ground state")

########################################
p.newSlide()
p.title("Optical tweezer vibrational ground state")

########################################
p.newSlide()
p.title("Optical tweezer")

########################################
p.newSlide()
p.title("Optical tweezer: photon scattering rate")

########################################
p.newSlide()
p.title("Optical tweezer: photon scattering rate")


########################################
p.newSlide()
p.title("Optical tweezer interactive")


p.leftText(r"""

Parameters

* Atom: Cs
* Trapping laser wavelength 1.06 $\mu$m
* Power 1 mW

""", fontSize = 0.5)


p.rightIFrame("./QIC_Figures/Tweezer_interactive.html", height=800)


########################################
p.newSlide()
p.title("QIC.13 Summary")
p.leftText(r"""
** QIC.13 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Derive an expression for the trapping potential in 3D using gaussian beam optics.

* Derive expressions for the spatial extent of atomic wave packet assuming it can be cooled to the motional ground state.
 
* Estimate the population in the excited state and the rate of spontaneous scattering for particular trap parameters. 


""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_13.html")

