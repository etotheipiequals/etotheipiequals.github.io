from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/QIC_Caroline/Climate.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

########################################
p.newSlide()
p.title("**The trouble with history?**")

p.leftImage( "./Figures/Population.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)


p.rightText(r"""

* What is amazing?

""",fontSize=1.0)

########################################
p.newSlide()
p.title("**The trouble with history?**")

p.leftImage( "./Figures/Population.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)


p.rightText(r"""

* What is amazing?

* Factor of 10 every 3000 years.

""",fontSize=1.0)



########################################
p.newSlide()
p.title("**The trouble with history?**")

p.leftImage( "./Figures/Population.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)


p.rightText(r"""

* What is amazing?

* Factor of 10 every 3000 years.

* After 1800, factor of 10 in 200 years. Why?  

""",fontSize=1.0)

########################################
p.newSlide()
p.title("**The trouble with history?**")

p.leftImage( "./Figures/Population.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)


p.rightText(r"""

* What is amazing?

* Factor of 10 every 3000 years.

* After 1800, factor of 10 in 200 years. Why?  

* *It is doubtful whether Homo sapiens will still be around a thousand years from now*, YN Harari, *Sapiens*, p.7, 2011.

""",fontSize=1.0)


########################################
p.newSlide()
p.title("**What else was changing?**")

p.leftImage( "./Figures/PopulationCO2.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)


p.rightText(r"""

* Blue: Ice Core data http://ncdc.noaa.gov/paleo/study/17975

* Purple: Atmospheric measurements

""",fontSize=1.0)


########################################
p.newSlide()
p.title("The trouble with economics")
p.makeGrid(3,2)
p.gridImage(0,0, "./Figures/Candle.jpg", height=200, textBelow = r"""Candle 5 to 80 W (of which 4 W is light)""",fontSize=0.5)

p.gridImage(0,1, "./Figures/Millet.jpg", height=200, textBelow = r"""Man with a Hoe, Jean-Francois Millet1862 Getty Museum, https://www.getty.edu/art/collection/object/103RGZ""",fontSize=0.5)

p.gridText(2,1, r"""Human 100 W. Short bursts up to a few hundred. 2000 calories $=$ 8.4 million Joles divide by 24 hours and 3600 second per hour given 100 W""",fontSize=0.5)

########################################
p.newSlide()
p.title("The trouble with economics")
p.makeGrid(3,2)
p.gridImage(0,0, "./Figures/PloughEgypt.jpg", height=100, textBelow = r"""https://www.britannica.com/technology/plow""",fontSize=0.5)

p.gridImage(0,1, "./Figures/PloughModern.jpg", height=200, textBelow = r"""https://blog.oliver-meili.name/""",fontSize=0.5)

p.gridText(2,1, r"""Ox 350 W. Two oxen $=$ A horse   Horse power 746 W""",fontSize=0.5)



########################################
p.newSlide()
p.title("The trouble with economics")
p.makeGrid(3,2)
p.gridImage(0,0, "./Figures/Killhope.jpg", height=200, textBelow = r"""Water Wheels 2-200 kW

Killhope Wheel https://live.staticflickr.com/4383/36796080161_21a6e8e77c_b.jpg""",fontSize=0.5)

p.gridImage(0,1, "./Figures/Smil.jpg", height=200, textBelow = r"""Energy and Civilisation: A history MIT Press 2017""",fontSize=0.5)

#p.gridText(2,1, r"""Ox 350 W. Two oxen $=$ A horse   Horse power 746 W""",fontSize=0.5)


########################################
p.newSlide()
p.title("The trouble with economics")
p.makeGrid(3,2)
p.gridImage(0,0, "./Figures/Watt1788.jpg", height=200, textBelow = r"""
Newcomen 1712 3.75kW
Watt 1788 https://www.britannica.com/technology/rotative-engine 
Watt 1795 20kW 
Watt 1800 100 kW""",fontSize=0.5)

p.gridImage(0,1, "./Figures/CalderHall1956.jpg", height=200, textBelow = r"""Calder Hall 4$\times$ 60 MHz $=$ 240 MW""",fontSize=0.5)

#p.gridText(2,1, r"""Ox 350 W. Two oxen $=$ A horse   Horse power 746 W""",fontSize=0.5)


########################################
#p.newSlide()
#p.title("Where does the energy come from?")
#p.makeGrid(3,2)
#p.gridImage(0,0, "./Figures/EnergyConsumptionBySource.png", height=200, textBelow = r"""
#""",fontSize=0.5)

#p.gridImage(0,1, "./Figures/CalderHall1956.jpg", height=200, textBelow = r"""Calder Hall 4$\times$ 60 MHz $=$ 240 MW""",fontSize=0.5)

#p.gridText(2,1, r"""Ox 350 W. Two oxen $=$ A horse   Horse power 746 W""",fontSize=0.5)

########################################
p.newSlide()
p.title("Where does the energy come from?")
p.spanCenterImage( "./Figures/EnergyConsumptionBySource.png", height=400, textBelow = r"""
About 80% fossil energy.""",fontSize=0.5)

########################################
p.newSlide()
p.title("Who did it?")
p.spanCenterImage( "./Figures/EmissionsSelectedCountries.png", height=600, textBelow = r"""
""",fontSize=0.5)

########################################
p.newSlide()
p.title("Who did it?")
p.spanCenterImage( "./Figures/EmissionsPerCapita.png", height=600, textBelow = r"""
""",fontSize=0.5)



########################################
p.newSlide()
p.title("World Trade")
p.makeGrid(3,2)
p.gridImage(0,0, "./Figures/ExportTrade.png", height=200, textBelow = r"""
""",fontSize=0.5)

#p.gridImage(0,1, "./Figures/CalderHall1956.jpg", height=200, textBelow = r"""Calder Hall 4$\times$ 60 MHz $=$ 240 MW""",fontSize=0.5)

#p.gridText(2,1, r"""Ox 350 W. Two oxen $=$ A horse   Horse power 746 W""",fontSize=0.5)




########################################
p.newSlide()
p.title("Historic emissions")
p.makeGrid(3,3)
p.gridImage(0,1, "./Figures/CarbonBriefHistoric.jpg", height=450, textBelow = r"""https://www.carbonbrief.org/analysis-which-countries-are-historically-responsible-for-climate-change""",fontSize=0.5)



########################################
p.save("./Climate.html")

