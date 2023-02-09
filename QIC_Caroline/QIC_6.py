from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_6_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("QIC.6: Ph 30, 14.00 Thursday Jan 27, 2022")
p.makeGrid(4,4)
p.gridText(0,0,r"""

** QIC.5 Summary **

""", fontSize = 1.0)

p.gridText(0,1,r"""

**Single-qubit gates (DVC2)**

""", fontSize = 1.0)

p.gridText(1,1,r"""

Rabi oscillations

$\rightarrow$ $\pi/2$, $\pi$, $2\pi$ pulses.

""", fontSize = 0.5)

p.gridImage(1,2,"./QIC_Figures/QIC5_pi_over_2.png", height = 150, textBelow = r""" """, fontSize = 0.5)

p.gridText(2,1,r"""

Hadamard gate

""", fontSize = 0.5)

p.gridImage(2,2,"./QIC_Figures/BlochDM_Hxz.png", height = 150)

p.gridImage(2,3,"./QIC_Figures/QIC5_Sr_Rabi_oscillation_1.png", height = 100)

########################################
p.newSlide()
p.title("**QIC.6: Outline**")
p.makeGrid(3,3)
p.gridText(0,0,r"""

**Low Decoherence (DVC4)**

""", fontSize = 1.0)

p.gridText(1,0,r"""

* Build **decay** and **decoherence** into qubit model.

* T1/T2 times

* Optical Bloch equations

""", fontSize = 0.5)

p.gridText(1,1,r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}
""", fontSize = 0.5)

p.gridImage(1,2,"./QIC_Figures/BlochDM_T2.png", height = 200)

p.gridImage(0,2,"./QIC_Figures/QIC6_intro.png", height = 200)

########################################
p.newSlide()
p.title(r"""**Decay and decoherence: $T_1$ and $T_2$**""")


########################################
p.newSlide()
p.title(r"""**Optical Bloch equations**""")

########################################
p.newSlide()
p.title(r"""**Optical Bloch equations**""")

########################################
p.newSlide()
p.title(r"""**OBE: analytic example**""")

########################################
p.newSlide()
p.title(r"""**Decoherence**""")

p.leftText(r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}

No driving, $\Omega = 0$.

Detuning, $\Delta \neq 0$

Initial state $\vert +\rangle = \textstyle{1\over\sqrt{2}}(\vert 0\rangle +\vert 1\rangle)$

Transition from 

$T2 > T1$ ($T_2 = 2T_1$ decay only) 

to 

$T2 \ll T1$ ($T_2 = 2T_1/21$ decohernce dominates)

\begin{eqnarray} 
\frac{1}{T_2} = \frac{1}{2T_1} + \Gamma_2
\end{eqnarray}


\begin{eqnarray} 
\Gamma_2 = [0, 2.5, 5, 7.5, 10]/T_1
\end{eqnarray}

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_T2.html", height=800)


########################################
p.newSlide()
p.title(r"""**$T_1$ and $T_2$ times**""")

p.leftText(r"""

How to measure $T_2$?

See QIC.7

""", fontSize = 0.5)

p.rightImage("./QIC_Figures/QIC6_superconducting_T1_T2.png", height=400)




########################################
p.newSlide()
p.title(r"""**OBE: transition to steady-state**""")

p.leftText(r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}

$t \gg 1/Omega,~1\Delta$
""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM6_initial_to_steady_state.html", height=800)

########################################
p.newSlide()
p.title(r"""**OBE: transition to steady-state**""")

p.leftText(r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}

""", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/QJump_interactive.html", height=800)

########################################
p.newSlide()
p.title(r"""**OBE steady state**""")

p.leftText(r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}

""", fontSize = 0.5)

p.rightImage("./QIC_Figures/QJump.png", height=400)

########################################
p.newSlide()
p.title(r"""**OBE steady-state**""")
p.leftText(r"""

\begin{eqnarray} 
\dot{u}&=&-\frac{u}{T_2}-\Delta v~,\\\
\dot{v}&=&\Delta u-\frac{v}{T_2}-\Omega w~,\\\
\dot{w}&=&\Omega v-\frac{1}{T_1}\left(w-1 \right)~.
\end{eqnarray}

""", fontSize = 0.5)

p.rightImage("./QIC_Figures/rabi_ss_1.png", height=400)

########################################
p.newSlide()
p.title("**OBE steady-state**")
p.makeGrid(4,4)
p.gridText(0,0,r"""

""", fontSize = 1.0)

p.gridImage(0,3,"./QIC_Figures/rabi_ss_1.png", height = 100, textBelow = r""" """, fontSize = 0.5)

########################################
p.newSlide()
p.title("QIC.6 Summary")
p.leftText(r"""
** QIC.6 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""


* Identify the terms in the optical Bloch equations.

* Explain, the distinction between $T_1$ and $T_2$.

* Sketch and describe the dynamics of the Bloch vector in the case of decay or decoherence. 

* Explain whether the steady-state predicted by the optical Bloch equations is Markovian or non-Markovian. 

""", fontSize = 1.0)

########################################
p.save("./QIC_6.html")

