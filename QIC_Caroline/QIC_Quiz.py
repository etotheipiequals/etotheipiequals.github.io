from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_Quiz_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz **")

p.makeGrid(3,3)

p.gridImage(0,1,"./QIC_Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./QIC_Figures/time.mp3")

########################################
############# QUIZ  ##############
########################################

p.newQuiz(
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

p.newQuiz(
    questionText="#The amount of information that can be stored in one qubit is",
    answersText=[r"One bit.",
                 r"Two bits.",
                 r"Infinite.",
                 r"In depends on the measurement."]
)

########################################
############# QUIZ slide ##############
########################################

p.newQuiz(
    questionText="#The amount of information that can be retrieved from one qubit is",
    answersText=[r"One bit.",
                 r"Two bits.",
                 r"Infinite.",
                 r"In depends on the measurement."]
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(
#    questionImage="./Quiz_figures/Maxwell.jpg",
    questionText=r"##In the Bloch sphere representation, which of the following state vectors lie in the $yz$ plane?",
    answersText=[
        r"\begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} 0  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"\begin{eqnarray}\vert \psi \rangle & = &\left(\begin{array}{c} \cos\textstyle{\theta\over 2}  \\\ {\rm e}^{{\rm i}\pi}\sin\textstyle{\theta\over 2} \end{array}\right)\end{eqnarray}",
        r"\begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} -{\rm i}  \\\ {\rm i} \end{array}\right)\end{eqnarray}",
        r"\begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}} \left(\begin{array}{c} -{\rm i}  \\\ 1 \end{array}\right)\end{eqnarray}",
        r"\begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{-{\rm i}3\pi/8} \end{array}\right)\end{eqnarray}",
        r"\begin{eqnarray}\vert \psi \rangle & = &\textstyle{1\over\sqrt{2}}\left(\begin{array}{c} {\rm e}^{{\rm i}\pi/8}  \\\ {\rm e}^{{\rm i}3\pi/8} \end{array}\right)\end{eqnarray}",
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

p.save("./QIC_Quiz.html")

# LIST OF POSSIBLE ELEMENTS:
#
### p.newSlide()   followed by some number of
#
# p.title(markdown_text, fontSize=1):
#
# p.leftText(markdown_text, fontSize=1)
# p.rightText(markdown_text, fontSize=1)
# p.spanText(markdown_text, fontSize=1)
# p.spanCenterText(markdown_text, fontSize=1)
#
# p.leftImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.rightImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.spanImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.spanCenterImage(fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
#
# p.leftIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.rightIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.spanIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1):
# p.spanCenterIFrame(url, textBelow=None, textAbove=None, height=None, fontSize=1)
#
# p.leftMyCamera(height=None)
# p.rightMyCamera(height=None)
# p.spanMyCamera(height=None)
# p.spanCenterMyCamera(height=None)
#
# p.leftMP4(source, height=None):
# p.rightMP4(source, height=None)
# p.spanMP4(source, height=None):
# p.spanCenterMP4(source, height=None):
#
###    OR  grid layout
#
# p.newSlide()   followed by
# p.makeGrid(rows, columns, padding="0.3em")    followed by some number of
#
# p.gridText(row, column, markdown_text, fontSize=1)
# p.gridImage(row, column, fileName, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.gridIFrame(row, column, url, textBelow=None, textAbove=None, height=None, fontSize=1)
# p.gridMyCamera(row, column, height=None)
# p.gridMP4(row, column, source, height=None):
#
###    OR quiz
# p.newQuiz(questionText=None, questionImage=None, answersText = None, answersImage=None, fontSize=1 )
#
#   NOTE: quiz does not have p.newSlide before
#   NOTE: Quiz questoin can use both questionText and questionImage
#         but that Quiz answer can use EITHER answersText list or answersImage list
#         and maximum number of answers options supported currently is 6
#
###  NOTE: markdown text input
#          it's best to enclose it between    r""" ... """
#          (note r before the first tripple of ")
#          as in this way multiline input and LaTeX work fine
#
