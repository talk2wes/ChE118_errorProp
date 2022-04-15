#Wesley Johanson
import ChE
import numpy as np


#Define Data
labels = ["Pressure [Bar]", "Signal [Volts]", "Pressure_xError [bar]",\
		"Signal_yError [Volts]" ]
fnLabels = labels[1:]

#Create Plotting Object
plot = ChE.ChEplot()

#FIXING THE DATA_____________________________________
plot.loadCSV("CSV/data_che118_hw.csv", labels, indepVars=1, skip=11)
print("what the original data looked like")
plot.printData()
#Gotta fix the data, it's scrambled from the copy/paste
#	->Each Row vector of the orig. matrix is listed in order, in the first col
#	of the CSV file
x = []
y = []
x_err = []
y_err = []
orig = plot.data

i = 0
while(i < len(plot.data)):
	x.append(orig[i]); i += 1	
	y.append(orig[i]); i += 1
	x_err.append(orig[i]); i += 1
	y_err.append(orig[i]); i += 1
print("what the corrected data looks like")
plot.printData()
#FIXING THE DATA_____________________________________

#Set Data
plot.setData(np.array([x, y, x_err, y_err]), vars = 1)
plot.setDataLabel(labels)
#Plotting
plot.setDataColors(['#89CFF0','#800020','#301934'])
plot.setFnLabels(fnLabels)
plot.setDataColors(['#89CFF0','#800020','#301934'])
plot.plotData(width=6,height=6)
#Regression
plot.plotLRegLines(width=0.1)
plot.printAllRSquared()


#Plot Parameters 
plot.setAxisLabels(labels[0], labels[1], xpadding=5, ypadding=5)
# plot.setTicProps()
# plot.setNumTics(delta_x=1.0, delta_y=1.0, x_subTics=3, y_subTics=3)
plot.showLegend()
plot.changeFont()
#Presentation
plot.showPlot()
plot.savePlot(filename="log(Re)_vs_log(f).png",_dpi=600)




# #Data
# plot.loadCSV('logRe_logf.csv', dataNames, indepVars=1)
# #Plotting
# plot.setFnLabels(fnLabels)
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