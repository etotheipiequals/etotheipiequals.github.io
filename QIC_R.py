from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_R_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black


########################################
############# TITLE slide ##############
########################################

p.newSlide()
p.spanCenterText(r"""



** C. S. Adams**

**Quantum information and computing** 

** QIC.R Ph30, 14.00 Monday May 2, 2022 **

""", fontSize = 1.0)

p.leftText(r"""
* 1 Qubit
* 2 Bloch sphere
* 3 Density matrix
* 4 Rotations
* 5 Single-qubit gates
* 6 Decoherence
* 7 Ramsey interferometry
* 8 Bell
* 9 Two-qubit gates
* 10 Quantum circuits 
* 11 Atomic qubits
* 12 Light forces
* 13 Optical tweezer
* 14 Slowing and cooling
* 15 Optical pumpinh
* 16 Stim Raman
* 17 Rydberg blockade
* 18 Rydberg CNOT

""",fontSize=0.5)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.1 Qubit")
p.makeGrid(4,4)
p.gridText(0,2,r"""
Classical bit 0 or 1

Quantum bit 0 and 1
 
(but only if we do not look!)
""", fontSize = 0.5)
p.gridImage(0,3,"./Figures/Bit_vs_Qubit.JPG", height = 100)
p.gridText(1,2,r"""
** $\vert \psi\rangle = a \vert 0 \rangle + b \vert 1 \rangle$ **
""", fontSize = 0.5)
p.gridImage(1,3,"./QIC_Figures/QIC1_qubit.png", height = 100)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.2 DiVinenzo and Bloch")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC2_Bloch_2.png", height = 400)


########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.3 Density matrix")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/BlochDM_theta_phi.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.4 Rotations")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/BlochDM_Hxz.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.5 Rabi and Hadamard")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC4_EMfield+qubit.png", height = 400)
p.gridImage(1,2,"./QIC_Figures/QIC5_Sr_Rabi_oscillation_1.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.6 Decoherence")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/BlochDM_T2.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.7 Ramsey")
p.makeGrid(3,3)
p.gridImage(0,2,"./Figures/Ramsey_static.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.8 Bell")
p.makeGrid(3,3)
p.gridImage(0,2,"./Figures/Bell_irrotational.JPG", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.9 Two-qubit gates")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC9_CNOT_CZ.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.10 Quantum circuits")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC10_delayed_choice_quantum_eraser_circuit.png", height = 400)


########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.11 Atomic qubits")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC11_Cs_energy_levels_2.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.12 Light forces")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC12_light_forces_1.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.13 Optical tweezers")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC13_tweezer_static.png", height = 400)


########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.14 Slowing and cooling")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC14_Sr_sideband_2018.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.15 Optical pumping")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC15_optical_pumping_3.png", height = 400)
p.gridImage(1,2,"./QIC_Figures/QIC15_optical_pumping_4.png", height = 400)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.16 Stimulated Raman")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC16_Raman_2.png", height = 240)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.17 Rydberg blockage")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC17_Blockade_1.png", height = 240)
p.gridImage(1,2,"./QIC_Figures/QIC17_Blockade_4.png", height = 240)

########################################
#############  New slide  ##############
########################################
p.newSlide()
p.title("QIC.18 Rydberg CNOT")
p.makeGrid(3,3)
p.gridImage(0,2,"./QIC_Figures/QIC18_pulse_234.png", height = 400)


p.save("./QIC_R.html")


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
