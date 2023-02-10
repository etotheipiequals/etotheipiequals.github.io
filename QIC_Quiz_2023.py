from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_2023_Quiz_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(d)
    questionImage="./Figures/Caroline_Herschel.JPG",
    questionText="##Are you connected?",
    answersText=[
        r"Yes, I can vote.",
        r"No, I cannot vote.",
    ],
)

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz 2023 **")

p.makeGrid(3,3)

p.gridImage(0,1,"./QIC_Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./QIC_Figures/time.mp3")

'''

########################################
############# QUIZ  ##############
########################################


p.newQuiz(#(a) and (d)
    questionImage="./Figures/Bit_vs_Qubit.JPG",
    questionText=r"$1.$ Why might we want to build a quantum computer?",
    answersText=[
        r"$({\rm a})$ They could solve some problems much faster than classical computers.",
        r"$({\rm b})$ They have a much higher clock speed than classical computers.",
        r"$({\rm c})$ They do not consume any energy.",
        r"$({\rm d})$ The raw materials are cheap.",
        r"$({\rm e})$ Because we can.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (d) and (e)
    questionImage="./Figures/Bohr.jpg",
    questionText=r"$2.$  Which of the following are superpositions of the form, $\vert \psi\rangle = \textstyle{1\over\sqrt{2}}\left( \vert 0 \rangle \pm  \vert 1 \rangle \right)$ ?",
    answersImage=[
        "./Figures/2s12m12.png",
        "./Figures/2p12m12.png",
        "./Figures/1s12m12.png",
        "./Figures/2s12m12+2p12m32.png",
        "./Figures/2s12m12+2p12m12.png",
        "./Figures/2p12m32.png",
    ],
)

'''

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


'''
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
'''

########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (a) and (d)
    questionImage="./QIC_Figures/QIC9_GHZ.png",
    questionText=r"$2.$ Which of the following is applicable to a quantum two-qubit gate?  [2 marks]",
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
############# QUIZ slide ##############
########################################

p.newQuiz(# (c)
    questionText=r"$3.$ The amount of information that can be stored in one qubit is",
    answersText=[r"$({\rm a})$ One bit.",
                 r"$({\rm b})$ Two bits.",
                 r"$({\rm c})$ Infinite.",
                 r"$({\rm d})$ It depends on the measurement."]
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (a)
    questionText=r"$4.$ The amount of information that can be retrieved from one qubit is",
    answersText=[r"$({\rm a})$ One bit.",
                 r"$({\rm b})$ Two bits.",
                 r"$({\rm c})$ Infinite.",
                 r"$({\rm d})$ It depends on the measurement."]
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (c)
    questionText=r"$5.$ For three qubits, the number of states is: ",
    answersText=[r"$({\rm a})$ 3.",
                 r"$({\rm b})$ 6.",
                 r"$({\rm c})$ 8.",
                 r"$({\rm d})$ 9."]
)

p.newQuiz(# (c)
    questionText=r"$6.$ A qutrit is desribed by the state vector, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle +c\vert 2\rangle$. What is the number of states of two qutrits?",
    answersText=[r"$({\rm a})$ 4.",
                 r"$({\rm b})$ 6.",
                 r"$({\rm c})$ 9.",
                 r"$({\rm d})$ 27."]
)

########################################
############# QUIZ  ##############
########################################


p.newQuiz(#(d)
    questionImage="./Figures/Bit_vs_Qubit.JPG",
    questionText=r"$7.$ From a single measurement on a single qubit in the pure state, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle$, we learn",
    answersText=[
        r"$({\rm a})$ The values of $a$ and $b$",
        r"$({\rm b})$ That either $a$ or $b$ is non-zero.",
        r"$({\rm c})$ The values of $\vert a\vert^2$ and $\vert b\vert^2$.",
        r"$({\rm d})$ The values of $\vert a\vert^2$ and $\vert b\vert^2$ if the qubit is in an eigenstate.",
        r"$({\rm e})$ None of the above.",
    ],
)


#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b) and (e)
    questionImage="./QIC_Figures/QIC2_DiVincenzo_1.png",
    questionText=r"$8.$ Which of the DiVincenzo criteria can't we test (fully) with a single qubit?  [2 marks]",
    answersText=[
        r"$({\rm a})$ Initialisation.",
        r"$({\rm b})$ Gates.",
        r"$({\rm c})$ Read-out.",
        r"$({\rm d})$ Decoherence.",
        r"$({\rm e})$ Scalability.",
    ],
)

'''

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$2.$ Which of the following corresponds to the state $\vert 1\rangle$? $[1~{\rm mark}]$",
    answersImage=[
        "./QIC_Figures/BS_+.png",
        "./QIC_Figures/BS_-i.png",
        "./QIC_Figures/BS_1.png",
        "./QIC_Figures/BS_0.png",
        "./QIC_Figures/BS_-.png",
        "./QIC_Figures/BS_+i.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$3.$ Which of the following corresponds to the state $\vert -\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle -\vert 1 \rangle)$? [1 mark]",
    answersImage=[
        "./QIC_Figures/BS_+.png",
        "./QIC_Figures/BS_-i.png",
        "./QIC_Figures/BS_1.png",
        "./QIC_Figures/BS_0.png",
        "./QIC_Figures/BS_-.png",
        "./QIC_Figures/BS_+i.png",
    ],
)

'''

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$9.$ Which of the following corresponds to the state $\vert +{\rm i}\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle +{\rm i}\vert 1 \rangle)$? [1 mark]",
    answersImage=[
        "./QIC_Figures/BS_+.png",
        "./QIC_Figures/BS_-i.png",
        "./QIC_Figures/BS_1.png",
        "./QIC_Figures/BS_0.png",
        "./QIC_Figures/BS_-.png",
        "./QIC_Figures/BS_+i.png",
    ],
)




#######################################
############# QUIZ  ##############
########################################

p.newQuiz(#(a) and (d)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$10.$ Which of the following are true? $[2~{\rm marks}]$",
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

p.newQuiz(#(a) and (c)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$11.$ Which of the following CANNOT be represented using a Bloch sphere?  [2 marks]",
    answersText=[
        r"$({\rm a})$ A harmonic oscillator.",
        r"$({\rm b})$ Photon polarization.",
        r"$({\rm c})$ Quantum entanglement.",
        r"$({\rm d})$ Decoherence.",
        r"$({\rm e})$ Any two-level system.",
        r"$({\rm f})$ An electron spin.",
    ],
)





########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (b) and (f)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$12.$ In the Bloch sphere representation, which of the following state vectors ${\bf {\rm DO~ NOT}}$ lie in the $yz$ plane? $~~~$ [2 marks]",
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

p.newQuiz(# (e)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$13.$ Which of the following corresponds to the state $\vert 0\rangle$? $[1~{\rm mark}]$",
    answersImage=[
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/DM-z.png",
        "./QIC_Figures/DM-y.png",
        "./QIC_Figures/DM-x.png",
        "./QIC_Figures/DM+x.png",
        "./QIC_Figures/DM+z.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$14.$ Which of the following corresponds to the state $\vert -\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle -\vert 1 \rangle)$? [1 mark]",
    answersImage=[
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/DM-z.png",
        "./QIC_Figures/DM-y.png",
        "./QIC_Figures/DM-x.png",
        "./QIC_Figures/DM+x.png",
        "./QIC_Figures/DM+z.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b) and (d)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$15.$ When a qubit interacts with the environment the coherences decay and the state becomes mixed. Which of the following corresponds to a MIXED state? $[1~{\rm mark}]$",
    answersImage=[
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/DM_pure_1.png",
       "./QIC_Figures/DM_1.png",
        "./QIC_Figures/DM_mixed_1.png",
         "./QIC_Figures/DM_pure_2.png",
        "./QIC_Figures/DM_pure_3.png",
    ],
)



'''

p.newQuiz(#(a)
    questionImage="./QIC_Figures/R_pi3.png",
    questionText=r"$16.$ For the rotation shown (from red dot to red dot), what is the rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

'''

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nxnz.png",
    questionText=r"$16.$ For the rotation shown (from red dot to red dot), what is the rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC5_rabi_oscillation_noisey_1.png",
    questionText=r"$17.$ The blue line (average of the red measurement data) shows the simulated dymanics of a qubit driven by a noisey field. What is the total rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 4\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 6\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 16\pi\end{eqnarray}",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (a)
    questionImage="./QIC_Figures/QIC1_Ibn_Khallikan.jpg",
    questionText=r"$18.$ Which of the following sketches best illustrates the effect of decoherence on Ramsey fringes? [1 mark]",
    answersImage=[
        "./QIC_Figures/QIC_7_Quiz_Ramsey_1.png",
        "./QIC_Figures/QIC_7_Quiz_Ramsey_2.png",
        "./QIC_Figures/QIC_7_Quiz_Ramsey_3.png",
        "./QIC_Figures/QIC_7_Quiz_Ramsey_4.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (d)
    questionImage="./QIC_Figures/QIC1_Ibn_Khallikan.jpg",
    questionText=r"$19.$ Which of the following sketches best illustrates the effect of decay on Ramsey fringes? [1 mark]",
    answersImage=[
        "./QIC_Figures/QIC_7_Quiz_Ramsey_1.png",
        "./QIC_Figures/QIC_7_Quiz_Ramsey_2.png",
        "./QIC_Figures/QIC_7_Quiz_Ramsey_3.png",
        "./QIC_Figures/QIC_7_Quiz_Ramsey_4.png",
    ],
)


########################################
############# QUIZ  ##############
########################################


p.newQuiz(# (b) and (d)
    questionImage="./Figures/Bell.jpg",
    questionText=r"$20.$ Photon pairs are prepared in the Bell state, \begin{eqnarray}\vert \Phi^+ \rangle & = &\frac{1}{\sqrt{2}}\left(\vert {\sf HH} \rangle+\vert {\sf VV} \rangle\right)~.\end{eqnarray} Which of the following are ${\bf {\rm TRUE}}$? ",
    answersText=[
        r"$({\rm a})$ If Alice and Bob both measure in the same basis they sometimes get the same result.",
        r"$({\rm b})$ If Alice and Bob both measure in the same basis they always get the same result.",
        r"$({\rm c})$ If Alice and Bob measure in a different same basis they never get the same result.",
        r"$({\rm d})$ If Alice and Bob measure in a different same basis they sometimes get the same result.",
     ],
)







########################################
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$EXTRA 21.$ Which of the following are possible qubit states?  $[4~{\rm marks}]$",
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

p.newQuiz(# (b) and (d)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$EXTRA 22.$ Which of the following correspond to a MIXED state? $[1~{\rm mark}]$",
    answersImage=[
        "./QIC_Figures/DM-y.png",
        "./QIC_Figures/DM_mixed.png",
        "./QIC_Figures/DM_pure_1.png",
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/DM_pure_2.png",
        "./QIC_Figures/DM_pure_3.png",
    ],
)


p.newQuiz(#(b)
    questionImage="./QIC_Figures/QIC3_vonNeumann.png",
    questionText=r"$EXTRA 23.$ A qubit is in either a pure or a mixed state. If we writee the density matrix in the form \begin{eqnarray}\rho & = &\frac{1}{2} \left(\begin{array}{cc} 1+w & u-{\rm i}v \\\ u+{\rm i}v & 1-w \end{array}\right)~, \end{eqnarray} which of the following is NOT true? [1 mark]", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ ${\rm Tr}(\rho^2) = u^2+v^2+w^2$.",
        r"$({\rm b})$ ${\rm Tr}(\rho^2) = \textstyle{1\over 2}(1+ u^2+v^2+w^2)$.",
        r"$({\rm d})$ ${\rm Tr}(\rho)=1$.",
        r"$({\rm e})$ ${\rm Tr}(\rho^2)leq 1$.",
        r"$({\rm f})$ $u^2+v^2+w^2\leq 1$.",
    ],
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (c) and (f)
    questionText=r"$Extra 24.$ For the qutrit state vector, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle +c\vert 2\rangle$, which of the following are true?    [2 marks]      [Hint: $m\times n$, $m$ rows $\times$ $n$ columns.]",
    answersText=[r"$({\rm a})$ \begin{eqnarray}\vert \psi \rangle * \vert \psi \rangle \end{eqnarray} is a $6\times1$ matrix. ",
                 r"$({\rm b})$ \begin{eqnarray} \langle  \psi \vert * \langle  \psi \vert \end{eqnarray} is a $9\times1$ matrix.",
                 r"$({\rm c})$ \begin{eqnarray}\langle  \psi \vert * \langle  \psi \vert \end{eqnarray} is a $1\times9$ matrix.",
                 r"$({\rm d})$ \begin{eqnarray}\langle \psi\vert \psi \rangle \end{eqnarray} is a $9\times9$ matrix.",
                 r"$({\rm e})$ \begin{eqnarray}\vert \psi \rangle \langle \psi\vert   \end{eqnarray} is a $9\times9$ matrix.",
                 r"$({\rm f})$ \begin{eqnarray}\vert \psi \rangle \langle \psi\vert \end{eqnarray} is a $3\times3$ matrix.",
                 ]
)



########################################
#############  SAVE  ##############
########################################

p.save("./QIC_2023_Quiz.html")






