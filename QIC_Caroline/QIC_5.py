from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_5_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.5: Ph 30, 14.00 Monday Jan 24, 2022")

p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.4 Summary **

""", fontSize = 1.0)

p.gridText(1,0,r"""

**Rotation matrices**

""", fontSize = 1.0)

p.gridImage(1,2,"./QIC_Figures/QIC4_rotation.png", height = 100, textBelow = r""" """, fontSize = 0.5)

p.gridText(1,3,r"""

\begin{eqnarray} {\sf R}_y^\Theta & = & 
\left( 
\begin{array}{cc} 
\cos \Theta/2  & -\sin \Theta/2\\\
\sin \Theta/2 & \cos \Theta/2
\end{array} 
\right)  
\end{eqnarray}

""", fontSize = 0.5)

p.gridText(2,0,r"""

EM field + qubit

**Rabi solution**

""", fontSize = 1.0)

p.gridImage(2,2,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 100, textBelow = r""" 
\begin{eqnarray}
\Omega = \frac{\langle 0 \vert -\boldsymbol{d}\cdot\boldsymbol{\cal E}_0\vert 1\rangle}{\hbar}
= \frac{d{\cal E}_0}{\hbar}
\end{eqnarray}
 """, fontSize = 0.5)

p.gridText(2,3,r"""

\begin{eqnarray} {\cal H}_{\rm int} & = & 
\frac{\hbar}{2}\left( 
\begin{array}{cc} 
\Delta & \Omega {\rm e}^{ - {\rm i}\phi_L }  \\\
\Omega {\rm e}^{  {\rm i}\phi_L } & -\Delta
\end{array}
\right)  
\end{eqnarray} 


""", fontSize = 0.5)

#\Delta & \Omega  {\rm e}^{-{\rm i}\phi_{\rm L}} \\\
#\Omega {\rm e}^{{\rm i}\phi_{\rm L}} & \Delta


#\begin{eqnarray}\Delta = 0 \end{eqnarray} 

#\begin{eqnarray} {\sf R}(\Omega t, \phi_{\rm L}) & = & 
#\left( 
#\begin{array}{cc} 
#\cos\textstyle{\Omega t\over 2} & -{\rm i}{\rm e}^{-{\rm i}\phi_{\rm L}}\sin\textstyle{\Omega t\over 2}\\\
#-{\rm i}{\rm e}^{{\rm i}\phi_{\rm L}}\sin\textstyle{\Omega t\over 2} & \cos\textstyle{\Omega t\over 2}
#\end{array} 
#\right)  
#\end{eqnarray} 

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("**QIC.5: Outline**")

p.makeGrid(3,3)
p.gridText(0,0,r"""

**Single-qubit gates (DVC2)**

* Rabi oscillations

* $\pi/2$, $\pi$, $2\pi$ pulses.

""", fontSize = 1.0)

p.gridImage(0,2,"./QIC_Figures/QIC5_pi_over_2.png", height = 150, textBelow = r""" """, fontSize = 0.5)

p.gridText(1,0,r"""

* Hadamard gate

""", fontSize = 1.0)

p.gridImage(1,2,"./QIC_Figures/BlochDM_Hxz.png", height = 200)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit control using EM fields: Rabi solution **
""")

p.makeGrid(4,4)
p.gridText(0,0,r"""

\begin{eqnarray} {\cal H}_{\rm int} & = & 
\frac{\hbar}{2}\left( 
\begin{array}{cc} 
\Delta & \Omega {\rm e}^{ - {\rm i}\phi_L }  \\\
\Omega {\rm e}^{  {\rm i}\phi_L } & -\Delta
\end{array}
\right)  
\end{eqnarray} 

See QIC.4 Appendix for more details.

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 150,
            textBelow="", fontSize = 0.5)
            
########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit control using EM fields: ${\sf R}_z$ and ${\sf R}_y$ rotations **
""")

p.makeGrid(4,4)
p.gridText(0,2,r"""

\begin{eqnarray} {\cal H}_{\rm int} & = & 
\frac{\hbar}{2}\left( 
\begin{array}{cc} 
\Delta & \Omega {\rm e}^{ - {\rm i}\phi_L }  \\\
\Omega {\rm e}^{  {\rm i}\phi_L } & -\Delta
\end{array}
\right)  
\end{eqnarray} 

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 150,
            textBelow="", fontSize = 0.5)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Rabi solution $\rightarrow {\sf R}_y$ rotation**""")

p.leftText(r"""

\begin{eqnarray} 
\Delta = 0
\end{eqnarray}

** Rabi solution **

\begin{eqnarray} {\sf R}(\Omega t, \phi_{\rm L}) & = & 
\left( 
\begin{array}{cc} 
\cos\textstyle{\Omega t\over 2} & -{\rm i}{\rm e}^{-{\rm i}\phi_{\rm L}}\sin\textstyle{\Omega t\over 2}\\\
-{\rm i}{\rm e}^{{\rm i}\phi_{\rm L}}\sin\textstyle{\Omega t\over 2} & \cos\textstyle{\Omega t\over 2}
\end{array} 
\right)  
\end{eqnarray}

** Set field phase **

\begin{eqnarray} 
\phi_{\rm L} = \pi/2
\end{eqnarray}

** Rotation angle **

\begin{eqnarray} 
\Theta = \Omega t
\end{eqnarray}

**Rabi solution $\rightarrow {\sf R}_y$ rotation**

\begin{eqnarray} {\sf R}_y^\Theta & = & 
\left( 
\begin{array}{cc} 
\cos \Theta/2  & -\sin \Theta/2\\\
\sin \Theta/2 & \cos \Theta/2
\end{array} 
\right)  
\end{eqnarray}

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_Ry.html", height=800)

########################################
############# NEW slide ##############
########################################

p.newSlide()

p.title("**Rabi oscillations $\\rightarrow$ single-qubit gates**")

p.makeGrid(4,4)
p.gridText(0,0,r"""

**$\pi/2$, $\pi$, $2\pi$ pulses**

""", fontSize = 1.0)

p.gridImage(0,3,"./QIC_Figures/QIC5_rabi_oscillation.png", height = 100, textBelow = r""" """, fontSize = 0.5)

########################################
############# NEW slide ##############
########################################

p.newSlide()

p.title("**$\pi/2$ pulse**")

p.makeGrid(2,2)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC5_pi_over_2.png", height = 240, textBelow = r""" """, fontSize = 0.5)

########################################
############# NEW slide ##############
########################################

p.newSlide()

p.title("**$\pi$ pulse**")

p.makeGrid(2,2)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC5_pi.png", height = 240, textBelow = r""" """, fontSize = 0.5)

########################################
############# NEW slide ##############
########################################

p.newSlide()

p.title("**$2\pi$ pulse**")

p.makeGrid(2,2)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC5_2pi.png", height = 240, textBelow = r""" """, fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Hadamard gate (${\sf H}$)**""")

p.makeGrid(4,4)
p.gridText(0,3,r"""

* What is it?

* Why is it important?

* How to realise ${\sf H}$ using EM field?
""", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC5_Hadamard.png", height = 200, textBelow = r""" """, fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_{xz}$ rotation**""")

p.leftText(r"""

Hadamard $\vert 0\rangle \rightarrow \vert +\rangle \rightarrow \vert 0\rangle$

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_Hxz.html", height=800)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_{yz}$ rotation**""")

p.leftText(r"""

Change field phase to $\phi_{\rm L}$

Not a Hadamard 

$\vert 0\rangle \rightarrow \vert +{\rm i}\rangle \rightarrow \vert 0\rangle$

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_Hyz.html", height=800)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Rabi oscillations: real qubits **
""")

p.makeGrid(4,4)

p.gridText(0,0,r"""

Superconductors
""", fontSize = 0.5)

p.gridImage(0,2,"./QIC_Figures/QIC5_superconducting_Rabi_oscillation_0.png", height = 100,
            textBelow="", fontSize = 0.25)
p.gridImage(0,3,"./QIC_Figures/QIC5_superconducting_Rabi_oscillation_1.png", height = 140,
            textBelow=r"""https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.107.240501""", fontSize = 0.25)

p.gridText(1,0,r"""

Atoms
""", fontSize = 0.5)

p.gridImage(1,2,"./QIC_Figures/QIC5_Sr_Rabi_oscillation_0.png", height = 100,
            textBelow="", fontSize = 0.5)
p.gridImage(1,3,"./QIC_Figures/QIC5_Sr_Rabi_oscillation_1.png", height = 100,
            textBelow="", fontSize = 0.5)

p.gridText(2,0,r"""

Silicon
""", fontSize = 0.5)


p.gridImage(2,3,"./QIC_Figures/QIC1_Si_2_qubit_0.png", height = 100,
            textBelow="Mills et al, arXiv:2111.1937", fontSize = 0.5)


########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.5 Summary")
p.leftText(r"""
** QIC.5 Notes ** 

Summary 

""", fontSize = 1.0)
p.rightImage("./QIC_Figures/QIC5_Summary.png", height = 400)

p.save("./QIC_5.html")
