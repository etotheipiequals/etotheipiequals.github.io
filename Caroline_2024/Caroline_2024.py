from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
#    presentationServer="http://localhost:8000/Caroline_2024_audience.html",
    presentationServer="https://etotheipiequals.github.io/Caroline_2024/Caroline_2024_audience.html",
    presentationSemaphore=True,  # allows audience to always feed back to lecturer on the speed of the lecture
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title(r"""Long-range interactions in the classroom""")


p.leftImage("./presentation_files/Caroline_Herschel.jpeg", height = 400, textBelow=r"""**Figure**: Caroline Herschel.""" ) 


p.rightText(r"""
**Link**: > pip install Caroline-presentation

          https://github.com/nikolasibalic/Caroline
          
          * Python + HTML
          
          """,fontSize=0.75)


#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("History")


p.spanCenterImage("./Figures/IOPPRydbergPhysics.png", height=600)




#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("History")




p.spanCenterIFrame("./Figures/rydberg_wavefunctions.html", height=600)



#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("History")
p.leftImage("./Figures/Waterstones.png", height=600)
p.rightIFrame("./Figures/bang_bang.html", height=600)

#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Interactivity!")


p.spanCenterIFrame("./Figures/timeline_qo.html", height=1600, textBelow=r"""An interactive guide to quantum optics.""")


########################################
############# NEW slide ##############
########################################

p.newSlide()

p.title(r"""Caroline presentor software""")


p.leftImage("./presentation_files/Caroline_Herschel.jpeg", height = 400, textBelow=r"""**Figure**: Caroline Herschel.""" ) 


p.rightText(r"""
**Link**: > pip install Caroline-presentation

          https://github.com/nikolasibalic/Caroline
          
          * Python + HTML
          
          """,fontSize=0.75)


#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Python code to generate a slide")
p.leftText(
    r"""
Simple example with left/right layout.
```python
p.newSlide()
p.title("History")
p.leftImage("./Figures/Waterstones.png", height=600)
p.rightIFrame("./Figures/bang_bang.html", height=600)
```
""",
    fontSize=0.6,
)

p.rightImage("./Figures/SampleSlide.png", height=600)



#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Python code to generate a slide")
p.leftText(
    r"""
**Grid** layout.
```python
p.newSlide()
p.title("Qubit (two-level system): Examples ")
p.makeGrid(4,4)
p.gridImage(0,1,"./Figures/superconducting.jpg", height = 100, 
	textBelow="Google's Sycamore processor", fontSize = 0.5)
p.gridImage(0,2,"./Figures/superconducting.png", height = 100, 
	textBelow=" Qubits (red): tuning (dark blue);
		control (purple). Coupling (orange). Read-out (blue). 
		https://arxiv.org/abs/1801.07904", fontSize = 0.5)
p.gridImage(0,3,"./Figures/superconducting1.png", height = 100, 
	textBelow="Blais et al, Rev Mod Phys **93**, 25005 (2021)", fontSize = 0.5)
p.gridImage(1,2,"./Figures/ions1.jpg", height = 100, 
	textBelow="Honeywell", fontSize = 0.5)
p.gridImage(1,3,"./Figures/ions2.png", height = 100, 
	textBelow="Chris Monroe, Duke and IonQ", fontSize = 0.5)
p.gridImage(2,3,"./Figures/Rydberg.png", height = 100, 
	textBelow="Barredo et al, Nature  **561**, 79 (2018)", fontSize = 0.5)
```
""",
    fontSize=0.5,
)

p.rightImage("./Figures/SlideExample2.png", height=600)

########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("QLM Xmas Quiz?")

p.makeGrid(3,3)

p.gridImage(0,1,"./Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./Figures/time.mp3")



########################################
#############  New slide  ##############
########################################

p.newQuiz( # (c)
#    questionImage="./Figures/fourier.png",
    questionText="Which of the following is NOT a liquid at room temperature?",
    answersImage=[
        "./Figures/MILK.png",
        "./Figures/BEER.png",
        "./Figures/WINE.png",
        "./Figures/IRON.png",
    ],
)


p.newQuiz( # (c) (d) and (e)
    questionImage="./Figures/BlochSphere1.jpg",
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

########################################
############# NEW slide ##############
########################################

p.newSlide()
p.title("Young's double slit: photon by photon")
p.leftText(r"""
* G. I. Taylor (1886-1975)

* Interference fringes with feeble light

* Proc. Camb. Phil. Soc. 15, 114 (1909).
 
""")

p.rightImage("./Figures/4aiZ.gif", height = 300, textBelow = "Light is both wave and particle", fontSize = 1.0) 



########################################
#############  New slide  ##############
########################################


p.newSlide()
p.title("Audio/Video clips")

p.makeGrid(4,4)


p.gridText(0,0,r"""
** Richard Feynman **
> *Probability and uncertainty - the quantum mechanical view of nature*  

Messenger Letures, Cornell, November 18th, 1964.""", fontSize =0.75
)

p.gridImage(0,1,"./Figures/Feynman.png", height=200)

p.gridText(0,2,r"""
*Don't keep asking yourself, but how can it be like that.....*  
""", fontSize =0.75
)

p.gridIFrame(2,2,"./Figures/nobody2.mp4", height=80) # picture does not appear


########################################
p.newSlide()
p.title("**Synchronisation in a thermal Rydberg gas**")

p.leftImage( "./Figures/KarenFig4.png", height=600, textBelow = r"""
Karen Wadenpfuhl, https://arxiv.org/abs/2306.05188
""",fontSize=0.5)

p.rightIFrame( "./Figures/Metronomes.mp4", height=600, textBelow = r"""
Video from Veritasium, https://www.youtube.com/watch?v=t-_VPRCtiUg
""",fontSize=0.5)




########################################
#############  New slide  ##############
########################################


p.newSlide()
p.title("Open interactive web pages")

p.spanCenterIFrame("https://shilingliang.com/web-simulator-by-GPT4/interactive_vicsek.html", height = 300,
textBelow="Shiliang Liang  https://shilingliang.com/web-simulator-by-GPT4",fontSize=0.75) 


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Open interactive web pages: Quantum circuits")
p.spanCenterIFrame("https://algassert.com/quirk#circuit={%22cols%22:[[%22H%22],[%22%E2%80%A2%22,%22X%22]]}", height = 600) 

########################################
p.newSlide()
p.title("OWID plots")
p.makeGrid(2,2)
#p.gridIFrame(0,0, "https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?facet=none&hideControls=True", height=450)
p.gridIFrame(0,0, "https://ourworldindata.org/grapher/global-energy-substitution?country=~OWID_WRL", height=450)


p.gridIFrame(0,1, "https://ourworldindata.org/grapher/covid-deaths-per-million-exemplars?country=GBR~NZL~?facet=none&hideControls=True", height=450)


#p.gridIFrame(0,1, "https://ourworldindata.org/grapher/covid-deaths-per-million-exemplars?country=USA~GBR~HKG~NZL~DEU~TWN~AUS~?facet=none&hideControls=True", height=450)

#p.gridIFrame(1,0, "https://ourworldindata.org/grapher/oil-production-by-country?time=1946..latest&country=NOR~USA~GBR~Russian+Federation+%26+USSR~SAU~OWID_WRL~OPEC", height=450)

p.gridIFrame(1,0, "https://ourworldindata.org/grapher/oil-production-by-country?time=1946..latest&country=NOR~USA~GBR~Russian+Federation+%26+USSR~SAU~", height=450)

p.gridIFrame(1,1, "https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage?country=~OWID_WRL", height=450)




#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Annotations/Text")


#######################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Roundtable")

p.spanCenterImage("./Figures/roundtable.jpg", height=600)



########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Demonstration (e.g. experiment demo) with two different cameras")
# p.spanMyCamera(height=900)
p.leftMyCamera(height=500)
p.rightMyCamera(height=500)


'''
########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Interactivity!")

p.leftText(r"""

* Explore multi-parameter space in real time

* This example: Tranverse coherence length

* Adding different wavelengths.   
          
          """,fontSize=0.75)


p.rightIFrame("./Figures/Jinc2Col.html", height=1200)
'''


########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Combining Real-time Questions and Interactivity!")


p.leftText(r"""

* Do interactive figures enhance the learning experience?

* Instant feedback on what works.
          
          """,fontSize=0.75)

p.rightIFrame("./Figures/Jinc2Col.html", height=1200)




########################################
#############  New slide  ##############
########################################


p.newQuiz(#(a)
    questionText="For a collimated laser beam focused by a lens, the beam waist is...",
    answersText=[r"$({\rm a})$ ...upstream of the focal plane.",
                 r"$({\rm b})$ ...in the focal plane.",
                 r"$({\rm c})$ ...downstream of the focal plane."]
)

########################################
#############  New slide  ##############
########################################

p.newSlide()
p.title("Interactivity!")


p.spanCenterIFrame("./Figures/LensInteractive.html", height=1200)


########################################
#############  New slide  ##############
########################################


p.newQuiz(#(a)
    questionText="For a collimated laser beam focused by a lens, the beam waist is...",
    answersText=[r"$({\rm a})$ ...upstream of the focal plane.",
                 r"$({\rm b})$ ...in the focal plane.",
                 r"$({\rm c})$ ...downstream of the focal plane."]
)

########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("Summary: Caroline")

p.makeGrid(2,2)

p.gridText(0,0,r"""
* python $\rightarrow$ html

* webcams

* real-time interactivity

**Link**: https://github.com/nikolasibalic/Caroline

""", fontSize = 0.75) 

p.gridIFrame(0,1,"./Figures/timeline_qo.html",height=600)


p.gridIFrame(1,1, "https://ourworldindata.org/grapher/oil-production-by-country?time=1946..latest&country=NOR~USA~GBR~Russian+Federation+%26+USSR~SAU~", height=450)


########################################
############# QUIZ  ##############
########################################

'''

p.newQuiz(#(d)
    questionImage="",
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
############# QUIZ  ##############
########################################

p.newQuiz( # (c) (d) and (e)
    questionImage="",
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
    questionImage="",
    questionText=r"Photon pairs are prepared in the Bell state, \begin{eqnarray}\vert \Phi^+ \rangle & = &\frac{1}{\sqrt{2}}\left(\vert {\sf HH} \rangle+\vert {\sf VV} \rangle\right)\end{eqnarray} ",
    answersText=[
        r"$({\rm a})$ If Alice and Bob both measure in the same basis they sometimes get the same result.",
        r"$({\rm b})$ If Alice and Bob both measure in the same basis they always get the same result.",
        r"$({\rm c})$ If Alice and Bob measure in a different same basis they never get the same result.",
        r"$({\rm d})$ If Alice and Bob measure in a different same basis they sometimes get the same result.",
     ],
)

p.newQuiz(
    questionImage="",
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


'''
p.save("./Caroline_2024.html")




