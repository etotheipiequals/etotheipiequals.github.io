from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_4_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black
########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.4: Ph 30, 14.00 Thursday Jan 20, 2022")

p.leftText(r"""

** QIC.3 Summary **

Pauli matrices

\begin{eqnarray} 
\langle \psi \vert \sigma_x\vert \psi \rangle & = & u
\end{eqnarray} 

\begin{eqnarray} 
\langle \psi \vert \sigma_y\vert \psi \rangle & = & v
\end{eqnarray}
 
\begin{eqnarray} 
\langle \psi \vert \sigma_z\vert \psi \rangle & = & w
\end{eqnarray} 

Density matrix

\begin{eqnarray} \rho & = & \frac{1}{2}
\left( 
\begin{array}{cc} 
1 + w & u - {\rm i} v\\\
u + {\rm i}v & 1 - w 
\end{array} 
\right)  
\end{eqnarray} 

""", fontSize = 0.5)

p.rightImage("./QIC_Figures/BlochDM_theta_phi.png", height = 400)

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("QIC.4: Ph 30, 14.00 Thursday Jan 20, 2022")

p.makeGrid(3,3)
p.gridText(0,0,r"""

Single-qubit gates (DVC2)

Rotation

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC4_rotation.png", height = 200, textBelow = r""" """, fontSize = 0.5)

#p.gridImage(0,2,"./QIC_Figures/QIC3_speedgraphic.jpg", height = 100)

p.gridText(1,0,r"""

EM field + qubit $\rightarrow$ rotation

**Rabi solution**

""", fontSize = 1.0)

p.gridImage(1,1,"./QIC_Figures/QIC4_Rabi.png", height = 400)

p.gridText(1,2,r"""

""", fontSize = 0.5)

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("Rotation martrix")

p.makeGrid(3,3)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,2,"./QIC_Figures/QIC4_rotation.png", height = 100)

##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("Rotation martrix")

p.makeGrid(3,3)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,2,"./QIC_Figures/QIC4_rotation.png", height = 100)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_x$ rotation**""")

p.makeGrid(4,4)

p.gridText(0,3,r"""

**Worked example**: Derive a matrix for a $\pi/2$ rotation about the $x$ axis.

What is the direction of the Bloch vector after this rotation is applied to 

(i) $\vert 0\rangle$ and 

(ii) $\vert 1\rangle$? 

""", fontSize = 0.5)

p.gridText(1,3,r"""

\begin{eqnarray} {\sf R}_x^\Theta & = & 
\left( 
\begin{array}{cc} 
\cos \Theta/2  & -{\rm i}\sin \Theta/2\\\
-{\rm i}\sin \Theta/2 & \cos \Theta/2
\end{array} 
\right)  
\end{eqnarray} 

""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_x$ rotation**""")

p.leftText(r"""

\begin{eqnarray} {\sf R}_x^\Theta & = & 
\left( 
\begin{array}{cc} 
\cos \Theta/2  & -{\rm i}\sin \Theta/2\\\
-{\rm i}\sin \Theta/2 & \cos \Theta/2
\end{array} 
\right)  
\end{eqnarray} 

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_Rx.html", height=800)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_y$ rotation**""")

p.leftText(r"""

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
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_z$ rotation**""")

p.makeGrid(4,4)

p.gridText(0,3,r"""

**Worked example**: Derive a matrix for a $\pi/2$ rotation about the $z$ axis.

What is the direction of the Bloch vector after this rotation is applied to 

$\vert +\rangle = \textstyle{1\over \sqrt{2}}(\vert 0\rangle + \vert 1\rangle)$? 

""", fontSize = 0.5)

p.gridText(1,3,r"""

\begin{eqnarray} {\sf R}_z^\Theta & = & 
\left( 
\begin{array}{cc} 
{\rm e}^{-{\rm i}\Theta/2}  & 0\\\
0 & {\rm e}^{{\rm i}\Theta/2}
\end{array} 
\right)  
\end{eqnarray} 

""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**${\sf R}_z$ rotation**""")

p.leftText(r"""

\begin{eqnarray} {\sf R}_z^\Theta & = & 
\left( 
\begin{array}{cc} 
{\rm e}^{-{\rm i}\Theta/2}  & 0\\\
0 & {\rm e}^{{\rm i}\Theta/2}
\end{array} 
\right)  
\end{eqnarray} 

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_Rz.html", height=800)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit control using EM fields **
""")

p.makeGrid(4,4)
p.gridText(0,2,r"""

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 100,
            textBelow="", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit control using EM fields **
""")

p.makeGrid(4,4)
p.gridText(0,2,r"""

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 100,
            textBelow="", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit control using EM fields **
""")

p.makeGrid(4,4)
p.gridText(0,2,r"""

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 100,
            textBelow="", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"""**Qubit control using EM fields **
""")

p.makeGrid(4,4)
p.gridText(0,2,r"""

""", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 100,
            textBelow="", fontSize = 0.5)

########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.4 Summary")
p.leftText(r"""
** QIC.4 Notes ** 

Summary 

""", fontSize = 1.0)
p.rightImage("./QIC_Figures/QIC4_Summary.png", height = 400)

p.save("./QIC_4.html")
