from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_3_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.3: Ph 30, 14.00 Monday Jan 17, 2022")

p.makeGrid(5,5)
p.gridText(0,0,r"""

** QIC.2 Summary **

""", fontSize = 1.0)

p.gridText(1,1,r"""

5 DiVincenzo Criteria:

Framework

How to build a Qunatum Computer

""", fontSize = 0.5)

p.gridText(1,4,r"""

* Qubit initialisation
* One- and two-qubit gates
* Read-out
* Low decoherence
* Scalability: $2^{100} \sim 10^{30}$

""", fontSize = 0.5)

p.gridImage(1,2,"./QIC_Figures/QIC2_DiVincenzo_1.png", height = 100)

p.gridText(2,1,r"""

DVC 1: Qubits 

* Qubit mathematical

* Qubit diagramatic

""", fontSize = 0.5)

p.gridText(2,2,r"""

\begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \cos\textstyle{\theta\over 2}  \\\ {\rm e}^{{\rm i}\pi}\sin\textstyle{\theta\over 2} \end{array}\right)\end{eqnarray}

""", fontSize = 0.5)

p.gridImage(2,4,"./QIC_Figures/QIC2_Bloch_2.png", height = 100)

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.3: Ph 30, 14.00 Monday Jan 17, 2022")

p.makeGrid(3,3)
p.gridText(0,0,r"""

Pauli matrices

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC3_pauli_1.jpg", height = 100, textBelow = r"""https://physicstoday.scitation.org/doi/pdf/10.1063/1.1359710""", fontSize = 0.5)

p.gridImage(0,2,"./QIC_Figures/QIC3_speedgraphic.jpg", height = 100)

p.gridText(1,0,r"""

Density matrix

""", fontSize = 1.0)

p.gridImage(1,1,"./QIC_Figures/QIC3_vonNeumann.png", height = 200)

p.gridText(1,2,r"""

_In mathematics you don't understand things you just get usd to them._

Quoted in G. Zukav _The Dancing Wu Li Masters_

""", fontSize = 0.5)

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("Pauli martrices: Why?")

p.makeGrid(3,3)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,2,"./QIC_Figures/QIC3_spin.png", height = 100)

p.gridImage(1,2,"./QIC_Figures/QIC3_gates.png", height = 200, textBelow = r"""https://en.wikipedia.org/wiki/Quantum_logic_gate""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Pauli martrices: What?")

p.makeGrid(3,3)
p.gridText(0,0,r"""


""", fontSize = 1.0)

p.gridImage(0,2,"./QIC_Figures/QIC3_spin.png", height = 100)

p.gridImage(1,2,"./QIC_Figures/QIC3_gates.png", height = 200, textBelow = r"""https://en.wikipedia.org/wiki/Quantum_logic_gate""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Pauli martrices: Worked example")

p.makeGrid(3,3)
p.gridText(0,2,r"""

Find the expectation value of $\sigma_y$ for an arbitary qubit state. [Hint: Use spherical polar coordinates]

""", fontSize = 0.5)

p.gridText(1,2,r"""

Sketch the Bloch sphere. Label the axes in terms of Pauli matrices. Mark and label for cartesian components of the Bloch vector for an arbitrary state vector $\vert \psi\rangle$.

""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Density matrix: Why?")

p.makeGrid(3,3)
p.gridText(0,0,r"""

**Advantages:**

* Represent both pure and mixed states (state vector pure only).

* Represent a part of a multi-qubit state.

""", fontSize = 0.5)

p.gridText(1,0,r"""

**Visualisation**

$\vert \rho_{ij}\vert \leq 1 $

""", fontSize = 0.5)

p.gridImage(1,1,"./Figures/Colour_Wheel.JPG", height = 100,
            textBelow="**Colour wheel** Amplitude proportional to transparency. Phase given by colour.", fontSize = 0.5)

p.gridImage(1,2,"./Figures/QFT_dots.png", height = 100, textBelow="**Quantum Fourier transform:** 5 qubits. https://en.wikipedia.org/wiki/Quantum_Fourier_transform", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Density matrix**

**Pure states: $\rho=\vert\psi\rangle\langle\psi\vert$ **
""")

p.makeGrid(4,4)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridText(2,2,r"""

**Visualisation**

""", fontSize = 1.0)

p.gridImage(2,3,"./QIC_Figures/QIC3_BlochDM_H.png", height = 100,
            textBelow="", fontSize = 0.5)

#p.gridImage(0,2,"./Figures/QFT_circuit_diagram.png", height = 100)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Density matrix**

**Pure states: $\rho=\vert\psi\rangle\langle\psi\vert$ **
""")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Density matrix**

**Pure states: $\rho=\vert\psi\rangle\langle\psi\vert$ **
""")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit Density matrix**""")

p.leftText(r"""

\begin{eqnarray} \rho & = & \frac{1}{2}
\left( 
\begin{array}{cc} 
1 + w & u - {\rm i} v\\\
u + {\rm i}v & 1 - w 
\end{array} 
\right)  
\end{eqnarray} 

\begin{eqnarray} u & = & \sin\theta \cos\phi\\\
v & = & \sin\theta \sin\phi\\\
w & = & \cos\theta 
\end{eqnarray} 

""")

p.rightIFrame("./QIC_Figures/BlochDM_6.html", height=800)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit Density matrix**""")

p.leftText(r"""

\begin{eqnarray} \rho & = & \frac{1}{2}
\left( 
\begin{array}{cc} 
1 + w & u - {\rm i} v\\\
u + {\rm i}v & 1 - w 
\end{array} 
\right)  
\end{eqnarray} 

\begin{eqnarray} u & = & \sin\theta \cos\phi\\\
v & = & \sin\theta \sin\phi\\\
w & = & \cos\theta 
\end{eqnarray} 

""")

p.rightIFrame("./QIC_Figures/BlochDM_theta_phi.html", height=800)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Decoherence **
""")
p.makeGrid(4,4)
p.gridText(0,2,r"""

'Environment' perturbs energy levels

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC3_qubit_noise.png", height = 100,
            textBelow="", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Decoherence **
""")

p.makeGrid(4,4)
p.gridText(0,2,r"""

'Environment' perturbs energy levels

""", fontSize = 0.5)


p.gridImage(0,3,"./QIC_Figures/QIC3_qubit_noise.png", height = 100,
            textBelow="", fontSize = 0.5)

p.gridImage(2,3,"./QIC_Figures/QIC3_random_phase.png", height = 100,
            textBelow="", fontSize = 0.5)

########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.3 Summary")
p.leftText(r"""
** QIC.3 Notes ** 

Summary 

""", fontSize = 1.0)
p.rightImage("./QIC_Figures/QIC3_Summary.png", height = 400)

p.save("./QIC_3.html")
