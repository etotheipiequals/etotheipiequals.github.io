from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_Quiz_3_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz 3 **")

p.spanCenterImage("./QIC_Figures/QIC3_BlochDM_H.png", height = 600, textBelow=r"Bloch vector (blue). Rotation axis (yellow).", fontSize = 1.0)




########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b)
    questionImage="./QIC_Figures/QIC1_Ibn_Khallikan.jpg",
    questionText=r"$1.$ In the context of quantum advantage---why quantum computers are more powerful than classical computers---which of the following best illustrates exponential scaling? [1 mark]",
    answersImage=[
        "./QIC_Figures/QIC1_moores_law_1.png",
        "./QIC_Figures/QIC1_exponential_scaling.png",
        "./QIC_Figures/QIC1_energy_2.png",
        "./QIC_Figures/QIC1_energy_1.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b)
    questionImage="./QIC_Figures/QIC1_Ibn_Khallikan.jpg",
    questionText=r"$1.$ $[{\rm Solution}]$ $({\rm b})$ Each square of the guess board has a factor of 2 more grains of wheat just like each qubit gives a factor of 2 more basis states. Picture (top left) is Ibn Khallikan who first wrote about this in 1256.",
    answersImage=[
        "./QIC_Figures/QIC1_exponential_scaling.png",
#    answersText=[
#        r"$({\rm b})$ Each square of the guess board has a factor of 2 more grains of wheat just like each qubit gives a factor of 2 more basis states.",
     ],
)

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
    questionText=r"$2.$ $[{\rm SOLUTION}]~ ({\rm c})$ State $\vert 1\rangle$ corresponds to a Bloch vector pointing at the South Pole.",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/BS_1.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
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

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$3.$ $[{\rm SOLUTION}] ~ ({\rm e})$ State $\vert -\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle -\vert 1 \rangle)$ corresponds to a Bloch vector pointing in the $-x$ direction (into the page in this image).",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/BS_-.png",
        "./QIC_Figures/Blank.png",
    ],
)




########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./QIC_Figures/QIC2_Bloch_2.png",
    questionText=r"$4.$ Which of the following corresponds to the state $\vert +{\rm i}\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle +{\rm i}\vert 1 \rangle)$? [1 mark]",
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
    questionText=r"$4.$ $[{\rm SOLUTION}] ~ ({\rm e})$ State $\vert +{\rm i}\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle +{\rm i}\vert 1 \rangle)$ corresponds to a Bloch vector pointing in the $+y$ direction (towards the right in this image)",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/BS_+i.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
#    questionImage="./QIC_Figures/QIC3_vonNeumann.png",
    questionText=r"$5.$ The density matrix, $\rho$ with element $\rho_{ij}$, for a qubit is \begin{eqnarray}\rho & = &\frac{1}{2} \left(\begin{array}{cc} 1+w & u-{\rm i}v \\\ u+{\rm i}v & 1-w \end{array}\right)~,\end{eqnarray} where $(u,v,w)$ are the cartesian components of the Bloch vector. Which of the following are false? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ $\vert \rho_{ij}\vert  \leq 1 $.",
        r"$({\rm b})$ For $N$ qubits the indices $i$ and $j$ have a range $1$ to $N$ (or $0$ to $N-1$).",
        r"$({\rm c})$ $\rho_{ij}  =  \rho_{ji}^*$ and hence the diagonal element are all real.",
        r"$({\rm d})$ ${\rm Tr}(\rho)=1$.",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b)
#    questionImage="./QIC_Figures/QIC3_vonNeumann.png",
    questionText=r"$5.$ $[{\rm SOLUTION}] ~ ({\rm b})$ """, fontSize=1.0,
    answersText=[
        r"$({\rm a})$ $\vert \rho_{ij}\vert  \leq 1 $.",
        r"$({\rm b})$ For $N$ qubits the indices $i$ and $j$ have a range $1$ to $N$ (or $0$ to $N-1$). $[{\rm CORRECT}]$. This is $[{\rm FALSE}]$ The indices range from $1$ to $2N$. ",
        r"$({\rm c})$ $\rho_{ij}  =  \rho_{ji}^*$ and hence the diagonal element are all real.",
        r"$({\rm d})$ ${\rm Tr}(\rho)=1$.",
    ],
)



########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$6.$ Which of the following corresponds to the state $\vert 0\rangle$? $[1~{\rm mark}]$",
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
    questionText=r"$6.$ $[{\rm SOLUTION}] ~ ({\rm f})$ corresponds to the state $\vert 0\rangle$. \begin{eqnarray}\rho & = & \vert 0\rangle\langle 0\vert = \textstyle{1\over\sqrt{2}}{\small \left(\begin{array}{c} 1  \\\ 0 \end{array}\right)} \textstyle{1\over\sqrt{2}}{\small \left(\begin{array}{cc} 1 & 0 \end{array}\right)} =  {\small \left(\begin{array}{cc} 1 & 0 \\\ 0 & 0 \end{array}\right)}\end{eqnarray}",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/DM+z.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$7.$ Which of the following corresponds to the state $\vert -\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle -\vert 1 \rangle)$? [1 mark]",
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
    questionText=r"$7.$ $[{\rm SOLUTION}] ~ ({\rm d})$ corresponds to the state $\vert -\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle -\vert 1 \rangle)$. \begin{eqnarray}\rho & = & \vert -\rangle\langle -\vert = \textstyle{1\over\sqrt{2}}{\small \left(\begin{array}{c} 1  \\\ -1 \end{array}\right)} \textstyle{1\over\sqrt{2}}{\small \left(\begin{array}{cc} 1 & -1 \end{array}\right)} = \frac{1}{2}{\small \left(\begin{array}{cc} 1 & -1 \\\ -1 & 1 \end{array}\right)}\end{eqnarray}",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/DM-x.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (e)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$8.$ Which of the following corresponds to the state $\vert +{\rm i}\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle +{\rm i}\vert 1 \rangle)$? [1 mark]",
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
    questionText=r"$8.$ $[{\rm SOLUTION}] ~ ({\rm a})$ corresponds to the state $\vert +{\rm i}\rangle =\textstyle{1\over\sqrt{2}}(\vert 0\rangle +{\rm i}\vert 1 \rangle)$. \begin{eqnarray}\rho & = & \vert +{\rm i}\rangle\langle +{\rm i}\vert = \textstyle{1\over\sqrt{2}}{\small \left(\begin{array}{c} 1  \\\ {\rm i} \end{array}\right)} \textstyle{1\over\sqrt{2}}{\small \left(\begin{array}{cc} 1 & -{\rm i} \end{array}\right)} = \frac{1}{2} {\small \left(\begin{array}{cc} 1 & -{\rm i} \\\ {\rm i} & 1 \end{array}\right)}\end{eqnarray}",
    answersImage=[
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b) and (d)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$9.$ When a qubit interacts with the environment the coherences decay and the state becomes mixed. Which of the following corresponds to a MIXED state? $[1~{\rm mark}]$",
    answersImage=[
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/DM_pure_1.png",
       "./QIC_Figures/DM_1.png",
        "./QIC_Figures/DM_mixed_1.png",
         "./QIC_Figures/DM_pure_2.png",
        "./QIC_Figures/DM_pure_3.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b) and (d)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$9.$ $[{\rm SOLUTION}] ~ ({\rm d})$ is a MIXED state. Note how the off-diagonal matrix elements have decayed to near zero.",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
       "./QIC_Figures/Blank.png",
        "./QIC_Figures/DM_mixed_1.png",
         "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b) and (d)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$10.$ Which of the following correspond to a MIXED state? $[1~{\rm mark}]$",
    answersImage=[
        "./QIC_Figures/DM-y.png",
        "./QIC_Figures/DM_mixed.png",
        "./QIC_Figures/DM_pure_1.png",
        "./QIC_Figures/DM+y.png",
        "./QIC_Figures/DM_pure_2.png",
        "./QIC_Figures/DM_pure_3.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (b) and (d)
    questionImage="./Figures/Colour_Wheel.JPG",
    questionText=r"$10.$ $[{\rm SOLUTION}] ~ ({\rm b})$ is a MIXED state. Note how the magnitude of the coherences (the off-diagonal terms) are less than either of the diagonals.",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/DM_mixed.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b)
    questionImage="./QIC_Figures/QIC3_vonNeumann.png",
    questionText=r"$10+.$ [BONUS QUESTION] The density matrix for a qubit in either a pure or a mixed state is \begin{eqnarray}\rho & = &\frac{1}{2} \left(\begin{array}{cc} 1+w & u-{\rm i}v \\\ u+{\rm i}v & 1-w \end{array}\right)~.\end{eqnarray} Which of the following is NOT true? [1 mark]", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ ${\rm Tr}(\rho^2) = u^2+v^2+w^2$.",
        r"$({\rm b})$ ${\rm Tr}(\rho^2) = \textstyle{1\over 2}(1+ u^2+v^2+w^2)$.",
        r"$({\rm d})$ ${\rm Tr}(\rho)=1$.",
        r"$({\rm e})$ ${\rm Tr}(\rho^2)= 1$ for a pure state.",
        r"$({\rm f})$ ${\rm Tr}(\rho^2)< 1$ for a mixed state.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b)
    questionImage="./QIC_Figures/QIC3_vonNeumann.png",
    questionText=r"$10+.$ $[{\rm SOLUTION}] ~ ({\rm a})$", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ ${\rm Tr}(\rho^2) = u^2+v^2+w^2~$ $[{\rm CORRECT}]$ this is FALSE.",
        r"$({\rm b})$ ${\rm Tr}(\rho^2) = \textstyle{1\over 2}(1+ u^2+v^2+w^2)$.",
        r"$({\rm d})$ ${\rm Tr}(\rho)=1$.",
        r"$({\rm e})$ ${\rm Tr}(\rho^2)= 1$ for a pure state.",
        r"$({\rm f})$ ${\rm Tr}(\rho^2)< 1$ for a mixed state.",
    ],
)


p.save("./QIC_Quiz_3.html")

'''
########################################
############# QUIZ  ##############
########################################


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





