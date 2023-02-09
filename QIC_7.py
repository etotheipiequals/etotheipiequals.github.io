from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_7_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("QIC.7: Quantum interference and measurement")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.6 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

**Low decoherence (DVC4)**

""", fontSize = 1.0)

p.gridText(1,1,r"""

* Build **decay** and **decoherence** into qubit model.

* T1/T2 times

* Optical Bloch equations

""", fontSize = 0.5)

p.gridText(2,1,r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}

""", fontSize = 0.5)

p.gridImage(2,2,"./QIC_Figures/BlochDM_T2.png", height = 150)

########################################
p.newSlide()
p.title("**QIC.7: Quantum interference**")
p.makeGrid(3,3)
p.gridText(0,0,r"""

**Outline**

""", fontSize = 1.0)

p.gridText(1,0,r"""

* How to measure coherence?

* A **quantum** (**Ramsey**) interferometer

* What is it?

""", fontSize = 0.5)

p.gridImage(1,1,"./QIC_Figures/QIC7_Ramsey_0.png", height = 200)

p.gridImage(1,2,"./Figures/Ramsey_static.png", height = 200)

########################################
p.newSlide()
p.title(r"""**DVC3: Measurement/Read-out**""")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC7_projection.png", height = 150)

########################################
p.newSlide()
p.title(r"""**Measuring coherence**""")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC7_circuit_H_measure.png", height = 150)

p.gridImage(2,3,"./QIC_Figures/QIC7_rho_H_measure.png", height = 150)

########################################
p.newSlide()
p.title(r"""**Measuring coherence**""")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC7_circuit_H_measure.png", height = 150)

p.gridImage(2,3,"./QIC_Figures/QIC7_rho_H_measure.png", height = 150)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometer**""")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC7_Ramsey_2.png", height = 150)
p.gridImage(1,3,"./QIC_Figures/QIC7_Ramsey_1.png", height = 150)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometer**""")

p.makeGrid(4,4)

p.gridImage(0,1,"./QIC_Figures/QIC7_Ramsey_circuit_1.png", height = 150)

p.gridImage(1,1,"./QIC_Figures/QIC7_Ramsey_time.png", height = 150)

p.gridImage(2,1,"./QIC_Figures/QIC7_Ramsey_5.png", height = 150)

p.gridImage(2,2,"./QIC_Figures/QIC7_Ramsey_6.png", height = 150)

p.gridImage(2,0,"./QIC_Figures/QIC7_Ramsey_4.png", height = 150)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometer**""")


p.spanCenterImage("./QIC_Figures/QIC7_Ramsey_clocks.png", height=400)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometer**""")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC7_Ramsey_1.png", height = 150)


########################################
p.newSlide()
p.title(r"""**Ramsey interferometer**""")

p.leftText(r"""

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Ramsey_2_interactive.html", height=800)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometer**""")

p.leftText(r"""

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/Ramsey_interactive.html", height=800)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometer: decoherence**""")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC7_Ramsey_2.png", height = 150)
p.gridImage(1,3,"./QIC_Figures/QIC7_Ramsey_1.png", height = 150)

p.gridImage(2,3,"./QIC_Figures/QIC7_Ramsey_3.png", height = 150)

########################################
p.newSlide()
p.title(r"""**Ramsey interferometry: measuring $T_1$ and $T_2$**""")

p.makeGrid(2,2)

p.gridImage(0,0,"./QIC_Figures/QIC7_Sr_tweezer_0.png", height = 300)
p.gridImage(0,1,"./QIC_Figures/QIC7_Sr_tweezer_1.png", height = 300)

########################################
p.newSlide()
p.title("QIC.7 Summary")
p.leftText(r"""
** QIC.7 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Explain the principle of the Ramsey interferometer.

* Derive the probabilities to be in the $\vert 0\rangle$ or $\vert 1\rangle$ at the output for different pulses sequences ($\pi/2$ pulses with different phase and Hadamards).
 
* Sketch the evolution on the Bloch sphere.


""", fontSize = 1.0)

########################################
p.save("./QIC_7.html")

