from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/OWID_plots_1.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("Examples of Interactive Figures")
p.makeGrid(2,3)
p.gridIFrame(0,0, "https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?facet=none&hideControls=True", height=450)
p.gridIFrame(0,1, "./QIC_Figures/Life_Expectancy_GDP_linear.html", height=450)
p.gridIFrame(0,2, "./QIC_Figures/Tweezer_interactive.html", height=450)

p.gridIFrame(1,1, "./QIC_Figures/BlochDM_T2_landscape.html", height=450)


########################################
p.save("./OWID_plots_1.html")

