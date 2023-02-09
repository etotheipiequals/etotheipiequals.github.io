from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_9_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("QIC.9: Ph 30, 14.00 Monday Feb 7, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.8 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

* Two-qubit states 

* Example: Bell states

""", fontSize = 0.5)

p.gridText(0,2, r"""
$
\vert\Phi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 00 \rangle \pm \vert 11 \rangle)$
 
$\vert\Psi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 01 \rangle \pm \vert 10 \rangle)$
""", fontSize = 0.5)

p.gridText(0,3,r"""

* Entangled - non separable

* Entanglment essential to QC.

""", fontSize = 0.5)

p.gridText(1,1,r"""

* Two-qubit operators

""", fontSize = 0.5)

p.gridImage(1,2,"./equations/Ry_otimes_Ry.png", height = 150)

p.gridText(2,1,r"""

* Irrotational property of a Bell state

""", fontSize = 0.5)

p.gridImage(2,2,"./Figures/Bell_irrotational.JPG", height = 300)


########################################
p.newSlide()
p.title("**QIC.9: Two-qubits gates and quantum circuits**")
p.makeGrid(3,3)
p.gridText(0,0,r"""

**Outline**

""", fontSize = 1.0)

p.gridText(0,1,r"""

* How to produce a Bell state - using a quantum circuit?

* Entangling operator - two-qubit gate (DVC2)



""", fontSize = 0.5)

p.gridText(1,0,r"""

* Two-qubit gates: CNOT and SWAP

* Quantum circuit diagrams


""", fontSize = 0.5)

p.gridImage(1,1,"./QIC_Figures/QIC9_GHZ.png", height = 200)

########################################
p.newSlide()
p.title("**QIC.9: Two-qubits gates**")
p.makeGrid(2,2)

p.gridText(0,0,r"""

* Two-qubit gates (DVC2): CNOT, CZ and SWAP

""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC9_two_qubit_gates_1.png", height = 400)


########################################
p.newSlide()
p.title("**CNOT**")
p.makeGrid(4,4)
p.gridImage(0,3,"./QIC_Figures/QIC9_CNOT.png", height = 100)




########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("**CNOT: Entanglement**")
p.makeGrid(4,4)
p.gridImage(1,3,"./QIC_Figures/QIC9_Bell.png", height = 200)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""CPHASE""")
p.makeGrid(4,4)
p.gridImage(0,3,"./QIC_Figures/QIC9_CNOT_CZ.png", height = 200)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""Conditional Ramsey interferometer""")
p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC9_CNOT_CZ.png", height = 200)


p.gridText(1,0,r"""

* Conditional Ramsey interferometer (Hilbert space)

* Conditional optical interferometer (real space)

* QIC.18 Rydberg atoms: 5 laser pulses


""", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC9_KLM_1.gif", height = 200)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum computing with photons (QIC.1)")
p.makeGrid(3,3)

p.gridText(0,0,r"""

* Conditional Ramsey interferometer (Hilbert space)

* Conditional optical interferometer (real space)

""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC9_CNOT_CZ.png", height = 100)

p.gridText(1,0,r"""

Linear optics quantum computing (KLM), Knill et al. Nature **409**, 46 (2001).

""", fontSize = 0.5)

p.gridImage(0,2,"./QIC_Figures/QIC1_photons_1.png", height = 100)


#p.gridImage(1,1,"./QIC_Figures/QIC9_KLM_0.gif", height = 400)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"Photonic CNOT")

p.leftText(r"""
Linear optics quantum computing (KLM), 

Knill et al. Nature **409**, 46 (2001).


* Entanglement is not separable!


* *If you can see it, it is not quantum*

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/CNOT_interactive_v5.html", height=600)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"CNOT: Silicon and Rydberg atoms")


p.leftImage("./QIC_Figures/QIC18_Si_CNOT_SWAP.png", height=500,
textBelow =r"""Mills *et al*, arXiv:2111.1937  """, fontSize = 0.5)
p.rightImage("./QIC_Figures/QIC18_levine_2.png", height=500,
textBelow =r"""Levine *et al*, PRL, **123**, 170503 (2019) """, fontSize = 0.5)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum circuits")
p.makeGrid(2,2)
p.gridImage(0,1,"./QIC_Figures/QIC9_Quirk.png", height = 200, 
textBelow =r""" https://quantum-computing.ibm.com/ and https://algassert.com/quirk""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum circuits")
p.spanCenterIFrame("https://algassert.com/quirk#circuit={%22cols%22:[[%22H%22],[%22%E2%80%A2%22,%22X%22]]}", height = 300) 


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum circuits: Worked example")
p.makeGrid(4,4)
p.gridImage(0,3,"./QIC_Figures/QIC9_GHZ.png", height = 200)

########################################
p.newSlide()
p.title("QIC.9 Summary")
p.leftText(r"""
** QIC.9 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Write down matrices for ${\sf CNOT}$ and $\sqrt{\sf SWAP}$.

* Understand the principle of ${\sf CNOT}$ in terms of a conditional Ramsey interferometer.

* Evaluate the output of simple quantum circuits.

* Work out the state at each layer of simple circuits.




""", fontSize = 1.0)

########################################
p.save("./QIC_9.html")

