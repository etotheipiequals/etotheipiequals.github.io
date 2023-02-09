from caroline import Presentation

p = Presentation(
#    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/OWID_plots_1.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)


########################################
p.newSlide()
p.title("OWID plots")
p.makeGrid(2,2)
#p.gridIFrame(0,0, "https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?facet=none&hideControls=True", height=450)
p.gridIFrame(0,0, "https://ourworldindata.org/grapher/global-energy-substitution?country=~OWID_WRL", height=450)



p.gridIFrame(0,1, "https://ourworldindata.org/grapher/covid-deaths-per-million-exemplars?country=USA~GBR~HKG~NZL~DEU~TWN~AUS~?facet=none&hideControls=True", height=450)

#p.gridIFrame(1,0, "https://ourworldindata.org/grapher/oil-production-by-country?time=1946..latest&country=NOR~USA~GBR~Russian+Federation+%26+USSR~SAU~OWID_WRL~OPEC", height=450)

p.gridIFrame(1,0, "https://ourworldindata.org/grapher/oil-production-by-country?time=1946..latest&country=NOR~USA~GBR~Russian+Federation+%26+USSR~SAU~", height=450)

p.gridIFrame(1,1, "https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage?country=~OWID_WRL", height=450)


########################################
p.newSlide()
p.title("Global Energy")

p.spanIFrame("https://ourworldindata.org/grapher/global-energy-substitution?country=~OWID_WRL", height=950)

########################################
p.newSlide()
p.title("Global Energy")

p.spanIFrame("https://ourworldindata.org/grapher/oil-production-by-country?time=1946..latest&country=NOR~USA~GBR~Russian+Federation+%26+USSR~SAU~", height=950)



########################################
p.newSlide()
p.title("Covid-deaths-per-million")

p.spanIFrame("https://ourworldindata.org/grapher/covid-deaths-per-million-exemplars?country=USA~GBR~HKG~NZL~DEU~TWN~AUS~?facet=none&hideControls=True", height=950)

########################################
p.newSlide()
p.title("Cost of computer memory and storage")

p.spanIFrame("https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage?country=~OWID_WRL", height=950)




########################################
p.save("./OWID_plots_1.html")

