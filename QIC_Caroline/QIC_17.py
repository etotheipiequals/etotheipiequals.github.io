from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_17_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.17: Ph 30, 14.00 Monday Mar 7, 2022")
p.makeGrid(2,2)
p.gridText(0,0,r"""

** QIC.16 Summary **

""", fontSize = 1.0)

p.gridText(1,0,r"""

**Alkali atom: single qubit rotations **

* Stimulated Raman transition 


""", fontSize = 0.5)

p.gridImage(1,1,"./QIC_Figures/QIC16_Raman_2.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("QIC.17: Outline")

p.makeGrid(2,2)

p.gridText(0,0,
r"""

$\bbox[5px, border: 2px solid red]{\rm Two-qubit gates}$ QIC.17-18


""", fontSize = 0.5)


p.gridText(1,0,
r"""

Rydberg states

""", fontSize = 0.5)

p.gridImage(1,1,"./QIC_Figures/QIC17_Rydberg_2.png", height = 100)


########################################
p.newSlide()
p.title("What are Rydberg atoms? ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC17_Rydberg_1.png", height = 100)


########################################
p.newSlide()
p.title("What are Rydberg atoms? ")

p.makeGrid(2,2)

p.gridImage(0,1,"./QIC_Figures/QIC17_Rydberg_2.png", height = 100)


########################################
p.newSlide()
p.title("Interactions ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC17_vanderWaals_1.png", height = 100)
p.gridImage(1,3,"./QIC_Figures/QIC17_vanderWaals_2.png", height = 100)
p.gridImage(2,3,"./QIC_Figures/QIC17_vanderWaals_3.png", height = 100)


########################################
p.newSlide()
p.title("Rydberg blcokade")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC17_Blockade_1.png", height = 100)
p.gridImage(1,3,"./QIC_Figures/QIC17_Blockade_2.png", height = 100)
p.gridImage(2,3,"./QIC_Figures/QIC17_Blockade_3.png", height = 100)

########################################
p.newSlide()
p.title("Rydberg blcokade: eigenbasis")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC17_Blockade_4.png", height = 100)

########################################
p.newSlide()
p.title("Rydberg blockade: experiment")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC17_Blockade_5.png", height = 100)
p.gridImage(1,3,"./QIC_Figures/QIC17_Blockade_6.png", height = 100)


########################################
p.newSlide()
p.title("QIC.17 Summary")
p.leftText(r"""
** QIC.17 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Understand the scaling of the properties of Rydberg atoms as a function of their principal quantum number, $n$.
* Understand the concept of Rydberg blockade, and estimate the blockade radius given the parameters.
* Derive the interaction Hamiltonian in the entangled basis, and show how Rydberg blockade leads to entanglement.

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_17.html")

