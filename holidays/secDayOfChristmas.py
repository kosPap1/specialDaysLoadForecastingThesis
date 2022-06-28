import numpy as np
import pandas as pd
from functions.dataInput import load2014, load2015, load2016, temp2014, temp2015, temp2016
from BorutaShap import BorutaShap
import time
import datetime
import math

# Train Load lag inputs
loadTrainDayTarget = load2016['2016-12-26']
loadTrainDayMinus1 = load2016['2016-12-25']
loadTrainDayMinus7 = load2016['2016-12-19']
loadTrainDayMinus365 = load2015['2015-12-26']
loadTrainDayMinus730 = load2014['2014-12-26']

# Train temperature lag inputs
temperTrainDayTarget = temp2016['2016-12-26']
temperTrainDayMinus1 = temp2016['2016-12-25']
temperTrainDayMinus7 = temp2016['2016-12-19']
temperTrainDayMinus365 = temp2015['2015-12-26']
temperTrainDayMinus730 = temp2014['2014-12-26']

#############################################################################################
def daysOfTheWeekReferance(lag1, lag2, lag3):

    # D - 1
    temp1 = str(lag1.name)
    temp1 = temp1.split()
    lag1TiStamp = (time.mktime(datetime.datetime.strptime(temp1[0], "%Y-%m-%d").timetuple()))
    weekDayLag1 = datetime.datetime.fromtimestamp(lag1TiStamp).isoweekday()

    # D - 7
    temp1 = str(lag2.name)
    temp1 = temp1.split()
    lag2TiStamp = (time.mktime(datetime.datetime.strptime(temp1[0], "%Y-%m-%d").timetuple()))
    weekDayLag2 = datetime.datetime.fromtimestamp(lag2TiStamp).isoweekday()

    # D - 365
    temp1 = str(lag3.name)
    temp1 = temp1.split()
    lag3TiStamp = (time.mktime(datetime.datetime.strptime(temp1[0], "%Y-%m-%d").timetuple()))
    weekDayLag3 = datetime.datetime.fromtimestamp(lag3TiStamp).isoweekday()

    return weekDayLag1, weekDayLag2, weekDayLag3

weekDayLag1, weekDayLag2, weekDayLag3 = daysOfTheWeekReferance(loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365)

###############################################

# Transforming to numpy arrays
loadTrainLagTarget = loadTrainDayTarget.to_numpy()
loadTrainLagMinus1 = loadTrainDayMinus1.to_numpy()
loadTrainLagMinus7 = loadTrainDayMinus7.to_numpy()
loadTrainLagMinus365 = loadTrainDayMinus365.to_numpy()
tempTrainDayTarget = temperTrainDayTarget.to_numpy()

def setCreation(target, lag1, weekDayLag1, lag2, weekDayLag2, lag3, weekDayLag3,  temperTarget, temperLag1, temperLag2, temperLag3):

         #trainSetX
         maxLoad = max(lag1)  # creating average max load values
         minLoad = min(lag1) # creating average min value
         data = []
         for i in range(0, 24):
              temp = [lag1[i], math.sin(weekDayLag1), lag2[i],math.sin(weekDayLag2), lag3[i], math.sin(weekDayLag3),
                      temperTarget[i], temperLag1[i], temperLag2[i], temperLag3[i],
                      math.cos(i + 1), maxLoad, minLoad]
              data.append(temp)
         data1 = np.reshape(data, (24, len(temp)))

         #trainSetY
         data = []
         df = target
         for i in range(24):
              x = df[i]
              data.append(x)
         data2 = np.reshape(data, (-1, 1))
         return data1, data2


#######################################################################################################################


trainX, trainY = setCreation(loadTrainLagTarget, loadTrainLagMinus1, weekDayLag1, loadTrainDayMinus7, weekDayLag2, loadTrainDayMinus365,
                             weekDayLag3, tempTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus7,
                             temperTrainDayMinus365)

#######################################################################################################################

# Feature selection with Boruta SHAP

featureSelector = BorutaShap(importance_measure='shap', classification=False)
df1 = pd.DataFrame(trainX)
df1.columns = ['D-1', 'WeekDayLag1', 'D-7', 'WeekDayLag2', 'D-365', 'WeekDayLag3', 'TempDayTarget', 'tempD-1',
               'TempD-7', 'Temp-365', 'HourIndicator', 'maxLoad', 'minLoad']

df2 = pd.DataFrame(trainY)
df2.columns = ['loadTarget']

df2 = df2.to_numpy()
featureSelector.fit(df1, df2, n_trials=100, random_state=0)
featureSelector.plot(which_features='all', figsize=(24, 28))







