from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=False,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/Quantum_Semiotics_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# Title slide ##############
########################################


p.newSlide()
p.spanCenterText(r"""
#Quantum Semiotics

C. S. Adams

Quantum Information Seminar

Mexican Physical Society

September 30, 2021
""")

p.spanCenterImage("./figures/Blockade_0.png", height = 200)


########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("Where am I?")
p.leftText(r"""
* Durham - 400 km North of London

""")
p.rightImage("./figures/Location_Pop_Map.jpg",
            textBelow="**Figure**:  England population density. ")


########################################
#############  New slide  ############## What I do? Research 
########################################

p.newSlide()

p.title("What I do?")
p.leftText(r"""
** Research **

** Experimental quantum optics using atoms **

* *Rydberg physics*, Šibalić, N, Adams, CS, IOP Publishing 2018

* Quantum non-linear optics, *Collectively encoded Rydberg qubit* Spong et al PRL **127**, 063604 (2021). 

* THz imaging, Downes et al, Phys. Rev. X **10**, 011027 (2020) 
""")
p.rightImage("./figures/Rydberg_book_QO_THz.jpg", height = 450)

########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("What I do?")
p.leftText(r"""
** Teaching **

* *Optics f2f*, CS Adams and IG Hughes, OUP 2018

* *Optical rotation of white light*, Am. J. Phys. **88**, 247 (2020) 

""")
p.rightImage("./figures/Opticsf2f.jpg", height = 200)
p.rightImage("./figures/Arago_red.jpg", height = 100)

########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("What I do?")
p.leftText(r"""
** Teaching **

* 2004 - 09 Atoms, Photons and Qubits

* 2019 - Quantum information and computing

""")
p.rightImage("./figures/QIC_2004.jpg", height = 300)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum semiotics")
p.leftText(r"""
** Outline **

1. What is the problem?

2. What is semiotics?

3. What is quantum semiotics?

4. Some ideas and examples.


""")
p.rightImage("./figures/Blockade_0.png", height = 300)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum computing: Bits vs. Qubits")

p.spanCenterImage("./figures/Bit_vs_Qubit.JPG", height = 200,
            textBelow="**Figure**:  Classical bit vs. qubit (can be 0 and 1 but only if we do not look!) ")

p.spanCenterText(r"""

** $\vert \psi\rangle = a \vert 0 \rangle + b \vert 1 \rangle$ **

""")

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(
    questionText="#The amount of information that can be stored in a qubit is",
    answersText=[r"One bit.",
                 r"Two bits.",
                 r"Infinite.",
                 r"In depends on the measurement."]
)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 1: What is the problem?")


p.leftText(r"""
** Richard Feynman **

*Probability and uncertainty - the quantum mechanical view of nature*, 

Messenger Letures, Cornell, November 18th, 1964.

> *I think I can safely say that nobody understands quantum mechanics*

""")

p.rightIFrame("https://www.youtube.com/embed/41Jc75tQcB0?start=476&end=481", height=315)


########################################
############# QUIZ slide ##############
########################################

p.newQuiz(
    questionText="#The amount of information that can be retrieved from a qubit is",
    answersText=[r"One bit.",
                 r"Two bits.",
                 r"Infinite.",
                 r"In depends on the measurement."]
)

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
Quantum semiotic is my last hope of getting out of that drain!
""")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Paradox?")


p.makeGrid(3,3)
p.gridText(0,0,r"""
Qubit stores infinite information but we can only see one bit
""")
p.gridImage(0,1,"./figures/Bit_vs_Qubit.JPG", height = 100)


p.gridText(1,0,r"""
$~~$  *If you can see it, then it is not quantum*
""")

p.gridImage(1,1,"./figures/Nikola.jpg", height = 100)



p.gridText(2,0,r"""
$~~$  Something hidden?
""")

p.gridImage(2,1,"./figures/cylinder.jpg", height = 100)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(
    questionImage="./figures/Bohr.jpg",
    questionText=r"""## Which of the following are superpositions of the form, $\vert \psi\rangle = \textstyle{1\over\sqrt{2}}\left( \vert 0 \rangle \pm  \vert 1 \rangle \right)$ ?""",
    answersImage=[
        "./figures/2s12m12.png",
        "./figures/2p12m12.png",
        "./figures/1s12m12.png",
        "./figures/2s12m12+2p12m32.png",
        "./figures/2s12m12+2p12m12.png",
        "./figures/2p12m32.png",
    ],
)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 2: What is semiotics?")
p.leftText(r"""
** The doctrine of signs ** (or symbols)
""")
p.rightImage("./figures/Locke.jpg", height = 300)

p.makeGrid(4,4)
p.gridText(0,0,r"""
$~~$ Language
""")
p.gridImage(0,1,"./figures/Alphabets.JPG", height = 200)
p.gridText(0,2,r"""
$~~$ Maps  
""")
p.gridImage(0,3,"./figures/Maps.JPG", height = 140)

p.gridText(1,0,r"""
$~~$  Computing
""")
p.gridImage(1,1,"./figures/Computing_Punch_Card_Dynamicland.JPG", height = 100)

p.gridText(1,2,r"""
$~~$  Physics
""")
p.gridImage(1,3,"./figures/Equations_Maxwell_StandardModel.JPG", height = 200)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 2: What is semiotics?")

p.makeGrid(3,3)
p.gridText(0,0,r"""
$~~$ ** Images in physics **
""")
p.gridImage(0,1,"./figures/Leonardo.jpg", height = 300)

p.gridText(1,0,r"""
$~~$  Diagrammatic reasoning
""")
p.gridImage(0,2,"./figures/Leonardo_Sketches.JPG", height = 200)


'''
########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 2: What is semiotics? Images and Symbols in physics")

p.leftImage("./figures/Hertz.jpg", height = 200,
            textAbove="*The principles of mechanics* Heinrich Hertz (1899).",
            textBelow="We form for ourselves **images** or **symbols** of external objects",
            )
p.rightImage("./figures/Hertz_expt.jpg", height = 200,
            textAbove="... one image may be more suitable for one purpose, another for another.",
            textBelow=" **Figure**:  First transmission of EM waves 1887"
            )

'''


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("What is quantum semiotics: Quantum information and computing")
p.leftText(r"""

Semiotic representation of a qubit

$\vert \psi\rangle = a \vert 0 \rangle + b \vert 1 \rangle$


$a =\cos \frac{\theta}{2}$, $b={\rm e}^{{\rm i}\phi}\sin\frac{\theta}{2}$

** The Bloch sphere **

""")
p.rightImage("./figures/BlochSphere1.jpg", height = 200, 
            textBelow=r"**Figure**:  Bloch sphere representation of a qubit: Bloch vector (blue). Single-qubit gates performed as rotations about a torque vector, $\boldsymbol{\hat{n}}$, (yellow).")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Qubit rotation matrix")

p.leftImage("./equations/R_n.png", height = 70,
#            textAbove="**Qubit rotation matrix**",
           )

p.rightImage("./figures/Two_level_system.JPG"#, #height = 300,
#            textAbove="**Two level system**"
#            textBelow="**Two level system** "
            )

p.spanCenterText(r"""

${\small \Theta=\Omega_{\rm eff}t}$ 

${\small \Omega_{\rm eff}(n_x,n_y,n_z)=(\Omega\cos \phi_{\rm L},\Omega\sin \phi_{\rm L},\Delta)}$


${\small \Omega_{\rm eff}=(\Omega^2+\Delta^2)^{1/2}}$ 

""")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum semiotics: Quantum information and computing")
p.leftText(r"""
** Qunatum dynamics **

1. Choose $\Delta = 0$, $\phi_{\rm L} = \pi/2$

2. An ${\sf R}_y$ rotation!


""")
p.rightIFrame("./figures/Bloch_Ry.html", height=600)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Quantum information and computing")
p.leftText(r"""
** The perfect Bloch sphere? **
""")
p.rightImage("./figures/BlochSphere_Bad.JPG", height = 300)

p.spanCenterText(r"""   
What is the problem? Let's look at two-qubit states.
""")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two-qubits")
p.spanCenterText(r"""   
$
\vert\Psi\rangle 
 =  a_{00}\vert 00 \rangle + a_{01}\vert 01 \rangle + a_{10}\vert 10 \rangle + a_{11}\vert 11 \rangle$
""")

p.leftText(r"""

** Bell states ** 

$
\vert\Phi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 00 \rangle \pm \vert 11 \rangle)$
 
$\vert\Psi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 01 \rangle \pm \vert 10 \rangle)$
""")


p.rightImage("./figures/Bell.jpg", height = 300,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bell states are useful!")

p.leftText(r"""
$
\vert\Phi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 00 \rangle \pm \vert 11 \rangle)$
 
$\vert\Psi^{\pm}\rangle 
 =  \textstyle{1\over \sqrt{2}}(\vert 01 \rangle \pm \vert 10 \rangle)$
""")


p.rightImage("./figures/Quantum_Crypt_PhysWorld.jpg", height = 400,
#            textAbove="**Colour wheel**",
#            textBelow="**Colour wheel** Amplitude proportional to transparency. Phase given by colour."
            )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two-qubit operators")
p.leftText(r"""   
Apply an ${\sf R}_y$ rotation to both qubits.
""")

p.rightImage("./figures/Bloch_Ry.png", height = 200, 
            textBelow=r"**Figure**:  Bloch sphere $\times 2$?")


p.spanCenterImage("./equations/Ry_otimes_Ry.png", height = 200,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Irrotationality of the Bell state")


p.spanCenterImage("./equations/R2y_Phi+.png", height = 200,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

p.spanCenterText(r"""   
Apply an ${\sf R}_y$ rotation to both qubits. Nothing happens!

Bloch sphere picture doesn't work!
""")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Alternative to the Bloch sphere")

p.spanCenterText("""
**Must** be able to visualise arbitrary multi-qubit states including **entangled** states. See also Migdal PhD ICFO (2014) Vlastakis PhD Yale (2015). Craig Gidney http://algassert.com/quirk
""")

p.leftImage("./equations/rho_uvw.png", height = 70,
            textAbove=r"**The density matrix** $\rho=\vert\psi\rangle\langle\psi\vert$",
            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real.")


p.rightImage("./figures/Colour_Wheel.JPG", height = 150,
#            textAbove="**Colour wheel**",
            textBelow="**Colour wheel** Amplitude proportional to transparency. Phase given by colour.")


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bloch sphere vs the density matrix")


p.spanCenterIFrame("./figures/BlochDM_Ry_landscape.html", height=600)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Bloch sphere vs the density matrix")


p.spanCenterIFrame("./figures/BlochDM_Rx_landscape.html", height=600)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Decoherence: Bloch sphere vs the density matrix")


p.spanCenterIFrame("./figures/BlochDM_T2_landscape.html", height=600)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Irrotationality of the Bell state")


p.rightIFrame("./figures/Bell_Ry_dots.html", height=600)
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

p.spanCenterImage("./figures/Bell_irrotational.JPG", height = 200,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

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

p.rightIFrame("./figures/Bell_Rx_dots.html", height=600)
#p.spanCenterIFrame("./figures/Bell_Ry_dots.html", height=600)


########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("Experimental example: Rydberg blockade")


p.spanCenterImage("./figures/QIC17_Blockade_6.png", height = 400,
            textBelow=r"",
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("Experimental example: Rydberg blockade")

p.leftImage("./figures/Blockade_radius.JPG", height = 300,
#            textAbove="**Two level system**"
#            textBelow="**Two level system** "
            )

p.rightImage("./equations/H_Ryd.png", height = 100,
            textBelow=r"Rydberg blockade $V_{\rm vdW}\gg \Omega$",
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"Rydberg blockade $V_{\rm vdW}\gg \Omega$:  coupled basis")

p.spanCenterText(r"""
${\small \vert 00\rangle \rightarrow  \vert 00\rangle}$

${\small \vert 0{\rm r}\rangle, \vert {\rm r}0\rangle \rightarrow
\Psi^\pm = \frac{1}{\sqrt{2}}(\vert 0{\rm r}\rangle \pm\vert {\rm r}0\rangle) }$ """)


p.leftImage("./equations/R_Ryd.png", height = 70
           )
p.rightImage("./equations/H_Ryd_dashed.png", height = 70
           )

p.spanCenterImage("./figures/Blockade_coupled_basis.JPG", height = 300,
#            textAbove="**Two level system**"
#            textBelow="**Two level system** "
                 )


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title(r"Rydberg blockade dynamics: vary $V_{\rm vdW}/ \Omega$")

p.leftText(r"""

""")

p.rightIFrame("./figures/Blockade_dots.html", height=600)
#p.spanCenterIFrame("./figures/Bell_Ry_dots.html", height=600)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Rydberg blockade: Dynamics")


p.spanCenterImage("./figures/Blockade_1.png", height = 300,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Endless examples!")

p.spanCenterImage("./figures/QFT_circuit_diagram.png", height = 100,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

p.spanCenterImage("./figures/QFT_dots.png", height = 400,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Our recent experiment")

p.spanCenterImage("./figures/nick_prl_1.png", height = 180)

p.makeGrid(4,3)

p.gridText(1,0,r"""
Use Rydberg blockade to store one photon
""")
p.gridImage(1,1,"./figures/g2_flash.png", height = 240)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Our recent experiment")


p.spanCenterImage("./figures/nick_prl_1.png", height = 180)

p.makeGrid(4,3)

p.gridImage(1,0,"./figures/nick_prl_2.png", height = 240)

p.gridImage(1,1,"./figures/nick_prl_3.png", height = 240)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Summary")

p.leftText(r"""

1. We need better tools to visualise QM. 

2. The density matrix is a good choice because it contains complete information about the state, and is scalable to $N$ qubits.

3. By visualise quantum states, we turn quantum mechanics into an image recogition task.

4. Quantum computing, imaging recognisation, machine learning and AI, all begin to look the same!

""")


p.rightImage("./figures/QFT_dots.png", height = 400,
#            textAbove="**The density matrix**",
#            textBelow="$(u,v,w)$ are the components of the Bloch vector. All real."
           )

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Acknowledgements: Nikola Šibalić")

p.spanCenterIFrame("./figures/Wigner_interactive.html", height=600)


p.save("./Quantum_Semiotics.html")



'''

################## OLD SLIDES #################


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 3: What is quantum semiotics?")

p.makeGrid(3,3)
p.gridText(0,0,r"""
** Example:** 

Wave-particle duality
""")
p.gridImage(0,1,"./figures/deBroglie.jpg", height = 100,
            textBelow=" ...we are to understand descriptions which are certainly **complementary** but at the same time, taken strictly incompatible", fontSize = 0.5)


p.gridImage(0,2,"./figures/Escher_vase.jpg", height = 100,
             textBelow=" ...each of these complementary descriptions [wave or particle] is an idealisation permitting us to present certain aspects...but not all aspects", fontSize = 0.5)

p.gridText(1,0,r"""
$~~$  Something hidden?
""")

p.gridImage(1,1,"./figures/cylinder.jpg", height = 100,
             textBelow=" ...there's more we do not see", fontSize = 0.5)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 3: What is quantum semiotics?")
p.leftText(r"""
** Quantum computing **

Circuits

Gates

States: circles and lines 

Symbols galore!

""")
p.rightImage("./figures/Quirk.jpg", height = 300,
            textBelow="**Figure**:  Quirk ciruit model")

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Part 3: What is quantum semiotics?")
p.leftText(r"""
** Quantum computing **

Circuits

Gates

States: circles, spheres, lines, and histograms

Symbols galore!

""")
p.rightImage("./figures/Qiskit.jpg", height = 300,
            textBelow="**Figure**:  Qiskit ciruit model")
            
            
            
'''            
            







# LIST OF POSSIBLE ELEMENTS:
#
### p.newSlide()   followed by some number of
#
# p.title(markdown_text, fontSize=1):
#
# p.leftText(markdown_text, fontSize=1)
# p.rightText(markdown_text, fontSize=1)
# p.spanText(markdown_text, fontSize=1)
# p.spanCenterText(markdown_text, fontSize=1)
#
# p.leftImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.rightImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.spanImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.spanCenterImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
#
# p.leftIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.rightIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.spanIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1):
# p.spanCenterIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1)
#
# p.leftMyCamera(height=None)
# p.rightMyCamera(height=None)
# p.spanMyCamera(height=None)
# p.spanCenterMyCamera(height=None)
#
# p.leftMP4(source, height=None):
# p.rightMP4(source, height=None)
# p.spanMP4(source, height=None):
# p.spanCenterMP4(source, height=None):
#
###    OR  grid layout
#
# p.newSlide()   followed by
# p.makeGrid(rows, columns, padding="0.3em")    followed by some number of
#
# p.gridText(row, column, markdown_text, fontSize=1)
# p.gridImage(row, column, fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.gridIFrame(row, column, url, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.gridMyCamera(row, column, height=None)
# p.gridMP4(row, column, source, height=None):
#
###    OR quiz
# p.newQuiz(questionText=None, questionImage=None, answersText = None, answersImage=None, fontSize=1 )
#
#   NOTE: quiz does not have p.newSlide before
#   NOTE: Quiz questoin can use both questionText and questionImage
#         but that Quiz answer can use EITHER answersText list or answersImage list
#         and maximum number of answers options supported currently is 6
#
###  NOTE: markdown text input
#          it's best to enclose it between    r""" ... """
#          (note r before the first tripple of ")
#          as in this way multiline input and LaTeX work fine
#
