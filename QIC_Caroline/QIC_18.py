from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_18_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.18: Ph 30, 14.00 Thursday Mar 10, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.17 Summary **

""", fontSize = 1.0)

p.gridText(1,0,r"""

**Rydberg blockade **



""", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC17_Rydberg_1.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(2,3,"./QIC_Figures/QIC17_Blockade_4.png", height = 100)




########################################
p.newSlide()
p.title("QIC.18: Rydberg CNOT gate")
p.makeGrid(4,4)
p.gridText(0,0,
r"""

DVC2: $\bbox[5px, border: 2px solid lime]{\rm Two-qubit \; gate}$ 

""", fontSize = 0.5)


p.gridText(1,0,
r"""
CNOT [QIC.9]
""", fontSize = 1.0)

p.gridImage(1,1,"./QIC_Figures/QIC9_CNOT.png", height = 100)
p.gridImage(1,2,"./QIC_Figures/QIC9_CNOT_CZ.png", height = 100)
p.gridImage(1,3,"./QIC_Figures/QIC18_CNOT_2.png", height = 200)

p.gridText(2,0,
r"""
Implement usng Rydberg blockade
""", fontSize = 1.0)
p.gridImage(2,2,"./QIC_Figures/QIC18_CNOT_Cs_atom.png", height = 200)


########################################
p.newSlide()
p.title("QIC.18: Rydberg CNOT gate")
p.makeGrid(4,4)
p.gridText(0,0,
r"""

DVC2: $\bbox[5px, border: 2px solid lime]{\rm Two-qubit \; gates}$ 

""", fontSize = 0.5)


p.gridImage(0,3,"./QIC_Figures/QIC9_CNOT.png", height = 60)
p.gridImage(1,3,"./QIC_Figures/QIC9_CNOT_CZ.png", height = 100)
p.gridImage(2,3,"./QIC_Figures/QIC18_CNOT_2.png", height = 100)

p.gridText(0,1,
r"""
Implement using Rydberg blockade
""", fontSize = 0.5)

########################################
p.newSlide()
p.title("Rydberg CNOT gate: Levels")
p.makeGrid(4,4)


p.gridImage(0,3,"./QIC_Figures/QIC18_CNOT_Cs_atom.png", height = 200)


########################################
p.newSlide()
p.title("CNOT Pulse Sequence ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC18_5_pulse.png", height = 200)


########################################
p.newSlide()
p.title("CNOT Pulse Sequence ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC18_pulse_1and5.png", height = 100)
p.gridImage(1,3,"./QIC_Figures/QIC18_pulse_3.png", height = 100)
p.gridImage(2,3,"./QIC_Figures/QIC18_pulse_2and4.png", height = 100)


########################################
p.newSlide()
p.title("Controlled Phase using Rydberg blockade ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC18_pulse_234.png", height = 100)


########################################
p.newSlide()
p.title("Experiment ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC18_levine_1.png", height = 100)
p.gridImage(1,3,"./QIC_Figures/QIC18_levine_2.png", height = 100)
p.gridImage(2,3,"./QIC_Figures/QIC18_levine_3.png", height = 100,
textBelow =r"""Levine *et al*, PRL, **123**, 170503 (2019) """, fontSize = 0.5)


########################################
p.newSlide()
p.title("CNOT: Si spin qubits ")

p.makeGrid(4,4)


p.gridImage(1,3,"./QIC_Figures/QIC18_Si_CNOT.png", height = 100,  textBelow="Mills et al, arXiv:2111.1937", fontSize = 0.5)
p.gridImage(2,3,"./QIC_Figures/QIC18_Si_CNOT_SWAP.png", height = 100,  textBelow="Mills et al, arXiv:2111.1937", fontSize = 0.5)


########################################
p.newSlide()
p.title("QIC.18 Summary")
p.leftText(r"""
** QIC.18 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Understand the five pulse sequence used to realise a Rydberg CNOT gate.
* Be able to write matrices to describe any of the pulses in a prescribed basis.

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_18.html")

