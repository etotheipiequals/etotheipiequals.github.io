from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_12_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.12: Ph 30, 14.00 Thursday Feb 17, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.11 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

""", fontSize = 1.0)

p.gridText(1,1,r"""

**Atoms and states**


* Rb, Cs, Sr


* Qubit states


""", fontSize = 0.5)


p.gridImage(1,2,"./QIC_Figures/QIC11_Cs_energy_levels_4.png", height = 150)

########################################
p.newSlide()
p.title("QIC.12: Outline")

p.makeGrid(2,2)


p.gridText(0,0,r"""

DVC1: Atom array initialisation using lasers

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC1_Rydberg_array.png", height = 300)

p.gridText(1,0,r"""

* Light forces

* Ehrenfest's theorem

* Two light forces

* Spontaneous force: laser cooling

* Optical dipole force: trapping

""", fontSize = 0.5)


p.gridImage(1,1,"./QIC_Figures/QIC12_light_forces_1.png", height = 150)

########################################
p.newSlide()
p.title("Ehrenfest's theorem ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/Ehrenfest.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Light forces ")

p.makeGrid(4,4)

p.gridImage(3,3,"./QIC_Figures/QIC12_light_forces_1.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Spontaneous force ")

p.makeGrid(2,2)

p.gridImage(1,1,"./QIC_Figures/QIC12_spont_force.png", height = 200, textBelow="", fontSize = 0.5)



########################################
p.newSlide()
p.title("Optical dipole potential ")

p.makeGrid(2,2)

p.gridImage(1,1,"./QIC_Figures/QIC12_dipole_in_out_of_phase.png", height = 200, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Optical dipole potential: Dressed state model ")

p.makeGrid(4,4)

p.gridImage(0,2,"./QIC_Figures/QIC12_dressed_states_1.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC12_dressed_states_2.png", height = 100, textBelow="", fontSize = 0.5)




########################################
p.newSlide()
p.title("QIC.12 Summary")
p.leftText(r"""
** QIC.12 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Explain the two types of light force.

* Understand how to derive expressions for the light-shift from either the light force or the eigenvalues of the interaction Hamiltonian. 

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_12.html")

