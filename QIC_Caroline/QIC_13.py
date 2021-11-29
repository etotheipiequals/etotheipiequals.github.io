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
p.title("QIC.13: Ph 30, 14.00 Monday Feb 21, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.12 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

""", fontSize = 1.0)

p.gridText(1,1,r"""

**Light forces**


* Spontaneous force


* Optical dipole formce


""", fontSize = 0.5)


p.gridImage(1,2,"./QIC_Figures/QIC12_light_forces_1.png", height = 150)

########################################
p.newSlide()
p.title("QIC.13: Outline")

p.makeGrid(2,2)

p.gridText(0,0,r"""

Optical tweezer


""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC13_tweezer_static.png", height = 150)

p.gridText(1,0,r"""

* 

""", fontSize = 0.5)

#p.gridImage(1,1,"./QIC_Figures/QIC7_Sr_tweezer_0.png", height = 150)

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
p.title("Part II")

p.spanCenterText(r"""

## Rydberg atom quantum computer 
""")

p.leftText(r"""
**DiVincenzo Criteria**

* Qubits: Atoms (Rb, Cs, Sr) Initialisation [QIC.11-15]
* Gates (lasers): Single-qubit gates [QIC.16] and Two-qubit gates [QIC.17-18]
* Read-out (lasers) [QIC.16]
* Low decoherence (select particular states) [QIC.11 and 16]
* Scalability (optical tweezer arrays) [QIC.12-15]

""", fontSize = 0.5)

########################################
p.newSlide()
p.title("Atoms")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC11_periodic_table.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Alkali Atoms: States ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC11_atom_parts.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Cs States ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC11_Cs_energy_levels_2.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Sr States ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC11_Sr_energy_levels_1.png", height = 100, textBelow="", fontSize = 0.5)




########################################
p.newSlide()
p.title(r"""**Initialisation (DVC1)**""")



p.makeGrid(2,2)

p.gridText(0,0,r"""
 
* Prepare atom array in state $\vert 0\rangle$
 
* Use lasers [QIC.12-15]

* For trapping: far-detuned laser with $\Delta \gg \Omega$.

* To load traps, laser cooling, near-resonant laser $\Delta \sim \Omega \sim \Gamma$ 
""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC7_Sr_tweezer_0.png", height = 300)


p.gridImage(1,1,"./QIC_Figures/QIC1_Rydberg_array.png", height = 200, textBelow="Barredo et al, Nature  **561**, 79 (2018)", fontSize = 0.5)

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

