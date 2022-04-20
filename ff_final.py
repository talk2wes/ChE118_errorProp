#Wesley Johanson
from re import I
import ChE
import numpy as np

#USER PARAMETERS
_filename = "x.csv"
#Data labels
labels = np.loadtxt(_filename, unpack=True, delimiter=',',dtype=str)[:, 0]	
savePlotAs = "plot.png"
folder = "IMG/"

# regressionVars = [0] #Variables to calculate Linear Regression R^2 values with respect to
customColors = None
customYLabel = None #"poop" 
# First int is x-axis, next int's are the functions to plot w/ respect to x on
# the same plot 

plots = [	[3, 1],
			[0, 3],
			[2, 3],
			[1, 3, 0, 2] 
			]

YLabels = None

YLabels = [	"Poop1",
			"poop2",
			"poop3",
			"poop4"
			] 


i = 0
for plotData in plots:
	# print(plotData)
	#  Create Plotting Object: LOAD A LABELED CSV FILE
	plot = ChE.ChEplot()
	plot.loadCSV(_filename, labels, indepVars=1, skip=1)
	#Set Data
	plot.setDataLabel(labels)
	#Plotting
	plot.setDataColors(customColors)
	plot.setFxns2Plot(plotData)
	plot.plotData(width=6,height=6)
	#Statistics & Regression
	plot.plotLRegLines(width=0.5)
	# plot.printAllRSquared()
	#Plot Parameters 
	xaxisLabel = labels[plotData[0]] #Don't Change
	yaxisLabel = YLabels[i] if YLabels else labels[plotData[1]]
	plot.setAxisLabels(xaxisLabel, yaxisLabel, xpadding=5, ypadding=5)
	plot.setTicProps()
	# plot.setNumTics(delta_x=1.0, delta_y=1.0, x_subTics=3, y_subTics=3)
	plot.showLegend()
	# plot.changeFont()
	#Presentation
	# plot.showPlot()
	temp = folder + str(i) + '_' + savePlotAs
	plot.savePlot(filename=temp,_dpi=600)
	print("\tPlot SAVED as ", temp)
	plot.close()
	i += 1

# def	saveManyPlots(_dataSets: list):
# 	for i in range(0, len(_dataSets)):
# 		#Create Plotting Object: LOAD A LABELED CSV FILE
# 		plot = ChE.ChEplot()
# 		plot.loadCSV(_filename, labels, indepVars=1, skip=1)
# 		#Set Data
# 		plot.setDataLabel(labels)
# 		#Plotting
# 		plot.setDataColors(customColors)
# 		plot.setFxns2Plot(_dataSets)
# 		plot.plotData(width=6,height=6)
# 		#Statistics & Regression
# 		plot.plotLRegLines(width=0.5)
# 		plot.printAllRSquared(vars=regressionVars)
# 		#Plot Parameters 
# 		xaxisLabel = labels[_dataSets[0]] #Don't Change
# 		yaxisLabel = customYAxisLabel if customYAxisLabel else labels[1]
# 		plot.setAxisLabels(xaxisLabel, yaxisLabel, xpadding=5, ypadding=5)
# 		plot.setTicProps()
# 		# plot.setNumTics(delta_x=1.0, delta_y=1.0, x_subTics=3, y_subTics=3)
# 		plot.showLegend()
# 		plot.changeFont()
# 		#Presentation
# 		# plot.showPlot()
# 		imgFileName = folder + str(i) + "_" + savePlotAs
# 		plot.savePlot(filename=imgFileName,_dpi=600)


# saveManyPlots(dataSets2Plot)



# #Data
# plot.loadCSV('logRe_logf.csv', dataNames, indepVars=1)
# #Plotting
# # plot.setFnLabels(fnLabels)
# plot.setDataColors(['#89CFF0','#800020','#301934'])
# plot.plotData(width=6,height=6)
# #Regression
# plot.plotLRegLines(width=0.1)
# plot.printAllRSquared()
# #Plot Parameters 
# plot.setAxisLabels("$Log_{10}(\mathcal{Re})$", "$Log_{10}(\mathcal{f})$", xpadding=5, ypadding=5)
# plot.setTicProps()
# plot.setNumTics(0.1, 0.25, 3,3)
# plot.showLegend()
# plot.changeFont()
# #Presentation
# plot.showPlot()
# plot.savePlot(filename="log(Re)_vs_log(f).png",_dpi=600)
# # plot.close()





#Best fit calibration line for the data, to modify the process control pressure. 
#I need to determine a logical argument if the transducer should be implemented

#Data->
# 	Err = +/- (ErrX, ErrY)->
# 		Calibration line->
#			Calculate 𝛥P for the tech to modify the process control
				#Should the transducer be used in the plant, given data

#Claibration Curve with 2 different method
# 		(a)std regression
# 			 report errors/confidence intervals on the estimated parameters
# 			 (i.e., slope and intercept).
#		(b) Using χ2 minimization, also 
# 			reporting the slope and intercept.


print("Program Complete")