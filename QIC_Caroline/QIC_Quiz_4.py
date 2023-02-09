from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/QIC_Quiz_4_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QIC Quiz 4: Single-qubit rotations and Rabi oscillations **")

p.leftIFrame("./QIC_Figures/BlochDM_Ry.html", height = 800, textBelow=r"Rotation about $y$ axis: Bloch vector (blue). Rotation axis (yellow).", fontSize = 0.5)

p.rightIFrame("./QIC_Figures/BlochDM_Rz.html", height = 800, textBelow=r"Rotation about $z$ axis: Bloch vector (blue). Rotation axis (yellow).", fontSize = 0.5)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_ny.png",
    questionText=r"$1.$ For the rotation shown, what are the components of the rotation axis? $[1~{\rm mark}]$ [Hint: Remember that $z$ is vertical and $x$ points towards you.]", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_ny.png",
    questionText=r"$1.$ $[{\rm SOLUTION}] ~ ({\rm b})$.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}  $[{\rm CORRECT}]$",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nz.png",
    questionText=r"$2.$ For the rotation shown, what are the components of the rotation axis? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nz.png",
    questionText=r"$2.$ $[{\rm SOLUTION}] ~ ({\rm c})$.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}  $[{\rm CORRECT}]$",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nxnz.png",
    questionText=r"$3.$ For the rotation shown, what are the components of the rotation axis? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nxnz.png",
    questionText=r"$3.$ $[{\rm SOLUTION}] ~ ({\rm e})$.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}  $[{\rm CORRECT}]$",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nynz.png",
    questionText=r"$4.$ For the rotation shown, what are the components of the rotation axis? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)


p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nynz.png",
    questionText=r"$4.$ $[{\rm SOLUTION}] ~ ({\rm f})$.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray} $[{\rm CORRECT}]$",
    ],
)



########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_ny.png",
    questionText=r"$5.$ For the rotation shown (from red dot to red dot), what is the rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_ny.png",
    questionText=r"$5.$ $[{\rm SOLUTION}] ~ ({\rm c})$.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray} $[{\rm CORRECT}]$",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_pi3.png",
    questionText=r"$6.$ For the rotation shown (from red dot to red dot), what is the rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_pi3.png",
    questionText=r"$6.$ $[{\rm SOLUTION}] ~ ({\rm a})$", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray} $[{\rm CORRECT}]$",
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
    questionImage="./QIC_Figures/R_3pi2.png",
    questionText=r"$7.$ For the rotation shown, what is the rotation angle, $\Theta$? [1 mark]", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_3pi2.png",
    questionText=r"$7.$ $[{\rm SOLUTION}] ~ ({\rm d})$. The key point here is to remember the right-hand rule for rotations.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray} $[{\rm CORRECT}]$",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nxnz.png",
    questionText=r"$8.$ For the rotation shown, what is the rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{3\pi}{2}\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{\pi}{4}\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nxnz.png",
    questionText=r"$8.$ $[{\rm SOLUTION}] ~ ({\rm c})$", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{\pi}{3}\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{\pi}{2}\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \pi\end{eqnarray} $[{\rm CORRECT}]$",
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
    questionText=r"$9.$ The blue line (average of the red measurement data) shows the simulated dymanics of a qubit driven by a noisey field. What is the total rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 4\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 6\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 16\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC5_rabi_oscillation_noisey_1.png",
    questionText=r"$9.$ $[{\rm SOLUTION}] ~ ({\rm d})$. The qubit makes three complete rotations around the $y$-axis.", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 4\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 6\pi\end{eqnarray} $[{\rm CORRECT}]$",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 16\pi\end{eqnarray}",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC5_rabi_oscillation.png",
    questionText=r"$10.$ For the Rabi oscillations shown, what is the total qubit rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 9\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 10\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 16\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 18\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 20\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/QIC5_rabi_oscillation.png",
    questionText=r"$10.$ $[{\rm SOLUTION}] ~ ({\rm b})$", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 9\pi\end{eqnarray} $[{\rm CORRECT}]$",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 10\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 11\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 19\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 21\pi\end{eqnarray}",
    ],
)


########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_4pi.png",
    questionText=r"$11.$ For qubit dynamics shown, what is the qubit rotation angle, $\Theta$? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 4\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 6\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 16\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_4pi.png",
    questionText=r"$11.$ $[{\rm SOLUTION}] ~ ({\rm c})$ The Bloch vector completes two full rotations about the $z$ axis.""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & 2\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & 4\pi\end{eqnarray} $[{\rm CORRECT}]$",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & 6\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & 8\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & 16\pi\end{eqnarray}",
    ],
)

########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/Rabi_oscillations_electrons.png",
    questionText=r"$12.$ For the Rabi oscillations shown [Ref: https://arxiv.org/abs/2111.11937], what is the qubit rotation angle, $\Theta$, on resonance, at $t=2.0~\mu$s? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{19}{2}\pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{21}{2}\pi\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \frac{23}{2}\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{25}{2}\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{27}{2}\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & \frac{29}{2}\pi\end{eqnarray}",
    ],
)

p.newQuiz(#(c)
    questionImage="./QIC_Figures/Rabi_oscillations_electrons.png",
    questionText=r"$12.$ $[{\rm SOLUTION}] ~ ({\rm b})$ The qubit has completed five (five dark bands) and a quarter rotations, $5\times 2\pi + \pi/2 = (21/2)\pi$.""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} \Theta & = & \frac{19}{2}\pi\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}\Theta & = & \frac{21}{2}\pi\end{eqnarray} $[{\rm CORRECT}]$",
        r"$({\rm c})$ \begin{eqnarray}\Theta & = & \frac{23}{2}\pi\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}\Theta & = & \frac{25}{2}\pi\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}\Theta & = & \frac{27}{2}\pi\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}\Theta & = & \frac{29}{2}\pi\end{eqnarray}",
    ],
)


p.save("./QIC_Quiz_4.html")

'''
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



########################################
############# QUIZ  ##############
########################################

p.newQuiz(#(c)
    questionImage="./QIC_Figures/R_nx.png",
    questionText=r"$5.$ For the rotation shown, what are the components of the rotation axis? [1 mark]""", fontSize=0.8,
    answersText=[
        r"$({\rm a})$ \begin{eqnarray} (n_x,n_y,n_z) & = & (1,0,0)\end{eqnarray}",
        r"$({\rm b})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,1,0)\end{eqnarray}",
        r"$({\rm c})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,0,1)\end{eqnarray}",
        r"$({\rm d})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}},0)\end{eqnarray}",
        r"$({\rm e})$ \begin{eqnarray}(n_x,n_y,n_z)=(\textstyle{1\over\sqrt{2}},0,\textstyle{1\over\sqrt{2}})\end{eqnarray}",
        r"$({\rm f})$ \begin{eqnarray}(n_x,n_y,n_z)=(0,\textstyle{1\over\sqrt{2}},\textstyle{1\over\sqrt{2}})\end{eqnarray}",
    ],
)


