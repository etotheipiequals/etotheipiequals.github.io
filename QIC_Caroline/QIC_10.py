from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_10_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("QIC.10: Ph 30, 14.00 Thursday Feb 10, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.9 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

* Two qubit states

""", fontSize = 0.5)

p.gridText(0,2, r"""
${\rm CNOT}$ and ${\rm SWAP}$
""", fontSize = 0.5)


p.gridText(1,1,r"""

* Quantum circuits

""", fontSize = 0.5)



p.gridImage(1,2,"./QIC_Figures/QIC9_GHZ.png", height = 200)


########################################
p.newSlide()
p.title("**QIC.10 : Decoherence, Entanglement, Complementarity: Quantum circuit models**")
p.makeGrid(3,3)
p.gridText(0,0,r"""

**Outline**

""", fontSize = 1.0)

p.gridText(0,2,r"""

* Quantum circuit model of entanglement with the environment

* Entanglement $\rightarrow$ decoherence (loss of fringe visibility)

* Relationship between decoherence, **which-path** information, and complementarity.

* Quantum eraser? 

""", fontSize = 0.5)

p.gridImage(1,2,"./QIC_Figures/QIC10_delayed_choice_quantum_eraser_circuit.png", height = 100)


########################################
p.newSlide()
p.title("**Decoherence due to interaction with the environment**")
p.makeGrid(4,4)
p.gridImage(0,3,"./QIC_Figures/QIC10_decoherence_circuit_1.png", height = 100)



########################################
p.newSlide()
p.title("**Decoherence due to interaction with the environment**")

########################################
p.newSlide()
p.title("**Decoherence due to interaction with the environment**")
p.makeGrid(4,4)
p.gridImage(2,3,"./QIC_Figures/QIC10_decoherence_circuit_2.png", height = 100)



########################################
p.newSlide()
p.title("**Delayed-choice quantum eraser**")
p.makeGrid(2,2)

p.gridText(0,0,r"""

Two concepts

* *Quantum* eraser

* Delayed choice


""", fontSize = 1.0)

p.gridText(1,0,r"""


John A Wheeler
 
*In any field, find the strangest thing and then 
explore it.* 


J Gleick, *Genius: the Life and Science of Richard Feynman* (1993)

""", fontSize = 1.0)



p.gridImage(1,1,"./QIC_Figures/QIC10_wheeler_1.jpg", height = 100)


########################################
p.newSlide()
p.title("**Delayed-choice quantum eraser: Can we erase the past?**")

p.leftImage("./QIC_Figures/QIC10_Science_cover.jpg", height=400)

p.rightImage("./QIC_Figures/QIC10_Science_307_875_2005.png", height=400)


########################################
p.newSlide()
p.title("**Wheeler's delayed-choice experiment**")

p.leftText(r"""

Test of complementarity

* We measure wave-like or particle-like properties but not both at the same time.

* In an interferometer, either which-way or interence, not both.

""", fontSize = 1.0)

p.rightImage("./QIC_Figures/interferometer_eraser_2.png", height=600)


########################################
p.newSlide()
p.title("**Wheeler's delayed-choice experiment**")

p.leftText(r"""

Test of complementarity

* We measure wave-like or particle-like properties but not both at the same time.

* In an interferometer, either which-way or interence, not both.

""", fontSize = 1.0)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################################
p.newSlide()
p.title("**Wheeler's delayed-choice experiment**")
p.spanCenterImage("./QIC_Figures/QIC10_delayed_choice_expt_1.png", height = 400, textBelow=r"""https://www.science.org/doi/abs/10.1126/science.1136303 Jacques et al, Science 315, 966 (2007)""", fontSize = 0.5)


########################################
p.newSlide()
p.title("**Delayed-choice quantum eraser**")
p.makeGrid(4,4)
p.gridText(0,3,r"""

Decoherence: Information leaks from our **S**ystem to the **E**nvironment, encoding which-path information about **S** in **E**, and thereby destroys the interference pattern.

Idea.


* Make measurement on **E** to erase which-path information and recover the interference fringes.

* Delayed-choice: erase which-path information after interference has taken place.

""", fontSize = 0.5)
p.gridImage(1,3,"./QIC_Figures/QIC10_delayed_choice_quantum_eraser_circuit.png", height = 100)

########################################
p.newSlide()
p.title("**Delayed-choice quantum eraser**")
p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC10_delayed_choice_quantum_eraser_circuit.png", height = 100)


########################################
p.newSlide()
p.title("QIC.10 Summary")
p.leftText(r"""
** QIC.10 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Construct a quantum circuit to model the interaction between a quantum system and the external world.
* Calculate the state vector after each layer of the circuit.
* Interpret the results in term of which-path information and complementarity. 
* Use the quantum circuit model to analyse the delayed-choice quantum eraser. 


""", fontSize = 1.0)

########################################
p.save("./QIC_10.html")

