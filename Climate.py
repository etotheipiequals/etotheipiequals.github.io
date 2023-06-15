from caroline import Presentation

p = Presentation(
    logo="./Figures/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/Climate_audience.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)


########################################
p.newSlide()
p.title("**Is science sustainable?**")
p.spanCenterImage( "./Figures/Apocalypse.jpg", height=600, textBelow = r"""
*Our house is on fire*, Greta Thunberg, 25 January, 2019. 
""",fontSize=0.5)

########################################
p.newSlide()
p.title("*Our house is on fire*, we knew it, we have known for 50 years")
p.spanCenterImage( "./Figures/keeling_decadal.png", height=600, textBelow = r"""
https://etotheipiequals.github.io/Climate_Book/Keeling_curve.html
""",fontSize=0.5)

########################################
p.newSlide()
p.title("**Technology, ideology, and market failure**")

p.makeGrid(2,2)

p.gridImage(0,0, "./Figures/F150_3.png", height=240, textBelow = r"""
Ford F150 Lightning""",fontSize=0.5)

p.gridImage(0,1, "./Figures/F150_4.png", height=240, textBelow = r"""
130 kWh""",fontSize=0.5)

p.gridImage(1,0, "./Figures/F150_2.png", height=240, textBelow = r"""
300 miles""",fontSize=0.5)

p.gridImage(1,1, "./Figures/F150_1.png", height=240, textBelow = r"""
3 tonnes""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Emissions inequality**")


p.leftImage("./Figures/Carbon_Inequality_Bruckner.png", height=480, textBelow = r"""
 
""",fontSize=0.5)
p.rightImage("./Figures/Carbon_Inequality_Chancel_1.png", height=480, textBelow = r"""
 
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Emissions inequality**")

p.spanCenterImage("./Figures/EmissionInequalityUS.png", height=480, textBelow = r"""
 
""",fontSize=0.5)

########################################
p.newSlide()
p.title("**Remaing carbon budget: simplified**")
p.spanCenterImage("./Figures/T_emission.png", height=480, textBelow = r"""
280 Gt: **35 tonnes each!**
""",fontSize=1.0)

########################################
p.newSlide()
p.title("**Car usage in London**")

p.spanCenterImage("./Figures/car_usage.png", height=600, textBelow = r"""
Nature Commun. **14**, 2357 (2023). https://www.nature.com/articles/s41467-023-37728-x
""",fontSize=0.5)










########################################
p.newSlide()
p.title("*Is it bad?*")
p.leftImage( "./Figures/FT2020.png", height=600, textBelow = r"""
""",fontSize=0.5)

########################################
p.newSlide()
p.title("*Is it bad?*")
p.leftImage( "./Figures/FT2020.png", height=600, textBelow = r"""
""",fontSize=0.5)

p.rightImage( "./Figures/FT2070.png", height=600, textBelow = r"""
""",fontSize=0.5)




########################################
p.newSlide()
p.title("**Non-linearity: feedback loops**")
p.leftImage( "./Figures/T_emission.png", height=500, textBelow = r"""
""",fontSize=0.5)

p.rightImage( "./Figures/FeedbackLoops.png", height=500, textBelow = r"""
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**It's happening now?**")
p.spanCenterImage( "./Figures/SST.png", height=720, textBelow = r"""
""",fontSize=0.5)

########################################
p.newSlide()
p.title("**It's happening now!**")
p.spanCenterImage( "./Figures/RadiativeForcing2023.png", height=500, textBelow = r"""
P. M. Forster et al.

Indicators of Global Climate Change 2022: annual update


Earth Syst. Sci. Data, **15**, 2295, 2023,
""",fontSize=0.5)

'''



########################################
p.newSlide()
p.title("**Population and CO2: NOT too many people!**")
p.spanCenterImage( "./Figures/PopulationCO2.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)




########################################
p.newSlide()
p.title("**Emissions inequality**")

p.spanCenterImage( "./Figures/CarbonBriefHistoric.jpg", height=480, textBelow = r"""
""",fontSize=0.5)




########################################
p.newSlide()
p.title("**Technology, ideology, and market failure**")

p.makeGrid(2,2)

p.gridImage(0,0, "./Figures/F150_3.png", height=240, textBelow = r"""
Ford F150 Lightning""",fontSize=0.5)

p.gridImage(0,1, "./Figures/F150_4.png", height=240, textBelow = r"""
130 kWh""",fontSize=0.5)

p.gridImage(1,0, "./Figures/F150_2.png", height=240, textBelow = r"""
300 miles""",fontSize=0.5)

p.gridImage(1,1, "./Figures/F150_1.png", height=240, textBelow = r"""
3 tonnes""",fontSize=0.5)

'''







########################################
p.newSlide()
p.title("**Self-declared CLIMATE EMERGENCY March 26, 2019**")

########################################
p.newSlide()
p.title("**Self-declared CLIMATE EMERGENCY March 26, 2019**")


p.makeGrid(4,2)


p.gridText(0,0,  r""" * Sustainability""",fontSize=1.0)

p.gridImage(1,0, "./Figures/SolarPanels.png", height=320, textBelow = r"""
""",fontSize=1.0)


p.gridText(0,1,  r""" * Data""",fontSize=1.0)

p.gridImage(1,1,"./Figures/SolarData.jpg", height=360, textBelow = r"""
March 17, 2023
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**What does CLIMATE EMERGENCY mean for a physicist?**")

p.makeGrid(4,2)


p.gridText(0,0,  r""" * Sustainability""",fontSize=1.0)

p.gridImage(1,0, "./Figures/PhysicsWorld_2019.png", height=320, textBelow = r"""
""",fontSize=1.0)


p.gridText(0,1,  r""" * Teaching innovation""",fontSize=1.0)

p.gridImage(1,1,"./Figures/Opticsf2f_CodeBook.png", height=360, textBelow = r"""
 https://opticsf2f.github.io/Opticsf2f_CodeBook/
""",fontSize=0.5)



#######################################
p.newSlide()
p.title(r"**Optics $f$2$f$: From Fourier to Frensel**")
p.spanCenterImage( "./Figures/Opticsf2f.jpg", height=600, textBelow = r"""
""",fontSize=0.5)

########################################
############# QUIZ  ##############
########################################


p.newQuiz(#
    questionImage="./Figures/fourier.png",
    questionText=r"**Q.** What does Fourier's law describe?",
    answersText=[
        r"$({\rm a})$ Mathematics.",
        r"$({\rm b})$ Heat.",
        r"$({\rm c})$ Optics.",
        r"$({\rm d})$ The Moon.",
    ],
)


########################################
p.newSlide()
p.title("**Fourier's law**")

p.leftImage( "./Figures/fourier.png", height=600, textBelow = r"""

""",fontSize=0.5)


p.rightText(r"""

* $\Delta Q = U~A~\Delta T$

* $U$ is a thermal conductance (reciprocal of thermal resistance.

* $U$ has unit of Wm$^{-2}$K$^{-1}$.

* U - values!

""",fontSize=1.0)



########################################
p.newSlide()
p.title("**Fourier's greenhouse papers: 1822-27**")
p.makeGrid(4,2)
p.gridImage(0,0, "./Figures/fourier.png", height=200, textBelow = r"""
""",fontSize=0.5)


p.gridImage(1,0, "./Figures/Fourier1827_1.png", height=200, textBelow = r"""
 
""",fontSize=0.5)
p.gridImage(2,0, "./Figures/Fourier1827_2.png", height=200, textBelow = r"""
 
""",fontSize=0.5)
p.gridImage(1,1, "./Figures/Fourier1827_3.png", height=200, textBelow = r"""
 
""",fontSize=0.5)
p.gridImage(2,1, "./Figures/Fourier1827_4.png", height=200, textBelow = r"""
 
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Bougier-Lambert-Beer law**")

p.leftText(r"""

* $I  = I_0 {\rm e} ^{-N\sigma z}$


* $N$ number density of absorbers

* $$\sigma_j = \frac{S_j}{\pi}\frac{\gamma_j}{(\omega_j-\omega_0)^2 + \gamma_j^2}$$

* Many different $j$s.

""",fontSize=1.0)


p.rightImage( "./Figures/beer_colour.png", height=500, textBelow = r"""
""",fontSize=0.5)

########################################
p.newSlide()
p.title("**Bougier-Lambert-Beer law**")

p.leftText(r"""

* $I  = I_0 {\rm e} ^{-N\sigma z}$


* $N$ number density of absorbers

* $$\sigma_j = \frac{S_j}{\pi}\frac{\gamma_j}{(\omega_j-\omega_0)^2 + \gamma_j^2}$$

* Many different $j$s.

""",fontSize=1.0)


p.rightImage( "./Figures/PQR.png", height=500, textBelow = r"""
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Spectrum of the Earth**")
p.spanCenterImage( "./Figures/High_Resolution_CO2.png", height=500, textBelow = r"""
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Spectrum of the Earth**")
p.spanCenterImage( "./Figures/Pierrehumbert_Phys_Today_2011.png", height=500, textBelow = r"""
*Infrared radiation and planetary temperature*,
Raymond T. Pierrehumbert, Phys. Today **64**, 1, 33 (2011).""",fontSize=0.5)



########################################
p.newSlide()
p.title("**What future will we choose?**")
p.spanCenterImage( "./Figures/T_emission.png", height=500, textBelow = r"""
""",fontSize=0.5)





########################################
p.newSlide()
p.title("**What future will we choose? Not physics? Sociophysics? Or Systems modelling**")

p.leftImage( "./Figures/Population.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)



########################################
p.newSlide()
p.title("**Past performance is not a guide to the future?**")

p.leftImage( "./Figures/Population.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)


p.rightText(r"""

* Knap of Howar -3600 CE, 10M

* Khafre pyramid, Giza -2600 CE, 20 M

* x10 every 3000 years. After 1800, x10 in 200 years. 

* Hyperbolic growth: Why?  

* *It is doubtful whether Homo sapiens will still be around a thousand years from now*, YN Harari, *Sapiens*, p.7, 2011.

""",fontSize=1.0)



########################################
p.newSlide()
p.title("**Systems modelling: Extended Korotayev model**")
p.spanCenterImage( "./Figures/Korotayev.png", height=600, textBelow = r"""
See also *The limits to growth*, Donella H. Meadows, Dennis L. Meadows, Jorgen Randers, William W. Behrens III, 1972
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Is science sustainable?**")

p.leftImage( "./Figures/Apocalypse.jpg", height=600, textBelow = r"""
""",fontSize=0.5)


p.rightText(r"""

* No!

* What can we do?

* Change ...

* Change ...

* Change ...

* Science ...

""",fontSize=1.0)


########################################
p.newSlide()
p.title("**Interdisciplinarity**")
p.spanCenterImage( "./Figures/Adnan.png", height=600, textBelow = r"""Adnan Jinnah, MSci project report 2023.
Collaboration with Phil Stevens and Steve Willis in Biosciences at Durham.
""",fontSize=0.5)

########################################
p.newSlide()
p.title("**Is science sustainable?**")

p.leftImage( "./Figures/Apocalypse.jpg", height=600, textBelow = r"""
""",fontSize=0.5)


p.rightText(r"""

* No!

* What can we do?

* Change how we behave

* Change how we teach: physics of climate

* Change how we do research: interdisciplinarity

* Science ...
""",fontSize=1.0)

########################################
p.newSlide()
p.title("**Is science sustainable?**")

p.leftImage( "./Figures/Apocalypse.jpg", height=600, textBelow = r"""
""",fontSize=0.5)


p.rightText(r"""

* No!

* What can we do?

* Change how we behave

* Change how we teach: physics of climate

* Change how we do research: interdisciplinarity

* Science can still be around 1000 years from now!

""",fontSize=1.0)





########################

######### TALK ENDS

########################











'''
########################################
p.newSlide()
p.title("**Something's going on?**")
p.spanCenterImage( "./Figures/ice_core.png", height=600, textBelow = r"""
Data from ice cores (blue) and atmospheric measurements (red).
""",fontSize=0.5)
'''













########################################
p.newSlide()
p.title("**Something's going on**")
p.spanCenterImage( "./Figures/CO2withoutPop.png", height=600, textBelow = r"""
Data from ice cores (blue) and atmospheric measurements (red).
""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Atmospheric CO2 and temperature**")
p.spanCenterImage( "./Figures/T_emission.png", height=500, textBelow = r"""
""",fontSize=0.5)















########################################
p.newSlide()
p.title("**Mistake 2: Blaming someone else**")
p.makeGrid(2,2)
p.gridImage(0,0, "./Figures/CarbonBriefHistoric.jpg", height=600, textBelow = r"""
""",fontSize=0.5)


#p.gridImage(0,1, "./Figures/Carbon_Inequality_Chancel_1.png", height=400, textBelow = r"""Lucas Chancel, *Global carbon inequality over 1990–2019* Nature Sustainability **5**, 931 (2022). """,fontSize=0.5)



########################################
p.newSlide()
p.title("**Mistake 2: Blaming someone else**")
p.makeGrid(2,2)
p.gridImage(0,0, "./Figures/CarbonBriefHistoric.jpg", height=600, textBelow = r"""
""",fontSize=0.5)


p.gridImage(0,1, "./Figures/HistoricalEmissions.png", height=600, textBelow = r"""
 
""",fontSize=0.5)



########################################
p.newSlide()
p.title("**It's what we do next that counts.**")
p.spanCenterImage( "./Figures/T_emission.png", height=500, textBelow = r"""
""",fontSize=0.5)

########################################
p.newSlide()
p.title("**Keeping 1.5 alive?: 1.5 is a proxy for bad things**")

p.makeGrid(2,2)
p.leftImage("./Figures/T_emission.png", height=400, textBelow = r"""CSA
""",fontSize=0.5)


p.rightImage("./Figures/BurningEmberOceans.png", height=400, textBelow = r"""
**Burning embers: towards more
transparent and robust climate-​change
risk assessments**, Nature Reviews Earth Environment **1**, 516 (2020)""",fontSize=0.5)


########################################
p.newSlide()
p.title("**1.5 is a proxy for bad things: non-linearity**")


p.leftImage("./Figures/T_emission.png", height=400, textBelow = r"""CSA
""",fontSize=0.5)


p.rightImage("./Figures/FeedbackLoops.png", height=400, textBelow = r"""Ripple et al,
*Many risky feedback loops amplify the need for climate action*, One Earth, **6**, 86 (2023).
DOI:https://doi.org/10.1016/j.oneear.2023.01.004""",fontSize=0.5)

########################################
p.newSlide()
p.title("**1.5 is a proxy for bad things: non-linearity**")


p.leftImage("./Figures/T_emission.png", height=400, textBelow = r"""CSA
""",fontSize=0.5)


p.rightImage("./Figures/SeaLevelRise.png", height=400, textBelow = r""" Total melt, Green + Antartica 70 m. 1000s of years, but sudden collapse of Antartic Ice Shelf.""",fontSize=0.5)



########################################
p.newSlide()
p.title("**It's what we do now that counts**")


p.leftImage("./Figures/T_emission.png", height=400, textBelow = r"""CSA
""",fontSize=0.5)


p.rightImage("./Figures/CarbonBudget2023.png", height=400, textBelow = r"""Forster et al,
https://www.carbonbrief.org/guest-post-what-the-tiny-remaining-1-5c-carbon-budget-means-for-climate-policy/""",fontSize=0.5)


p.newSlide()
p.title("**260 Gt = 35 tonnes per capita**")

p.spanCenterText(r"""

* 1 flight 1 t 

* 1 year eating meat 1 t 

* 1 SUV EV 10 t

""",fontSize=1.0)


########################################
p.newSlide()
p.title("**It's what we do next that counts.**")
p.spanCenterImage( "./Figures/CarbonInqualityChancel_1.png", height=600, textBelow = r"""
Population data from https://www.gapminder.org/data/documentation/gd003/
""",fontSize=0.5)



########################################
p.newSlide()
p.title("**We the high emitters**")

p.spanCenterText(r"""

* We know what to do, 

* We know how to do it, 

* We have the resources to do it, 


but we don't want to.

""",fontSize=1.0)





########################################
p.newSlide()
p.title("Who did it?")
p.spanCenterImage( "./Figures/EmissionsPerCapita.png", height=600, textBelow = r"""
""",fontSize=0.5)






########################################
p.newSlide()
p.title("**'Mainstream' economics: academic crime**")
p.spanCenterImage( "./Figures/AgricultureGDP.png", height=600, textBelow = r"""*economic development and technological change tend progressively to reduce climate sensitivity as the share of agriculture in output and employment declines*, 

W. D. Nordhaus, *Reflections on the economics of climate change*. Journal of Economic Perspectives, 7, 11 (1993).""",fontSize=0.5)


########################################
p.newSlide()
p.title("**'Mainstream' economics: academic crime**")
p.spanCenterIFrame( "https://ourworldindata.org/grapher/gdp-vs-agriculture-gdp", height=600, textBelow = r"""*economic development and technological change tend progressively to reduce $\bbox[2px, border: 2px solid red]{\rm climate~sensitivity~as}$ the share of agriculture in output and employment declines*, 

W. D. Nordhaus, *Reflections on the $\bbox[2px, border: 2px solid red]{\rm economics~of~climate~change}$*. Journal of Economic Perspectives, 7, 11 (1993).""",fontSize=0.5)



########################################
p.newSlide()
p.title("OWID plots")
p.makeGrid(2,2)
#p.gridIFrame(0,0, "https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?facet=none&hideControls=True", height=450)
p.gridIFrame(0,0, "https://ourworldindata.org/grapher/global-energy-substitution?country=~OWID_WRL", height=450)



########################################
p.newSlide()
p.title("**Technology and market failure**")

p.spanCenterText(r"""

* We, the high emitters, know what we must do, we have the resources to do it, but we don't want to do it.

""",fontSize=1.0)


########################################
p.newSlide()
p.title("**Technology and market failure**")

p.makeGrid(2,2)

p.gridImage(0,0, "./Figures/F150_3.png", height=320, textBelow = r"""
130 kWh""",fontSize=0.5)

p.gridImage(0,1, "./Figures/F150_4.png", height=320, textBelow = r"""
130 kWh""",fontSize=0.5)

p.gridImage(1,0, "./Figures/F150_2.png", height=240, textBelow = r"""
320 miles""",fontSize=0.5)

p.gridImage(1,1, "./Figures/Fig150_1.png", height=240, textBelow = r"""
3 tonnes""",fontSize=0.5)


########################################
p.newSlide()
p.title("**Technology and market failure**")

p.makeGrid(2,2)

p.gridImage(0,0, "./Figures/LithiumDemand.png", height=320, textBelow = r"""
From https://about.bnef.com/blog/will-the-real-lithium-demand-please-stand-up-challenging-the-1mt-by-2025-orthodoxy/
""",fontSize=0.5)

p.gridImage(0,1, "./Figures/LithiumDemand.png", height=320, textBelow = r"""
From https://about.bnef.com/blog/will-the-real-lithium-demand-please-stand-up-challenging-the-1mt-by-2025-orthodoxy/
""",fontSize=0.5)

p.gridImage(1,0, "./Figures/LithiumDemand.png", height=240, textBelow = r"""
From https://about.bnef.com/blog/will-the-real-lithium-demand-please-stand-up-challenging-the-1mt-by-2025-orthodoxy/
""",fontSize=0.5)

p.gridImage(1,1, "./Figures/LithiumDemand.png", height=240, textBelow = r"""
From https://about.bnef.com/blog/will-the-real-lithium-demand-please-stand-up-challenging-the-1mt-by-2025-orthodoxy/
""",fontSize=0.5)




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

p.gridText(2,1, r"""

* Modern Human: Survival need: 100 W. 2000 calories $=$ 8.4 million Joles divide by 24 hours and 3600 second per hour gives 100 W. Short bursts up 1 kW.

* Human consumption: Banglasdesh 300 W, UK/China  3 kW, US 9 kW

* Almost all modern humans rely on the energy surplus created elsewhere.

 """,fontSize=0.5)
 
 ########################################
p.newSlide()
p.title("Energy per capita")
p.makeGrid(2,2)
p.gridText(0,0, r"""1 W = 8.77 kWh per annum""", fontSize=0.5)

p.gridIFrame(0,1, "https://ourworldindata.org/grapher/per-capita-energy-use?tab=chart&time=earliest..2019&country=USA~BGD~GBR~CHN~TCD~ISL", height=800)



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

