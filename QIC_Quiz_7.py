from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_Quiz_7_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz 7: Ramsey sequence **")

p.spanCenterImage("./Figures/Ramsey_static.png", height = 600, textBelow=r"Horizontal axis steps through the Ramsey sequence. Vertical axis vary phase, $\phi$.", fontSize = 1.0)




########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (a)
    questionImage="./QIC_Figures/QIC1_Ibn_Khallikan.jpg",
    questionText=r"$1.$ Which of the following sketches best illustrates the effect of decoherence on Ramsey fringes? [1 mark]",
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
    questionText=r"$2.$ Which of the following sketches best illustrates the effect of decay on Ramsey fringes? [1 mark]",
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

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC4_rotation.png",
    questionText=r"$3.$ Which of the following is true? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} {\sf R}_x^{\pi/2} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} 1 & {\rm i}\\\
{\rm i} & 1 \end{array} \right)  \end{eqnarray} ",
        r"$({\rm b})$ \begin{eqnarray} {\sf R}_x^{\pi/2} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} 1 & -{\rm i}\\\
{\rm i} & 1 \end{array} \right)  \end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray} {\sf R}_x^{\pi/2} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} 1 &   -{\rm i}\\\
-{\rm i} & 1 \end{array} \right)  \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray} {\sf R}_x^{\pi/2} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} 1 &  {\rm i}\\\
-{\rm i} & 1 \end{array} \right)  \end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC4_rotation.png",
    questionText=r"$4.$ Which of the following is true? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} {\sf R}_x^{\phi} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} \cos\textstyle{\Theta\over 2} & {\rm i}\sin\textstyle{\Theta\over 2}\\\
{\rm i}\sin\textstyle{\Theta\over 2} & \cos\textstyle{\Theta\over 2} \end{array} \right)  \end{eqnarray} ",
        r"$({\rm b})$ \begin{eqnarray} {\sf R}_x^{\phi} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} \cos\phi & -{\rm i}\sin\phi\\\
-{\rm i}\sin\phi & \cos\phi \end{array} \right)  \end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray} {\sf R}_x^{\phi} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} \cos\textstyle{\phi\over 2} &   -{\rm i}\sin\textstyle{\phi\over 2}\\\
-{\rm i}\sin\textstyle{\phi\over 2} & \cos\textstyle{\phi\over 2} \end{array} \right)  \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray} {\sf R}_x^{\phi} & = & \textstyle{1\over \sqrt{2}}\left( \begin{array}{cc} \cos\textstyle{\phi\over 2} &  {\rm i}\sin\textstyle{\phi\over 2}\\\
-{\rm i}\sin\textstyle{\phi\over 2} & \cos\textstyle{\phi\over 2} \end{array} \right)  \end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(e)
    questionImage="./QIC_Figures/QIC7_Ramsey_0.png",
    questionText=r"$5.$ A Ramsey-like sequence ${\sf R}_y^{\pi/2}{\sf R}_x^{\phi}{\sf R}_y^{\pi/2}$ is applied to a qubit initially in state $\vert 0\rangle$. The probabity of detecting state a $\vert 0\rangle$ at the output, $P_0$, is measured. Which of the following is true? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} P_0 & = & 0   \end{eqnarray} ",
        r"$({\rm b})$ \begin{eqnarray} P_0 & = & \textstyle{1\over 2}   \end{eqnarray} ",
        r"$({\rm c})$ \begin{eqnarray} P_0 & = & \cos^2\textstyle{\phi\over 2}   \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray} P_0 & = & \sin^2\textstyle{\phi\over 2}   \end{eqnarray}",
       r"$({\rm e})$ \begin{eqnarray} P_0 & = & 1   \end{eqnarray}",
        r"$({\rm f})$ None of the above.",
    ],
)

########################################
############# QUIZ  ##############
########################################/

p.newQuiz(#(d)
    questionImage="./QIC_Figures/QIC7_Ramsey_0.png",
    questionText=r"$6.$ In the Ramsey-like sequence ${\sf R}_y^{\pi/2}{\sf R}_x^{\phi}{\sf R}_y^{\pi/2}$, what is the effect of the ${\sf R}_x^{\phi}$ rotation? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ Nothing. ",
        r"$({\rm b})$ Changes the relative phase by $\phi/2$. ",
        r"$({\rm c})$ Changes the relative phase by $\phi$.",
        r"$({\rm d})$ Changes the global phase by $\phi/2$.",
       r"$({\rm e})$ Changes the global phase by $\phi$.",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(b)
    questionImage="./QIC_Figures/QIC7_Ramsey_0.png",
    questionText=r"$7.$ A Ramsey-like sequence ${\sf R}_y^{\pi/2}{\sf R}_y^{\pi/2}{\sf R}_y^{\pi/2}$ is applied to a qubit initially in state $\vert 0\rangle$. The probabity of detecting state a $\vert 0\rangle$ at the output, $P_0$, is measured. Which of the following is true? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} P_0 & = & 0   \end{eqnarray} ",
        r"$({\rm b})$ \begin{eqnarray} P_0 & = & \textstyle{1\over 2}   \end{eqnarray} ",
        r"$({\rm c})$ \begin{eqnarray} P_0 & = & \cos^2\textstyle{\phi\over 2}   \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray} P_0 & = & \sin^2\textstyle{\phi\over 2}   \end{eqnarray}",
       r"$({\rm e})$ \begin{eqnarray} P_0 & = & 1   \end{eqnarray}",
        r"$({\rm f})$ None of the above.",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC7_Ramsey_0.png",
    questionText=r"$8.$ A Ramsey-like sequence ${\sf R}_x^{\pi/2}{\sf R}_z^{\phi}{\sf R}_y^{\pi/2}$ is applied to a qubit initially in state $\vert 0\rangle$. The probabity of detecting state a $\vert 0\rangle$ at the output, $P_0$, is measured. Which of the following is true? [1 mark]""", fontSize=1.0,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} P_0 & = & \cos^2\textstyle{\phi\over 2}   \end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray} P_0 & = & \cos^2\left( \textstyle{\phi\over 2} -\textstyle{\pi\over 4} \right)  \end{eqnarray} ",
        r"$({\rm c})$ \begin{eqnarray} P_0 & = & \cos^2\left( \textstyle{\phi\over 2} -\textstyle{\pi\over 2} \right)  \end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray} P_0 & = & \sin^2\textstyle{\phi\over 2}   \end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray} P_0 & = & \sin^2\left( \textstyle{\phi\over 2} -\textstyle{\pi\over 4} \right)  \end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray} P_0 & = & \sin^2\left( \textstyle{\phi\over 2} -\textstyle{\pi\over 2} \right)  \end{eqnarray}",
    ],
)






p.save("./QIC_Quiz_7.html")

'''
########################################
############# QUIZ  ##############
########################################


p.newQuiz(# (b) and (d)
    questionImage="./Figures/Bell.jpg",
    questionText=r"Photon pairs are prepared in the Bell state, \begin{eqnarray}\vert \Phi^+ \rangle & = &\frac{1}{\sqrt{2}}\left(\vert {\sf HH} \rangle+\vert {\sf VV} \rangle\right)\end{eqnarray}. Which of the following are {\bf TRUE}? ",
    answersText=[
        r"$({\rm a})$ If Alice and Bob both measure in the same basis they sometimes get the same result.",
        r"$({\rm b})$ If Alice and Bob both measure in the same basis they always get the same result.",
        r"$({\rm c})$ If Alice and Bob measure in a different same basis they never get the same result.",
        r"$({\rm d})$ If Alice and Bob measure in a different same basis they sometimes get the same result.",
     ],
)

'''





