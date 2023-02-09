from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_11_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.11: Ph 30, 14.00 Monday Feb 14, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.10 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

**Decoherence model**

""", fontSize = 1.0)

p.gridText(1,1,r"""

* Model 1: Information leak.


* Model 2: Spin-spin interaction


""", fontSize = 0.5)

p.gridText(2,1,r"""

* `Which-path' information $\rightarrow$ complementarity

* Quantum erasure.

""", fontSize = 0.5)

p.gridImage(2,2,"./Figures/cylinder.jpg", height = 150)

########################################
p.newSlide()
p.title("QIC: Part II")

p.spanCenterText(r"""
## How to build a quantum computer? 
""")

p.leftText(r"""
**DiVincenzo Criteria**

* Qubits

* Single- and two-qubit gates

* Read-out

* Low decoherence

* Scalability

""")

########################################
p.newSlide()
p.title("Qubit (two-level system): Examples ")

p.makeGrid(4,4)

p.gridImage(0,2,"./QIC_Figures/QIC1_superconducting_3.jpg", height = 100, textBelow="Google's Sycamore processor", fontSize = 0.5)

p.gridImage(1,2,"./QIC_Figures/QIC1_ions_2.png", height = 100, textBelow="Chris Monroe, Duke and IonQ", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC1_Rydberg_array.png", height = 100, textBelow="Barredo et al, Nature  **561**, 79 (2018)", fontSize = 0.5)


p.gridImage(2,2,"./QIC_Figures/QIC1_photons_1.png", height = 100)

p.gridImage(2,3,"./QIC_Figures/QIC1_semi.png", height = 100,  textBelow="Borjan et al, Nature  **577**, 195 (2020)", fontSize = 0.5)


########################################
p.newSlide()
p.title(r"""## Why atoms? Atoms, lasers and qubits """)

p.makeGrid(1,2)

p.gridImage(0,0,"./QIC_Figures/QIC11_Nature2022.png", height = 600, textBelow="Nature January 2022.", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC11_Nature2022_1.png", height = 600, textBelow="Number 3: Rydberg atoms", fontSize = 0.5)



########################################
p.newSlide()
p.title(r"""## Why atoms? Atoms, lasers and qubits """)

p.makeGrid(1,2)

p.gridImage(0,0,"./QIC_Figures/QIC11_Toric_super.png", height = 600, textBelow="Google: 31 qubits, 98 people", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC11_Toric_Rydberg.png", height = 600, textBelow="Harvard: 219 qubits, 16 people", fontSize = 0.5)

########################################
p.newSlide()
p.title(r"""## Why atoms? Atoms, lasers and qubits """)

p.makeGrid(1,2)

p.gridImage(0,0,"./QIC_Figures/QIC11_Toric_Rydberg.png", height = 600, textBelow="Harvard: 219 qubits, 16 people", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC11_Toric_Rydberg_Fig1.png", height = 600, textBelow="Harvard: 219 qubits, 16 people", fontSize = 0.5)



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
p.title("Alkaline earths: Strontium (Sr) ")

p.makeGrid(4,4)



p.gridImage(0,2,"./QIC_Figures/QIC14_Sr_metal.png", height = 100, textBelow="", fontSize = 0.5)
p.gridImage(0,3,"./QIC_Figures/QIC11_Sr_atom_parts.png", height = 100, textBelow="", fontSize = 0.5)


p.gridImage(1,3,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 100, textBelow="", fontSize = 0.5)




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
p.title("QIC.11 Summary")
p.leftText(r"""
** QIC.11 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Be able to explain why Rb, Cs and Sr make good choices for quantum computing.

* Be able to explain what states are chosen for the computational basis and why.

* Have an overview of other energy levels that are important in the initialisation (DVC1) and gate operation (DVC2) for a Rydberg atom quantum computer.

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_11.html")

