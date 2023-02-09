from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_14_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
p.newSlide()
p.title("QIC.14: Loading and state preparation of atom arrays (DVC1)")
p.leftText(r"""

** QIC.13 Summary **


**Optical tweezers**


* Trap depth $U_0$: How does it depend on laser power, beam size, wavelength?


* Trap freq: $\omega_{\rm rad}$, $\omega_{\rm ax}$.

* Scattering rate $R_{\rm spont} = \Gamma P_{\vert {\rm e}\rangle}$, 


* OBE steady state, $\vert \Delta\vert \gg \Omega \gg \Gamma$, $P_{\vert {\rm e}\rangle}=\Omega^2/2\vert \Delta\vert^2$


""", fontSize = 0.5)


p.rightImage("./QIC_Figures/QIC13_tweezer_static.png", height = 600)



########################################
p.newSlide()
p.title("QIC.14: Outline")

p.makeGrid(3,3)


p.gridText(0,0,r"""

DVC1: Initialisation of an atom array

* Optical tweezers [QIC.13] create array potential.

* Now we need to load traps with atoms 

* To load: **laser slowing** and laser cooling - spontaneous force

* To initial in qubit state: **optical pumping**


""", fontSize = 0.5)

p.gridImage(0,1,"./QIC_Figures/QIC7_Sr_tweezer_0.png", height = 240)

p.gridText(1,0,r"""

* Alkali (Rb, Cs) different to alkaline-earths (Sr)

* Different states used for slowing (Sr: $^1$S$_0$ and $^1$P$_1$), cooling, qubit (Sr: $^1$S$_0$ and $^3$P$_0$).


""", fontSize = 0.5)


p.gridImage(1,1,"./QIC_Figures/QIC11_Cs_energy_levels_4.png", height = 150)


p.gridImage(1,2,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 120)

########################################
p.newSlide()
p.title("QIC.14: Slowing hot atoms to rest")

p.makeGrid(2,2)


p.gridText(0,0,r"""

DVC1: Initialisation of an atom array

* Room $T$ atoms. A few hundred metres per second.

* Laser slowing and laser cooling - spontaneous force


""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC14_zeeman_slower_1.png", height = 150)

p.gridImage(1,1,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 150)


########################################
p.newSlide()
p.title("Worked example: 2021 Exam Q.3(d)")
p.makeGrid(4,4)
p.gridImage(0,3,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 150)
p.gridText(1,3,r"""

(i) In some atom quantum computers, it is necessary to slow an atomic beam using a counter-propagating laser. Write an equation for the minimum stopping distance in terms of the mass, $m$, and initial speed, $v$, of the atoms, the lifetime of the excited state, $\tau$, and the laser wavelength $\lambda$. [2 marks]

(ii) Discuss  the feasibility of slowing $^{88}$Sr atoms emitted by an oven at $T=10^3$ K using light with $\lambda=689\; $nm resonant with the intercombination line $^1{\rm S}_0\rightarrow ^3$P$_1$. The $^3{\rm P}_1$ has a lifetime $\tau=21.5 \; \mu$s.
[2 marks]

(iii) By what factor is the stopping distance reduced if we switch to the $^1{\rm S}_0\rightarrow ^1$P$_1$ transition, with $\lambda=461\; $nm and $\tau=5.27\; $ns? [1 mark]

""", fontSize = 0.5)

########################################
p.newSlide()
p.title("Worked example: 2021 Exam Q.3(d)")
p.makeGrid(4,4)
p.gridImage(0,3,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 150)
p.gridText(1,3,r"""

(i) In some atom quantum computers, it is necessary to slow an atomic beam using a counter-propagating laser. Write an equation for the minimum stopping distance in terms of the mass, $m$, and initial speed, $v$, of the atoms, the lifetime of the excited state, $\tau$, and the laser wavelength $\lambda$. [2 marks]

(ii) Discuss  the feasibility of slowing $^{88}$Sr atoms emitted by an oven at $T=10^3$ K using light with $\lambda=689$~nm resonant with the intercombination line $^1{\rm S}_0\rightarrow ^3$P$_1$. The $^3{\rm P}_1$ has a lifetime $\tau=21.5\;\mu$s.
[2 marks]

(iii) By what factor is the stopping distance reduced if we switch to the $^1{\rm S}_0\rightarrow ^1$P$_1$ transition, with $\lambda=461\;$nm and $\tau=5.27\;$ns? [1 mark]

""", fontSize = 0.5)

p.gridImage(2,1,"./QIC_Figures/Sr_MOT.jpg", height = 150, textBelow = r"""Matthew Hill PhD, Durham""", fontSize = 0.5)


'''


########################################
p.newSlide()
p.title("QIC.14: Laser cooling inside a trap - sideband cooling")

p.makeGrid(3,3)


p.gridText(0,0,r"""

DVC1: Initialisation of an atom array

* Laser cooling to the vibrational ground state of the tweezer

""", fontSize = 0.5)


p.gridImage(0,2,"./QIC_Figures/QIC14_sideband_cooling.png", height = 150)

p.gridImage(1,2,"./QIC_Figures/QIC14_Sr_sideband_2018.png", height = 240, textBelow = r"""https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.041054""", fontSize = 0.25)


########################################
p.newSlide()
p.title("Worked example: Well-resolved sideband regime")

p.makeGrid(4,4)

p.gridText(0,3,r"""

DU has decided to build a Sr atom quantum computer. They build a tweezer array using a laser at the *magic* wavelength, $\lambda=813$~nm, such that the trapping potentials for the $\vert 0\rangle=\vert ^1{\rm S}_1\rangle$ and $\vert 1\rangle=\vert ^3{\rm P}_0\rangle$ qubit states are identical. Easy tweezer has a laser power $P=1$~mW, and spot spot $w_0=1\;\mu$m. 

(i) Write an expression for the trap depth, $U_0$ in terms of $P$, $w_0$, the laser detuning, $\Delta$, and the decay rate $\Gamma$.
Verify that your formula has the correct dimensions. 

(ii) Estimate whether they are in the well-resolved sideband regime. 

[Hints: The trap depth is $U=\hbar \Omega^2/4\Delta$, where $\Omega^2=\Gamma^2 I/2I_{\rm s}$ and $I_{\rm s}=(\pi/3)(hc\Gamma/\lambda_0^2)$. The $^1P_1$ and $^3P_1$ states have decay rates, $\Gamma_{\rm 461}=2\pi\;(30.2\;{\rm MHz})$ and $\Gamma_{\rm 689}=2\pi\;(7.4\;{\rm kHz})$, where the subscript indicate the wavelength $\lambda_0$ in nanometers.]


""", fontSize = 0.5)


########################################
p.newSlide()
p.title(r"""**Sr atom array: Cool in a deeper 515 nm tweezer**""")

p.makeGrid(3,3)

p.gridImage(0,2,"./QIC_Figures/QIC14_Sr_515_lattice.png", height = 240)

p.gridImage(1,2,"./QIC_Figures/QIC14_Sr_sideband_2018.png", height = 240, textBelow = r"""https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.041054""", fontSize = 0.25)

########################################
p.newSlide()
p.title(r"""**Sr atom quantum computer?**""")

p.makeGrid(3,3)

p.gridText(0,0,
r"""

$\bbox[5px, border: 2px solid orange]{\rm DVC1: Initialisation}$

$\bbox[5px, border: 2px solid gray]{\rm DVC2: Gates}$ 
$\bbox[5px, border: 2px solid orange]{\rm Single-qubit}$ 
$\bbox[5px, border: 2px solid red]{\rm Two-qubit}$


$\bbox[5px, border: 2px solid orange]{\rm DVC3: Read out}$

$\bbox[5px, border: 2px solid lime]{\rm DVC4: Decoherence}$

$\bbox[5px, border: 2px solid gray]{\rm DVC5: Scaling}$


""", fontSize = 0.5)


p.gridImage(0,1,"./QIC_Figures/QIC7_Sr_tweezer_0.png", height = 100)
p.gridImage(0,2,"./QIC_Figures/QIC7_Sr_tweezer_1.png", height = 100)

p.gridText(2,0,r"""

$^1S_0\rightarrow ^3P_0$, $\Gamma_{\rm 698}=2\pi(1~{\rm mHz})$

$$\Omega^2 =\frac{3\Gamma\lambda_0^2}{2\pi hc}{\cal I} $$

""", fontSize = 0.5)


p.gridImage(2,1,"./QIC_Figures/QIC14_Sr_energy_levels.png", height = 100)


*  Explain the principle of sideband cooling. 
* Given input parameters such as laser wavelengths, powers and beam sizes, be able to estimate whether the condition for sideband cooling is satified. 



'''


########################################
p.newSlide()
p.title("QIC.14 Rb, Cs atom array initialisation")

p.makeGrid(2,2)


p.gridText(0,0,r"""

Rb, Cs atom array initialisation

""", fontSize = 1.0)

p.gridImage(0,1,"./QIC_Figures/QIC11_Cs_energy_levels_4.png", height = 150)


p.gridText(1,0,r"""

* Optical pumping

* Polarization selection rules


""", fontSize = 0.5)


p.gridImage(1,1,"./QIC_Figures/QIC15_optical_pumping_1.png", height = 150)


########################################
p.newSlide()
p.title("Alkali atom: States ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC15_optical_pumping_1.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC15_optical_pumping_2.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Selection rules ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC11_Cs_energy_levels_3.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Polarization selection rules ")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/H1s2p.jpg", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/H1s2p_lin.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(2,3,"./QIC_Figures/H1s2p_circ.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Polarization selection rules ")

p.makeGrid(4,4)


p.gridImage(2,3,"./QIC_Figures/QIC15_MOT_bad.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title("Optical pumping I")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC15_Kastler.png", height = 100, textBelow="", fontSize = 0.5)

p.gridImage(1,3,"./QIC_Figures/QIC15_optical_pumping_3.png", height = 100, textBelow="", fontSize = 0.5)

########################################
p.newSlide()
p.title("Optical pumping II")

p.makeGrid(4,4)

p.gridImage(0,3,"./QIC_Figures/QIC15_optical_pumping_4.png", height = 100, textBelow="", fontSize = 0.5)


########################################
p.newSlide()
p.title(r"""**Atom quantum computer: DVC**""")

p.makeGrid(2,2)

p.gridText(0,0,
r"""

$\bbox[5px, border: 2px solid orange]{\rm DVC1: Initialisation}$

$\bbox[5px, border: 2px solid gray]{\rm DVC2: Gates}$ 
$\bbox[5px, border: 2px solid red]{\rm Single-qubit}$ QIC.15 
$\bbox[5px, border: 2px solid red]{\rm Two-qubit}$ QIC.16-18

$\bbox[5px, border: 2px solid orange]{\rm DVC3: Read out}$

$\bbox[5px, border: 2px solid lime]{\rm DVC4: Decoherence}$

$\bbox[5px, border: 2px solid gray]{\rm DVC5: Scaling}$


""", fontSize = 0.5)


p.gridImage(0,1,"./QIC_Figures/QIC16_readout_1.png", height = 100)
p.gridImage(1,1,"./QIC_Figures/QIC16_readout_3.png", height = 100)


########################################
p.newSlide()
p.title("QIC.14 Summary")
p.leftText(r"""
** QIC.14 Notes ** 

Summary 

""", fontSize = 1.0)

p.rightText(r"""

* Understanding the significant of $\Gamma$ in the context of stopping and cooling atoms.
* Be able to calculate the stopping distance.
* Explain why labeling a laser beam $\sigma_-$, $\pi$, or $\sigma_+$ does not make sense.
* Work out what configuration of laser beam polarizations and propagation directions are needed to drive particular transitions and hence optically pump atoms into a particular state.
* Sketch optical pumping diagrams for different cases.

""", fontSize = 1.0)

########################## SAVE
p.save("./QIC_14.html")

