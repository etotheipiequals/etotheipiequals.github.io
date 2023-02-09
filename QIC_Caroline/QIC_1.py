from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_1_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""



** C. S. Adams**

**Quantum information and computing** 

** QIC.1 Ph30, 14.00 Monday Jan 10, 2022 **

""", fontSize = 1.0)

p.leftText(r"""

**Aims**

* How to build a **quantum computer**?

* Forefront of current knowledge (decoherence and entanglement) and technology.
 
""")

p.rightImage("./Figures/Ramsey_static.png", height = 400) ########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.0 Outline")
p.leftText(r"""


** Resources (Ultra) **

* Notes

* Slides (with annotations) .pdf (without).html files

** Outline **

* Lecture 1--10: Theoretical framework

* Lecture 11--18: Practical implementation (atoms, lasers and qubits)


""")
p.rightImage("./Figures/QIC_0_p_1.png", height = 400)


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""
**QIC.1** 

C. S. Adams,  Durham University, Jan 2021.
""", fontSize = 1.0)

p.leftText(r"""

Outline

* What is a qubit?

* Examples

* Why quantum computing?

* Exponential scaling.
 
""")

p.rightImage("./Figures/Ramsey_static.png", height = 400) 

########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.1 Notes")
p.leftText(r"""
* QIC.1 Notes 

 * *Circuit Quantum Electrodynamics*, A Blais, AL Grimsmo, SM Girvin, A Wallraff, 
Rev Mod Phys **93**, 25005 (2021)
https://arxiv.org/abs/2005.12667

""", fontSize = 0.5)
p.rightImage("./Figures/QIC_1_p_1.png", height = 400)


##################################/######
#############  New slide  ##############
########################################

p.newSlide()
p.title("What is quantum computing? Bits vs. Qubits")


p.makeGrid(4,4)
p.gridText(0,2,r"""

Classical bit 0 or 1

Quantum bit 0 and 1 

(but only if we do not look!)
""", fontSize = 0.5)

p.gridImage(0,3,"./Figures/Bit_vs_Qubit.JPG", height = 100)

p.gridText(1,2,r"""

** $\vert \psi\rangle = a \vert 0 \rangle + b \vert 1 \rangle$ **

""", fontSize = 0.5)



p.gridImage(1,3,"./QIC_Figures/QIC1_qubit.png", height = 100)


p.gridImage(2,2,"./Figures/2s12m12.png", height = 100)

p.gridImage(2,3,"./Figures/2p12m12.png", height = 100)




#p.gridImage(2,3,"./Figures/Feynman_85.png", height = 100)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("What is a qubit?")
p.spanCenterText(r"""

** $\vert \psi\rangle = a \vert 0 \rangle + b \vert 1 \rangle$ **

""", fontSize = 2.0)

p.spanCenterText(r"""

*The wave function [or state vector] is NOT a description of the quantum object, it is a prescription for what to expect when we make a measurement on that object*. Phillip Ball, *Quantum mechanics is not weird*, Qiskit Seminar, 12th February 2021.

""", fontSize = 0.5)


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Qubit (two-level system): Examples ")

p.makeGrid(4,4)

p.gridImage(0,1,"./QIC_Figures/QIC1_superconducting_3.jpg", height = 100, textBelow="Google's Sycamore processor", fontSize = 0.5)

p.gridImage(0,2,"./QIC_Figures/QIC1_superconducting_3.png", height = 100, textBelow=" Qubits (red): tuning (dark blue); control (purple). Coupling (orange). Read-out (blue). https://arxiv.org/abs/1801.07904", fontSize = 0.5)

p.gridImage(0,3,"./QIC_Figures/QIC1_superconducting_1.png", height = 100, textBelow="Blais et al, Rev Mod Phys **93**, 25005 (2021)", fontSize = 0.5)



p.gridImage(1,2,"./QIC_Figures/QIC1_ions_1.jpg", height = 100, textBelow="Honeywell", fontSize = 0.5)
p.gridImage(1,3,"./QIC_Figures/QIC1_ions_2.png", height = 100, textBelow="Chris Monroe, Duke and IonQ", fontSize = 0.5)

p.gridImage(2,3,"./QIC_Figures/QIC1_Rydberg_array.png", height = 100, textBelow="Barredo et al, Nature  **561**, 79 (2018)", fontSize = 0.5)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Qubit (two-level system): Examples ")

p.makeGrid(4,4)

p.gridImage(0,2,"./QIC_Figures/QIC1_pol_left_right.png", height = 100)
p.gridImage(0,3,"./QIC_Figures/QIC1_photons_1.png", height = 100)

p.gridImage(1,2,"./QIC_Figures/QIC1_semi.png", height = 100,  textBelow="Borjan et al, Nature  **577**, 195 (2020)", fontSize = 0.5)
p.gridImage(1,3,"./QIC_Figures/QIC1_Si_2_qubit_0.png", height = 100,  textBelow="Mills et al, arXiv:2111.1937", fontSize = 0.5)

########################################
############# NEW slide ############## Grid with text 
########################################

p.newSlide()
p.title("Why quantum computing?")
p.makeGrid(4,4)
p.gridText(0,1,r"""
*no exponential is forever... But we can delay ``forever''*. 

Gordon Moore

Slide 29 in *No_Exponential_is_Forever* at the International Solid State Circuits Conference 50th anniversary, 2003.
""", fontSize = 0.5)

p.gridImage(0,2,"./Figures/Moores_law_48_years.png", height = 100)
p.gridImage(0,3,"./QIC_Figures/QIC1_feature_size.png", height = 100)

p.gridImage(1,3,"./Figures/Moores_law_energy.png", height = 100,  textBelow="SIA/SRC report 2016", fontSize = 0.5)
p.gridImage(2,2,"./Figures/Feynman_85.png", height = 100)
p.gridImage(2,3,"./QIC_Figures/QIC1_energy_2.png", height = 100)


########################################
############# INTERACTIVE FIGURE  ##############
########################################

p.newSlide()
p.title("Quantum advantage")


########################################
############# INTERACTIVE FIGURE  ##############
########################################

p.newSlide()
p.title("Quantum advantage")


########################################
#############  New slide  ############## What I do? Teaching 
########################################

p.newSlide()

p.title("QIC.1 Summary")
p.leftText(r"""
** QIC.1 Notes ** 

Summary 


""", fontSize = 1.0)
p.rightImage("./QIC_Figures/QIC1_summary.png", height = 400)



p.save("./QIC_1.html")


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
