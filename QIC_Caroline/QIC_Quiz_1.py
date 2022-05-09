from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_Quiz_1_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black



########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz 1 **")

p.makeGrid(3,3)

p.gridImage(0,1,"./QIC_Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./QIC_Figures/time.mp3")



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

p.newQuiz(#(a) and (d)
    questionImage="./Figures/Bit_vs_Qubit.JPG",
    questionText=r"$1.$ $[{\rm SOLUTION}]$", fontSize = 0.8,
    answersText=[
        r"$({\rm a})$ They could solve some problems much faster than classical computers. $$[{\rm YES}]$$",
        r"$({\rm b})$ They have a much higher clock speed than classical computers. $$[{\rm NO}]$$",
        r"$({\rm c})$ They do not consume any energy. $$[{\rm NO}]$$",
        r"$({\rm d})$ The raw materials are cheap. $$[{\rm NOT~PARTICULARLY}]$$",
        r"$({\rm e})$ Because we can. $$[{\rm YES}]$$",
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

p.newQuiz(# (d) and (e)
    questionImage="./Figures/Bohr.jpg",
    questionText=r"$2.$  $[{\rm SOLUTION}]$ These two are superpositions. We can pick them out as their electric charge distribution is not symmetric.",
    answersImage=[
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./QIC_Figures/Blank.png",
        "./Figures/2s12m12+2p12m32.png",
        "./Figures/2s12m12+2p12m12.png",
        "./QIC_Figures/Blank.png",
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

p.newQuiz(# (c)
    questionText=r"$3.$ $[{\rm SOLUTION}]$ $({\rm c})$", fontSize=0.8,
    answersText=[r"$({\rm a})$ One bit.",
                 r"$({\rm b})$ Two bits.",
                 r"$({\rm c})$ Infinite. $$[{\rm CORRECT}]$$ because the coefficients $a$ and $b$ can be specified with infinite precision.",
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

p.newQuiz(# (a)
    questionText=r"$4.$ $[{\rm SOLUTION}]$ $({\rm a})$", fontSize=0.8,
    answersText=[r"$({\rm a})$ One bit. $$[{\rm CORECT}]$$ A single measurement can only give us a $0$ or $1$.",
                 r"$({\rm b})$ Two bits.",
                 r"$({\rm c})$ Infinite.",
                 r"$({\rm d})$ It depends on the measurement."]
)

########################################
############# QUIZ  ##############
########################################


p.newQuiz(#(d)
    questionImage="./Figures/Bit_vs_Qubit.JPG",
    questionText=r"$5.$ From a single measurement on a single qubit in the pure state, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle$, we learn",
    answersText=[
        r"$({\rm a})$ The values of $a$ and $b$",
        r"$({\rm b})$ That either $a$ or $b$ is non-zero.",
        r"$({\rm c})$ The values of $\vert a\vert^2$ and $\vert b\vert^2$.",
        r"$({\rm d})$ The values of $\vert a\vert^2$ and $\vert b\vert^2$ if the qubit is in an eigenstate.",
        r"$({\rm e})$ None of the above.",
    ],
)

p.newQuiz(#(d)
    questionImage="./Figures/Bit_vs_Qubit.JPG", fontSize=0.5,
    questionText=r"$5.$ $[{\rm SOLUTION}]$ $({\rm d})$",
    answersText=[
        r"$({\rm a})$ The values of $a$ and $b$.",
        r"$({\rm b})$ That either $a$ or $b$ is non-zero. $$[{\rm NO}]$$ because we already know that they cannot both be zero.",
        r"$({\rm c})$ The values of $\vert a\vert^2$ and $\vert b\vert^2$.",
        r"$({\rm d})$ The values of $\vert a\vert^2$ and $\vert b\vert^2$ if the qubit is in an eigenstate. $$[{\rm YES}]$$ assuming the question meant an eigenstate in the measurement basis. If we know we have either a $0$ or a $1$, a single measurement will tell us which.",
        r"$({\rm e})$ None of the above.",
    ],
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (c)
    questionText=r"$6.$ For three qubits, the number of states is: ",
    answersText=[r"$({\rm a})$ 3.",
                 r"$({\rm b})$ 6.",
                 r"$({\rm c})$ 8.",
                 r"$({\rm d})$ 9."]
)

p.newQuiz(# (c)
    questionText=r"$6.$ For three qubits, the number of states is: ",
    answersText=[r"$({\rm a})$ 3.",
                 r"$({\rm b})$ 6.",
                 r"$({\rm c})$ 8. $$[{\rm CORRECT}]$$ $2^3 = 8$.",
                 r"$({\rm d})$ 9."]
)

p.newQuiz(# (c)
    questionText=r"$7.$ A qutrit is desribed by the state vector, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle +c\vert 2\rangle$. What is the number of states of two qutrits?",
    answersText=[r"$({\rm a})$ 4.",
                 r"$({\rm b})$ 6.",
                 r"$({\rm c})$ 9.",
                 r"$({\rm d})$ 27."]
)

p.newQuiz(# (c)
    questionText=r"$7.$ A qutrit is desribed by the state vector, $\vert \psi\rangle = a\vert 0\rangle +b\vert 1\rangle +c\vert 2\rangle$. What is the number of states of two qutrits?",
    answersText=[r"$({\rm a})$ 4.",
                 r"$({\rm b})$ 6.",
                 r"$({\rm c})$ 9. $$[{\rm CORRECT}]$$ $3^2 = 9$.",
                 r"$({\rm d})$ 27."]
)

p.newQuiz(
#    questionImage="./Figures/Bell.jpg",
    questionText=r"What was your score?",
    answersText=[
        r"0-2",r"3-4",r"5-6",r"7-8",r"9",r"10",
     ],
)


p.newQuiz(
#    questionImage="./Figures/Bell.jpg",
    questionText=r"What is your opinion?",
    answersText=[
        r"I like quizzes and want more.",
        r"They do nothing for me.",
     ],
)

########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("What Richard Feynman said!")

p.leftText(r"""
... you'll get down a drain,

... nobody has yet escaped,

... nobody knows how it can be like that.
           
           """)
p.rightIFrame("https://www.youtube.com/embed/41Jc75tQcB0?start=509&end=521", height=315)

p.save("./QIC_Quiz_1.html")

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





