# libraries imports
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
import math


# The function creates the load and temperature arrays for TrainSet For Case 1.

def variablesCreation(loadTarget, loadLag1, loadLag2, loadLag3):
    df = loadTarget
    loadTrgt = df.to_numpy()
    df = loadLag1
    lag1 = df.to_numpy()
    df = loadLag2
    lag2 = df.to_numpy()
    df = loadLag3
    lag3 = df.to_numpy()



    return loadTrgt, lag1, lag2, lag3


# Generation of the day of the week reference based on lags date

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

# TrainSet and TestSet creation
def setCreation(target, lag1, lag2, lag3):

         #trainSetX
         maxLoad = max(lag1)
         minLoad= min(lag1)
         data = []
         for i in range(0, 24):
              pros = [lag1[i], lag2[i], lag3[i]]
              data.append(pros)
         data1 = np.reshape(data, (24, len(pros)))

         #trainSetY
         data = []
         df = target
         for i in range(24):
              x = df[i]
              data.append(x)
         data2 = np.reshape(data, (-1, 1))
         return data1, data2

########################################################################################################################
# Case 2

def setCreationCase2(target, lag1, lag2, lag3):
    # trainSetX
    maxLoad = max(lag1)
    minLoad = min(lag1)
    data = []
    for i in range(0, 24):
        pros = [lag1[i], lag2[i], lag3[i], math.sin(i+1), maxLoad, minLoad]
        data.append(pros)
    data1 = np.reshape(data, (24, len(pros)))

    # trainSetY
    data = []
    df = target
    for i in range(24):
        x = df[i]
        data.append(x)
    data2 = np.reshape(data, (-1, 1))
    return data1, data2



#####################################################################################################################

# CASE 3

def variablesCreationCase3(loadTarget, loadLag1, loadLag2, loadLag3, tempTarget, tempLag1, tempLag2, tempLag3 ):
    df = loadTarget
    x = df.to_numpy()
    df = loadLag1
    y = df.to_numpy()
    df = loadLag2
    z = df.to_numpy()
    df = loadLag3
    z1 = df.to_numpy()

    df = tempTarget
    t1 = df.to_numpy()
    df = tempLag1
    t2 = df.to_numpy()
    df = tempLag2
    t3 = df.to_numpy()
    df = tempLag3
    t4 = df.to_numpy()

    return x, y, z, z1, t1, t2, t3, t4



def setCreationCase3(target, lag1, lag2, lag3,  temperTarget, temperLag1, temperLag2, temperLag3):

         #trainSetX
         maxLoad = max(lag1)  # creating average max load values
         minLoad = min(lag1) # creating average min value
         data = []
         for i in range(0, 24):
              temp = [lag1[i], lag2[i], lag3[i], temperTarget[i], temperLag1[i], temperLag2[i], temperLag3[i],
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
# Case 4
def variablesCreationCase4(loadTarget, loadLag1, loadLag2, loadLag3, tempTarget, tempLag1, tempLag2, tempLag3 ):
    df = loadTarget
    x = df.to_numpy()
    df = loadLag1
    y = df.to_numpy()
    df = loadLag2
    z = df.to_numpy()
    df = loadLag3
    z1 = df.to_numpy()

    df = tempTarget
    t1 = df.to_numpy()
    df = tempLag1
    t2 = df.to_numpy()
    df = tempLag2
    t3 = df.to_numpy()
    df = tempLag3
    t4 = df.to_numpy()

    return x, y, z, z1, t1, t2, t3, t4

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



def setCreationCase4(target, lag1, weekDayLag1, lag2, weekDayLag2, lag3, weekDayLag3,  temperTarget, temperLag1, temperLag2, temperLag3):

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
