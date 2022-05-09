from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QLM_Quiz_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QLM Quiz **")

p.makeGrid(3,3)

p.gridImage(0,1,"./QIC_Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./QIC_Figures/time.mp3")



p.newQuiz(#(d)
    questionImage="./Figures/Maxwell.jpg",
    questionText="##Which equation contains a new term introduced by Maxwell?",
    answersText=[
        r"$\nabla \cdot \mathbf{E}=\frac{\rho}{\varepsilon_0}$",
        r"$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$",
        r"$\nabla \cdot \mathbf{B} = 0$",
        r"$\nabla \times \mathbf{B} = \mu_0 ~\mathbf{j} + \varepsilon_0 \mu_0 \frac{\partial \mathbf{E}}{\partial t}$",
    ],
)

p.newQuiz(#(b)
    questionText="#If a plane wave is incident on a lens, the wave fronts in the focal plane are",
    answersText=[r"$({\rm a})$ Planar.",
                 r"$({\rm b})$ Diverging.",
                 r"$({\rm c})$ Converging."]
)

p.newQuiz(#(b)
    questionText="#If a collimated laser beam is incident on a lens, the wave fronts in the focal plane are",
    answersText=[r"$({\rm a})$ Planar.",
                 r"$({\rm b})$ Diverging.",
                 r"$({\rm c})$ Converging."]
)

p.newQuiz(#(a)
    questionText="#If a collimated laser beam is incident on a lens, the beam waist of the focal beam is",
    answersText=[r"$({\rm a})$ Before (upstream of) the focal plane.",
                 r"$({\rm b})$ In the focal plane.",
                 r"$({\rm c})$ Beyond (downstream of) the focal plane."]
)


p.newQuiz( # (c)
    questionImage="./Figures/fourier.png",
    questionText="##Which of the following is the Fourier transform of M?",
    answersImage=[
        "./Figures/Z.png",
        "./Figures/A.png",
        "./Figures/M.png",
        "./Figures/N.png",
        "./Figures/W.png",
        "./Figures/X.png",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(# (d) and (e)
    questionImage="./Figures/Bohr.jpg",
    questionText=r"""## Which of the following are superpositions of the form, $\vert \psi\rangle = \textstyle{1\over\sqrt{2}}\left( \vert 0 \rangle \pm  \vert 1 \rangle \right)$ ?""",
    answersImage=[
        "./Figures/2s12m12.png",
        "./Figures/2p12m12.png",
        "./Figures/1s12m12.png",
        "./Figures/2s12m12+2p12m32.png",
        "./Figures/2s12m12+2p12m12.png",
        "./Figures/2p12m32.png",
    ],
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (c)
    questionText="#The amount of information that can be stored in one qubit is",
    answersText=[r"$({\rm a})$ One bit.",
                 r"$({\rm b})$ Two bits.",
                 r"$({\rm c})$ Infinite.",
                 r"$({\rm d})$ In depends on the measurement."]
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(# (a)
    questionText="#The amount of information that can be retrieved from one qubit is",
    answersText=[r"$({\rm a})$ One bit.",
                 r"$({\rm b})$ Two bits.",
                 r"$({\rm c})$ Infinite.",
                 r"$({\rm d})$ In depends on the measurement."]
)

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

p.newQuiz(
#    questionImage="./Figures/Bell.jpg",
    questionText=r"What was your score?",
    answersText=[
        r"0-4",r"5-8",r"8-12",r"13",r"14",r"15",
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

p.save("./QLM_Quiz.html")




