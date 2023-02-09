from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_eraser.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black


########################################
p.newSlide()
p.title("Not a quantum eraser?")

p.leftText(r"""

**What is a quantum eraser?**

* When a quantum system (S) interacts with the external world (E) some information is lost (from S to E).
* The system and external world become **entangled**.
* The effect of this entanglement is that when we try the wave fucntion describing S we find that it no longer has a well-defined phase. 
* This phase fuzziness is known as **decoherence**.
* This decoherence is measured using **interference**.
* The idea of the quantum eraser is that if we can delete the information in E, we can restore the coherence and the interference.

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################################
p.newSlide()
p.title("Not a quantum eraser?")

p.leftText(r"""

**A simple example**

* Consider the example of light - made of photons.
* The wave for each photon is split into two paths and then recombined.
* If we cannot tell which path the photon followed we see interference.
* If we can tell we don't.

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################################
p.newSlide()
p.title("Not a quantum eraser/")

p.leftText(r"""

**Complementarity**

* The link between 'which-path' information and interferece is illustrated in the figure.
* We use polarization to label the paths. 
* The two paths are horizontally (H) and vertically (V) polarized.
* **Complementarity** tells us that if we know 'which path' the particle follows then we cannot see the wave-like property - interference.
* But if can erase the path information then we can recover the inteference pattern.

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################################
p.newSlide()
p.title("Not a quantum eraser?")

p.leftText(r"""

**Simulation (left image)**

* The light intensity. The light propagates from top to bottom.
* We place a linear polarizer in the plane where the paths overlap.
* Now use the polarizer angle slider.
* When the polazier is horizontal the beam with horizontal polarization (H) is tramsmitted. 
* When the polazier is vertical the beam with vertical polarization (H) is tramsmitted. 
* When the polarizer is at $\pm 45^\circ$  both (50$\%$ thereof) are transmitted.
* For $\pm 45^\circ$ we no longer distinguish between H and V. As we have erased the path information, the interference pattern is recovered.

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################################
p.newSlide()
p.title("Not a quantum eraser?")

p.leftText(r"""

**Simulation (right image)**

* In addition to intensity patterns (left image) we can also look at the light field (right image).
* We detect the field at a point indicated by the white square in the left image.
* The field oscillates in time - horizontally for H and vertically V.
* The total field at different times are indicated by the blue dots.
* Now change the detector position using the position slider. 
* When we add together the two field we can get fields that oscillate along axis at $\pm 45^\circ$ or around in a circle - circular polarization.
* The component of the field that makes it through the polarizer is shown in red.
* As we move the position of the detector we learn how the amplitude of the field and hence the intensity vary with position.

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################################
p.newSlide()
p.title("Not a quantum eraser?")

p.leftText(r"""

**So is this a quantum eraser?**

* By choosing the polarizer angle at $\pm 45^\circ$ we erase the which-path information and recover the interference pattern.
* It has been called *single-photon quantum erasing* in this reference

https://iopscience.iop.org/article/10.1088/0143-0807/31/3/020


* But, there are some missing ingredients.
* There is no external world (no E).
* No decoherence.
* No entanglement.



""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)


########################################
p.newSlide()
p.title("Not the Quanum Eraser?")
p.leftText(r"""

** Summary ** 

* A quantum eraser needs a quantum system (like a photon) and an environment.
* The simplest environment we can envisage is another quantum particle.
* So we need at least two photons, as in this reference.

https://journals.aps.org/pra/abstract/10.1103/PhysRevA.45.7729


 

""", fontSize = 1.0)

p.rightIFrame("./QIC_Figures/Quantum_Erasure.html", height=800)

########################## SAVE
p.save("./QIC_eraser.html")

