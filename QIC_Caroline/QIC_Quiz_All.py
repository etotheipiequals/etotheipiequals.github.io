from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_Quiz_2_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz 2 **")

p.makeGrid(3,3)

p.gridImage(0,1,"./QIC_Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./QIC_Figures/time.mp3")


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(d)
    questionImage="./Figures/deBroglie.jpg",
    questionText="##Are you a wave or a particle?",
    answersText=[
        r"Yes, I am a wave.",
        r"Yes, I am a particle.",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC1_moores_law_2.png",
    questionText=r"$1.$ Moore's law is a straight line if you plot it with appropriate axis scales. What scaling should you use? [1 mark]",
    answersText=[
        r"$({\rm a})$ Standard lin-lin plot.",
        r"$({\rm b})$ Semi-log $x$.",
        r"$({\rm c})$ Semi-log $y$.",
        r"$({\rm d})$ Log-log plot.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC1_moores_law_2.png",
    questionText=r"$1.$ Moore's law is a straight line if you plot it with appropriate axis scales. What scaling should you use? $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ Standard lin-lin plot.",
        r"$({\rm b})$ Semi-log $x$.",
        r"$({\rm c})$ Semi-log $y$. $[{\rm YES}]$  ",
        r"$({\rm d})$ Log-log plot.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) and (e)
    questionImage="./QIC_Figures/QIC9_GHZ.png",
    questionText=r"$2.$ Which of the following is applicable to a classical NAND gate? [2 marks]",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\Delta U & = & 0 \end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Delta U & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Delta U & = & k_{\rm B}T \ln 2 \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Delta S & = & 0 \end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Delta S & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Delta S & = & k_{\rm B}T\ln 2 \end{eqnarray}",
     ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) and (e)
    questionImage="./QIC_Figures/QIC9_GHZ.png",
    questionText=r"$2.$ Which of the following is applicable to a classical NAND gate? $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\Delta U & = & 0 \end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Delta U & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Delta U & = & k_{\rm B}T \ln 2 \end{eqnarray} $[{\rm YES}]$",
        r"$({\rm d})$ \begin{eqnarray}\Delta S & = & 0 \end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Delta S & = & k_{\rm B}\ln 2 \end{eqnarray} $[{\rm YES}]$",
        r"$({\rm f})$ \begin{eqnarray}\Delta S & = & k_{\rm B}T\ln 2 \end{eqnarray}",
     ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (a) and (d)
    questionImage="./QIC_Figures/QIC9_GHZ.png",
    questionText=r"$3.$ Which of the following is applicable to a quantum two-qubit gate?  [2 marks]",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\Delta U & = & 0 \end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Delta U & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Delta U & = & k_{\rm B}T \ln 2 \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Delta S & = & 0 \end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Delta S & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Delta S & = & k_{\rm B}T\ln 2 \end{eqnarray}",
     ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (a) and (d)
    questionImage="./QIC_Figures/QIC9_GHZ.png",
    questionText=r"$3.$ Which of the following is applicable to a quantum two-qubit gate?  $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\Delta U & = & 0 \end{eqnarray} $[{\rm YES}]$",
        r"$({\rm b})$ \begin{eqnarray}\Delta U & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Delta U & = & k_{\rm B}T \ln 2 \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Delta S & = & 0 \end{eqnarray} $[{\rm YES}]$",
        r"$({\rm e})$ \begin{eqnarray}\Delta S & = & k_{\rm B}\ln 2 \end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Delta S & = & k_{\rm B}T\ln 2 \end{eqnarray}",
     ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b)
    questionImage="./QIC_Figures/QIC1_superconducting_3.png",
    questionText=r"$4.$ An advantage of using superconductors or semiconductors for quantum computing is:  [1 mark]",
    answersText=[
        r"$({\rm a})$ They work at room T.",
        r"$({\rm b})$ The qubits are fixed in position.",
        r"$({\rm c})$ The qubits do not interact with their environment.",
        r"$({\rm d})$ The qubits are all identical.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b)
    questionImage="./QIC_Figures/QIC1_superconducting_3.png",
    questionText=r"$4.$ An advantage of using superconductors or semiconductors for quantum computing is: $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ They work at room T.",
        r"$({\rm b})$ The qubits are fixed in position. $[{\rm YES}]$",
        r"$({\rm c})$ The qubits do not interact with their environment.",
        r"$({\rm d})$ The qubits are all identical.",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(d)
    questionImage="./QIC_Figures/QIC14_Sr_515_lattice.png",
    questionText=r"$5.$ An advantage of using atoms or ions for quantum computing is:  [1 mark]",
    answersText=[
        r"$({\rm a})$ They work at room T.",
        r"$({\rm b})$ The qubits are fixed in position.",
        r"$({\rm c})$ The qubits do not interact with their environment.",
        r"$({\rm d})$ The qubits are all identical.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(d)
    questionImage="./QIC_Figures/QIC14_Sr_515_lattice.png",
    questionText=r"$5.$ An advantage of using atoms or ions for quantum computing is: $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ They work at room T.",
        r"$({\rm b})$ The qubits are fixed in position.",
        r"$({\rm c})$ The qubits do not interact with their environment.",
        r"$({\rm d})$ The qubits are all identical. $[{\rm YES}]$",
    ],
)

#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b) and (e)
    questionImage="./QIC_Figures/QIC2_DiVincenzo_1.png",
    questionText=r"$6.$ Which of the DiVincenzo criteria can't we test (fully) with a single qubit?  [2 marks]",
    answersText=[
        r"$({\rm a})$ Initialisation.",
        r"$({\rm b})$ Gates.",
        r"$({\rm c})$ Read-out.",
        r"$({\rm d})$ Decoherence.",
        r"$({\rm e})$ Scalability.",
    ],
)

#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b) and (e)
    questionImage="./QIC_Figures/QIC2_DiVincenzo_1.png",
    questionText=r"$6.$ Which of the DiVincenzo criteria can't we test (fully) with a single qubit? $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ Initialisation.",
        r"$({\rm b})$ Gates. $[{\rm YES}]$ e.g. two-qubit gates.",
        r"$({\rm c})$ Read-out.",
        r"$({\rm d})$ Decoherence.",
        r"$({\rm e})$ Scalability. $[{\rm YES}]$ needs more than one qubit.",
    ],
)

#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(a) and (d)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$7.$ Which of the following are true? $[2~{\rm marks}]$",
    answersText=[
        r"$({\rm a})$ A Bloch vector in the $xz$ plane is purely real.",
        r"$({\rm b})$ A Bloch vector in the $yz$ plane is purely imaginary.",
        r"$({\rm c})$ A Bloch vector in the $xy$ plane is always complex.",
        r"$({\rm d})$ A Bloch vector with a $y$ component is always complex.",
    ],
)

#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(a) and (d)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$7.$ Which of the following are true? $[{\rm SOLUTION}]$",
    answersText=[
        r"$({\rm a})$ A Bloch vector in the $xz$ plane is purely real. $[{\rm TRUE}]$",
        r"$({\rm b})$ A Bloch vector in the $yz$ plane is purely imaginary. $[{\rm FALSE}]$ only a Bloch vector along $y$ axis is purely imaginary.",
        r"$({\rm c})$ A Bloch vector in the $xy$ plane is always complex. $[{\rm FALSE}]$ because it could be along $x$ and real. ",
        r"$({\rm d})$ A Bloch vector with a $y$ component is always complex. $[{\rm TRUE}]$",
    ],
)

#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(a) and (c)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$8.$ Which of the following CANNOT be represented using a Bloch sphere?  [2 marks]",
    answersText=[
        r"$({\rm a})$ A harmonic oscillator.",
        r"$({\rm b})$ Photon polarization.",
        r"$({\rm c})$ Quantum entanglement.",
        r"$({\rm d})$ Decoherence.",
        r"$({\rm e})$ Any two-level system.",
        r"$({\rm f})$ An electron spin.",
    ],
)

#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(a) and (c)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",fontSize=0.5,
    questionText=r"$8.$ Which of the following CANNOT be represented using a Bloch sphere?  $[{\rm SOLUTION}]:$",
    answersText=[
        r"$({\rm a})$  A harmonic oscillator. $[{\rm CORRECT}]$ because there are more than two levels.",
        r"$({\rm b})$ Photon polarization.",
        r"$({\rm c})$ Quantum entanglement. $[{\rm CORRECT}]$ needs more than one qubit which cannot be represented separately. ",
        r"$({\rm d})$ Decoherence.",
        r"$({\rm e})$ Any two-level system.",
        r"$({\rm f})$ An electron spin.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$9.$ Which of the following are possible qubit states?  $[4~{\rm marks}]$",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle & = &  \frac{1}{\sqrt{5}}\left(\begin{array}{c} 2  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\vert \psi \rangle & = &\frac{1}{\sqrt{3}}\left(\begin{array}{c} 1  \\\ \sqrt{2}{\rm e}^{{\rm i}\phi} \end{array}\right)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\vert \psi \rangle & = &\frac{1}{\sqrt{2}} \left(\begin{array}{c} {\rm e}^{{\rm i}\phi}  \\\ {\rm e}^{{\rm i}\phi} \end{array}\right)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\vert \psi \rangle & = & \left(\begin{array}{c} \sin\alpha  \\\ \cos\alpha \end{array}\right)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \sqrt{1/2 -\alpha} \\\ \sqrt{1/2 +\alpha^*} \end{array}\right)\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \tan\alpha  \\\ 1 \end{array}\right)\end{eqnarray}",
     ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",fontSize=0.5,
    questionText=r"$9.$ Which of the following are possible qubit states?  $[{\rm SOLUTION}]:$ Check is $\vert a\vert ^2 + \vert b\vert^2 =1$.",
    answersText=[
        r"$({\rm a})$ $[{\rm YES}]$ \begin{eqnarray}\vert \psi \rangle & = &  \frac{1}{\sqrt{5}}\left(\begin{array}{c} 2  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"$({\rm b})$ $[{\rm YES}]$ \begin{eqnarray}\vert \psi \rangle & = &\frac{1}{\sqrt{3}}\left(\begin{array}{c} 1  \\\ \sqrt{2}{\rm e}^{{\rm i}\phi} \end{array}\right)\end{eqnarray}",
        r"$({\rm c})$ $[{\rm YES}]$ \begin{eqnarray}\vert \psi \rangle & = &\frac{1}{\sqrt{2}} \left(\begin{array}{c} {\rm e}^{{\rm i}\phi}  \\\ {\rm e}^{{\rm i}\phi} \end{array}\right)\end{eqnarray}",
        r"$({\rm d})$ $[{\rm YES}]$ \begin{eqnarray}\vert \psi \rangle & = & \left(\begin{array}{c} \sin\alpha  \\\ \cos\alpha \end{array}\right)\end{eqnarray}",
        r"$({\rm e})$ $[{\rm NO}]$    \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \sqrt{1/2 -\alpha} \\\ \sqrt{1/2 +\alpha^*} \end{array}\right)\end{eqnarray}   \begin{eqnarray}\vert a\vert ^2 + \vert b\vert^2 & = &1/2 + 2\vert \alpha\vert^2 \end{eqnarray}",
        r"$({\rm f})$ $[{\rm NO}]$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \tan\alpha  \\\ 1 \end{array}\right)\end{eqnarray}",
     ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$10.$ In the Bloch sphere representation, which of the following state vectors lie in the $yz$ plane?  [3 marks]",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} 0  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} -{\rm i}  \\\ {\rm i} \end{array}\right)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \cos\textstyle{\theta\over 2}  \\\ {\rm e}^{{\rm i}\pi/2}\sin\textstyle{\theta\over 2} \end{array}\right)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}} \left(\begin{array}{c} -{\rm i}  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{-{\rm i}3\pi/8} \end{array}\right)\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{{\rm i}3\pi/8} \end{array}\right)\end{eqnarray}",
     ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",fontSize=0.5,
    questionText=r"$10.$ In the Bloch sphere representation, which of the following state vectors lie in the $yz$ plane?  $[{\rm SOLUTION}]:$ Check if relative phase $\phi =\pm \pi/2$",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} 0  \\\ 1 \end{array}\right)\end{eqnarray} $[{\rm YES}]$ but in this case relative phase is undefined.",
        r"$({\rm b})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} -{\rm i}  \\\ {\rm i} \end{array}\right)\end{eqnarray} $[{\rm NO}]$",
        r"$({\rm c})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \cos\textstyle{\theta\over 2}  \\\ {\rm e}^{{\rm i}\pi/2}\sin\textstyle{\theta\over 2} \end{array}\right)\end{eqnarray} $[{\rm YES}]$",
        r"$({\rm d})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}} \left(\begin{array}{c} -{\rm i}  \\\ 1 \end{array}\right)\end{eqnarray} $[{\rm YES}]$",
        r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{-{\rm i}3\pi/8} \end{array}\right)\end{eqnarray} $[{\rm YES}]$",
        r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{{\rm i}3\pi/8} \end{array}\right)\end{eqnarray} $[{\rm NO}]$",
     ],
)



########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (c) and (f)
    questionText=r"$11.$ For the qutrit state vector, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle +c\vert 2\rangle$, which of the following are true?    [2 marks]      [Hint: $m\times n$, $m$ rows $\times$ $n$ columns.]",
    answersText=[r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle * \vert \psi \rangle \end{eqnarray} is a $6\times1$ matrix. ",
                 r"$({\rm b})$ \begin{eqnarray} \langle  \psi \vert * \langle  \psi \vert \end{eqnarray} is a $9\times1$ matrix.",
                 r"$({\rm c})$ \begin{eqnarray}\langle  \psi \vert * \langle  \psi \vert \end{eqnarray} is a $1\times9$ matrix.",
                 r"$({\rm d})$ \begin{eqnarray}\langle \psi\vert \psi \rangle \end{eqnarray} is a $9\times9$ matrix.",
                 r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle \langle \psi\vert   \end{eqnarray} is a $9\times9$ matrix.",
                 r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle \langle \psi\vert \end{eqnarray} is a $3\times3$ matrix.",
                 ]
)


########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (c) and (f)
    questionText=r"$11.$ For the qutrit state vector, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle +c\vert 2\rangle$, which of the following are true?    $[{\rm SOLUTION}]:$     ",fontSize=0.5,
    answersText=[r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle * \vert \psi \rangle \end{eqnarray} is a $6\times1$ matrix. $[{\rm NO}]$ this would be $9\times1$ (a column vector)",
                 r"$({\rm b})$ \begin{eqnarray} \langle  \psi \vert * \langle  \psi \vert \end{eqnarray} is a $9\times1$ matrix. $[{\rm NO}]$",
                 r"$({\rm c})$ \begin{eqnarray}\langle  \psi \vert * \langle  \psi \vert \end{eqnarray} is a $1\times9$ matrix. $[{\rm YES}]$ one row, nine column, a row vector.",
                 r"$({\rm d})$ \begin{eqnarray}\langle \psi\vert \psi \rangle \end{eqnarray} is a $9\times9$ matrix. $[{\rm NO}]$ this is a number, $1\times1$. ",
                 r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle \langle \psi\vert   \end{eqnarray} is a $9\times9$ matrix. $[{\rm NO}]$ that would be true for two qutrits.",
                 r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle \langle \psi\vert \end{eqnarray} is a $3\times3$ matrix. $[{\rm YES}]$",
                 ]
)

#######################################
############# QUIZ  ##############
########################################


p.newQuiz(#(b)
 #   questionImage="./Figures/Bit_vs_Qubit.JPG",
    questionText=r"$12.$ Is the following a product state or an entangled state?  [1 mark] $\vert \psi\rangle = \alpha(1-\alpha^2)^{1/2}\vert 00\rangle +\alpha^2\vert 01\rangle +(1 - \alpha^2)\vert 10\rangle +\alpha(1- \alpha^2)^{1/2}\vert 11\rangle$",
    answersText=[
        r"$({\rm a})$ ENTANGLED state.",
        r"$({\rm b})$ PRODUCT state.",
    ],
)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Two-qubit product states")
p.leftText(r"""

How to work out whether any quoted two-qubit state is a product state or not?

For a general two-qubit product state we have
\begin{eqnarray}
\vert \Psi\rangle & = & (a \vert 0 \rangle + b \vert 1 \rangle)
* (a \vert 0 \rangle + b \vert 1 \rangle)
 =  \left(\begin{array}{c} 
 ac \\\ 
 ad \\\ 
 bc \\\ 
 bd 
 \end{array}\right)~.
\end{eqnarray}
Note that the product of the coefficients of the $\vert 00\rangle$ and $\vert 11\rangle$ terms is equal to the product of the coefficients of the $\vert 01\rangle$ and $\vert 10\rangle$ terms ($abcd$ in both cases). 


Checking this for 
\begin{eqnarray}
\vert \psi\rangle = \alpha(1-\alpha^2)^{1/2}\vert 00\rangle +\alpha^2\vert 01\rangle +(1 - \alpha^2)\vert 10\rangle +\alpha(1- \alpha^2)^{1/2}\vert 11\rangle
\end{eqnarray}
we get
\begin{eqnarray}
 \alpha^2(1-\alpha^2) = \alpha^2(1-\alpha^2)~,
\end{eqnarray}
and therefore it is a product state. The factorised form is
\begin{eqnarray}
\vert \Psi\rangle & = &   \left[\begin{array}{c} 
 \alpha \\\ 
 (1-\alpha^2)^{1/2} 
 \end{array}\right]
 *
 \left[\begin{array}{c} 
  (1-\alpha^2)^{1/2}  \\\ 
 \alpha 
 \end{array}\right] ~.
\end{eqnarray}
""", fontSize = 0.5)

########################################
#############   SCORES    ##############
########################################

p.newQuiz(
#    questionImage="./Figures/Bell.jpg",
    questionText=r"What was your score?",
    answersText=[
        r"0-3",r"4-7",r"8-11",r"12-15",r"16-19",r"20-22",
     ],
)

p.save("./QIC_Quiz_2.html")

'''
########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="./QIC_Figures/QIC2_Bloch_1.png",
    questionText=r"##In the Bloch sphere representation, which of the following state vectors lie in the $yz$ plane?",
    answersText=[
        r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} 0  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} -{\rm i}  \\\ {\rm i} \end{array}\right)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \cos\textstyle{\theta\over 2}  \\\ {\rm e}^{{\rm i}\pi/2}\sin\textstyle{\theta\over 2} \end{array}\right)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}} \left(\begin{array}{c} -{\rm i}  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{-{\rm i}3\pi/8} \end{array}\right)\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{{\rm i}3\pi/8} \end{array}\right)\end{eqnarray}",
     ],
)


p.newQuiz(# (b) and (d)
    questionImage="./Figures/Bell.jpg",
    questionText=r"Photon pairs are prepared in the Bell state, \begin{eqnarray}\vert \Phi^+ \rangle & = &\frac{1}{\sqrt{2}}\left(\vert {\sf HH} \rangle+\vert {\sf VV} \rangle\right)\end{eqnarray} ",
    answersText=[
        r"$({\rm a})$ If Alice and Bob both measure in the same basis they sometimes get the same result.",
        r"$({\rm b})$ If Alice and Bob both measure in the same basis they always get the same result.",
        r"$({\rm c})$ If Alice and Bob measure in a different same basis they never get the same result.",
        r"$({\rm d})$ If Alice and Bob measure in a different same basis they sometimes get the same result.",
     ],
)

'''





