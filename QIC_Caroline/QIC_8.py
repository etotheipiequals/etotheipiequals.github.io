from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_8_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("QIC.8: Ph 30, 14.00 Thursday Feb 3, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.7 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

**Quantum inference**

""", fontSize = 1.0)

p.gridText(1,1,r"""

* Ramsey inteferometer.

* Like optical, but in Hilbert space

""", fontSize = 0.5)

p.gridText(2,1,r"""


""", fontSize = 0.5)

p.gridImage(2,2,"./Figures/Ramsey_static.png", height = 300)


########################################
p.newSlide()
p.title("**QIC.8: Two qubits**")
p.makeGrid(3,3)
p.gridText(0,0,r"""

**Outline**

""", fontSize = 1.0)

p.gridText(1,0,r"""

* Two-qubit operators

* Engtanglement: Bell states

* Two-qubit operators

* Breakdown of Bloch sphere picture


""", fontSize = 0.5)

p.gridImage(1,1,"./Figures/Bell_irrotational.JPG", height = 200)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two changes everything - quantum entanglement!")


p.leftText(r"""
** Richard Feynman **

*Probability and uncertainty - the quantum mechanical view of nature*, 

Messenger Letures, Cornell, November 18th, 1964.

> *I think I can safely say that nobody understands quantum mechanics*

""")

p.rightIFrame("https://www.youtube.com/embed/41Jc75tQcB0?start=476&end=481", height=315)



########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("What Richard Feynman said!")


p.leftText(r"""
... you'll get down a drain,

... nobody has yet escaped,

... nobody knows how it can be like that.
           
           """)
p.rightIFrame("https://www.youtube.com/embed/41Jc75tQcB0?start=509&end=521", height=315)

p.spanCenterText(r"""
I have spent 30 years down that drain!
""")


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two-qubit states")

p.makeGrid(4,4)


p.gridText(0,3,r""" 

A and B

  
$
\vert\Psi\rangle 
 =  a_{00}\vert 00 \rangle + a_{01}\vert 01 \rangle + a_{10}\vert 10 \rangle + a_{11}\vert 11 \rangle$
""", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two-qubit states")

p.makeGrid(4,4)
p.gridText(0,3,r"""   
\begin{eqnarray}
\vert\Psi\rangle 
 =  a_{00}\vert 00 \rangle + a_{01}\vert 01 \rangle + a_{10}\vert 10 \rangle + a_{11}\vert 11 \rangle
\end{eqnarray}
""", fontSize = 0.5)


p.gridText(1,2,r""" Reduced density matrix for A
\begin{eqnarray}
\rho_{\rm A} = {\rm Tr}_{\rm B}
\left( 
\rho
\right)  \end{eqnarray}
""", fontSize = 0.5)

p.gridImage(2,3, "./QIC_Figures/QIC8_Bell_reduced.png", height = 100,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

p.gridText(1,3,r"""   
\begin{eqnarray}
\left( 
\begin{array}{cc} 
a  + f & c + h  \\\
i  + n & k + p  
\end{array} 
\right)
=
 {\rm Tr}_{\rm B}
\left( 
\begin{array}{cccc} 
a  & b & c & d  \\\
e  & f & g & h  \\\
i  & j & k & l  \\\
m  & n & o & p 
\end{array} 
\right)  
\end{eqnarray}
""", fontSize = 0.5)


########################################
#############  New slide  ##############
########################################


p.newSlide()
p.title("Two-qubit states")

p.makeGrid(4,4)
p.gridText(0,2,r"""

** Bell states ** 

$
\vert\Phi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 00 \rangle \pm \vert 11 \rangle)$
 
$\vert\Psi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 01 \rangle \pm \vert 10 \rangle)$
""", fontSize = 0.5)


p.gridImage(0,3,"./Figures/Bell.jpg", height = 200,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two-qubit operators")

p.makeGrid(4,4)
p.gridText(0,2,r"""
Apply an ${\sf R}_y$ rotation to both qubits.
""", fontSize = 0.5)


p.gridImage(0,3,"./Figures/Bloch_Ry.png", height = 200, 
            textBelow=r"**Figure**:  Bloch sphere $\times 2$?", fontSize = 0.5)


#p.spanCenterImage("./equations/Ry_otimes_Ry.png", height = 200)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bloch sphere?")
p.leftText(r"""


* Excellent to understand single-qubit gates

* Decay and decoherene of single qubit

* But does not work for more than one qubit.

* Fortunately, the density matrix is extendable to any number of qubits.


""")
p.rightImage("./Figures/BlochSphere_Bad.JPG", height = 300)





########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Irrotationality of the Bell state")


p.rightIFrame("./Figures/Bell_Ry_dots.html", height=600)
#p.spanCenterIFrame("./figures/Bell_Ry_dots.html", height=600)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Irrotationality of Bell states")

p.spanCenterText(r"""   
${\small \vert 00\rangle,~ 
\frac{1}{\sqrt{3}}(\sqrt{2}\vert 00\rangle + \vert 11\rangle),~ 
\bbox[5px, border: 2px solid red]{\frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 11\rangle)},~ 
\frac{1}{\sqrt{3}}(\vert 00\rangle + \sqrt{2}\vert 11\rangle),~ 
\vert 11\rangle}$
""")

p.spanCenterImage("./Figures/Bell_irrotational.JPG", height = 200,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bell states are useful!")


p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC8_crypto_1.png", height = 200)
p.gridImage(2,3,"./QIC_Figures/QIC8_crypto_2.png", height = 200)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"${\sf R}_x$ Rotationality of the Bell state")

p.leftText(r"""
$
\vert\Phi^+\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 00 \rangle + \vert 11 \rangle)$
 
$\rightarrow$

$\vert\Psi^+\rangle 
 =  -\textstyle{{\rm i}\over \sqrt{2}}(\vert 01 \rangle + \vert 10 \rangle)$
""")

p.rightIFrame("./Figures/Bell_Rx_dots.html", height=600)
#p.spanCenterIFrame("./Figures/Bell_Ry_dots.html", height=600)



########################################
p.newSlide()
p.title("QIC.8 Summary")
p.leftText(r"""
** QIC.8 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Explain the principle of entanglement and identify entangled states.

* Construct two-qubit operators.
 
* Analyse the properties of Bell states.

* Explain, why the Bloch sphere representation does not work for entangled states, and demonstrate examples such the directionless charactor of the Bloch vector and the irrotationality of Bell state.



""", fontSize = 1.0)

########################################
p.save("./QIC_8.html")

