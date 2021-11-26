from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_2_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.2: Ph 30, 14.00 Thursday Jan 13, 2022")

p.makeGrid(5,5)
p.gridText(0,0,r"""

** QIC.1 Summary **

""", fontSize = 0.5)

p.gridText(0,1,r"""

** Qubit **

""", fontSize = 0.5)

p.gridText(0,2,r"""

** $\vert \psi\rangle = a \vert 0 \rangle + b \vert 1 \rangle$ **

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC1_qubit.png", height = 100)

p.gridText(1,1,r"""

5 qubit candidates

""", fontSize = 0.5)

p.gridText(1,2,r"""

* LC superconducting circuit
* Ion
* Atom
* Photon
* P$^+$ in Si

""", fontSize = 0.5)

p.gridText(2,1,r"""

Motivation:

* Fundamental

* Moore's law no more (classical limits)

* Energy

* Quantum advantage

""", fontSize = 0.5)

p.gridText(3,2,r"""

$\vert \Psi\rangle = a_{000} \vert 000 \rangle + a_{001} \vert 001 \rangle + \ldots $

""", fontSize = 0.5)

p.gridText(3,4,r"""

Exponential scaling 

100 qubits: $10^{30}$.

""", fontSize = 0.5)

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.2: Ph 30, 14.00 Thursday Jan 13, 2022")

p.makeGrid(2,2)
p.gridText(0,0,r"""

* DiVincenzo Criteria

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC2_DiVincenzo_2.png", height = 100)

p.gridText(1,0,r"""

* Mathematical description of a qubit

* Graphical representation using the Bloch Sphere

""", fontSize = 1.0)

p.gridImage(1,1,"./QIC_Figures/QIC2_Bloch_1.png", height = 200)

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("DiVincenzo criteria")

p.makeGrid(2,2)
p.gridText(0,0,r"""

* DiVincenzo Criteria

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC2_DiVincenzo_2.png", height = 100)

p.gridText(1,0,r"""

* Reference

""", fontSize = 1.0)

p.gridImage(1,1,"./QIC_Figures/QIC2_DiVincenzo_1.png", height = 100)

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("DiVincenzo Criteria (DVC")

p.makeGrid(4,4)
p.gridText(0,2,r"""

* DiVincenzo criteria

""", fontSize = 1.0)

p.gridImage(0,3,"./QIC_Figures/QIC2_DiVincenzo_1.png", height = 100)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Single Qubit: Mathematical description")

p.makeGrid(4,4)
p.gridText(0,3,r"""

* DVC1 Qubits

""", fontSize = 1.0)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Single Qubit: Mathematical description")

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bloch Sphere")

p.makeGrid(2,2)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC2_Bloch_2.png", height = 200)

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bloch Sphere")

p.makeGrid(2,2)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC2_Bloch_2.png", height = 200)

########################################
#############  New slide  ##############
########################################

#p.newSlide()
#p.title("Qubit (two-level system): Examples ")

#p.makeGrid(4,4)

#p.gridImage(0,2,"./QIC_Figures/QIC1_superconducting_3.jpg", height = 100)
#p.gridImage(0,3,"./QIC_Figures/QIC1_superconducting_1.png", height = 100)

#p.gridImage(1,2,"./QIC_Figures/QIC1_ions_1.jpg", height = 100)
#p.gridImage(1,3,"./QIC_Figures/QIC1_ions_2.png", height = 100)

#p.gridImage(2,3,"./QIC_Figures/QIC11_Atom_QC_Review_2.png", height = 100)


########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.2 Summary")
p.leftText(r"""
** QIC.2 Notes ** 

Summary 


""", fontSize = 1.0)
p.rightImage("./QIC_Figures/QIC2_Summary.png", height = 400)

p.save("./QIC_2.html")
