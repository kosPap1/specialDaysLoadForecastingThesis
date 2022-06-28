from functions.TransformAndCreationFunctions import variablesCreation, variablesCreationCase3, daysOfTheWeekReferance,\
    setCreation, setCreationCase2, setCreationCase3, setCreationCase4
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
from sklearn.metrics import mean_absolute_percentage_error
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
import xgboost as xgb
import os


# Prediction engine for Case 1

def predictionEngine1(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365, loadTestDayTarget,
                     loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename):
    ########################################################################################################################

    # Training Sets

    # creating  Variables for TrainSets

    (loadTarget, loadLag1, loadLag2, loadLag3) = variablesCreation(loadTrainDayTarget, loadTrainDayMinus1,
                                                                   loadTrainDayMinus7, loadTrainDayMinus365)

    # Creating Days Of the Week reference

    (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTrainDayMinus1, loadTrainDayMinus7,
                                                                     loadTrainDayMinus365)

    # Creating Train sets
    trainSetX, trainSetY = setCreation(loadTarget, loadLag1, loadLag2, loadLag3)

    ########################################################################################################################

    # Test Sets
    # creating  Variables for Test Sets

    (loadTarget, loadLag1, loadLag2, loadLag3) = variablesCreation(loadTestDayTarget, loadTestDayMinus1,
                                                                   loadTestDayMinus7, loadTestDayMinus365)

    # Creating Days Of the Week reference

    (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTestDayMinus1, loadTestDayMinus7,
                                                                     loadTestDayMinus365)

    # # Creating Test Sets

    testSetX, testSetY = setCreation(loadTarget, loadLag1, loadLag2, loadLag3)

    ###########################################################

    # Scaling
    scaler = StandardScaler()
    scaler_coeff = 1

    # Scaling Train Sets
    trainSetX = scaler.fit_transform(trainSetX) * scaler_coeff
    trainSetY = scaler.fit_transform(trainSetY) * scaler_coeff

    # Scaling Test sets

    testSetX = scaler.fit_transform(testSetX) * scaler_coeff
    testSetY = scaler.fit_transform(testSetY) * scaler_coeff
    ###########################################################

    # running the MLP regression
    MLPreg = MLPRegressor().fit(trainSetX, trainSetY.ravel())

    ###########################################################

    # predicting next day's load

    h_prediction = MLPreg.predict(testSetX)

    # running xgboost predictor
    model = xgb.XGBRegressor(booster='dart')
    model.fit(trainSetX, trainSetY)

    # predicting next day's load

    y_predXGB = model.predict(testSetX)

    # revert scaling

    h_prediction = np.reshape(h_prediction, (-1, 1))
    y_predXGB = np.reshape(y_predXGB, (-1, 1))

    y_predXGB = scaler.inverse_transform(y_predXGB / scaler_coeff)
    h_prediction = scaler.inverse_transform(h_prediction / scaler_coeff)
    testSetY = scaler.inverse_transform(testSetY / scaler_coeff)
    #
    # # printing results
    #
    # print(h_prediction)
    # print(y_predXGB)
    # print(testSetY)
    #
    # calculating MAPE with sklearn
    mape = (mean_absolute_percentage_error(testSetY, h_prediction)) * 100
    maxError = metrics.max_error(testSetY, h_prediction)
    print('MAPE with mlp is ' + str(mape) + ' for ' + str(filename) )
    mape2 = (mean_absolute_percentage_error(testSetY, y_predXGB)) * 100
    print('MAPE with xgb is ' + str(mape2) + ' for ' + str(filename) )
    print('\n')


    # print('Model score by Metrics.R2 equals to ' + str(metrics.r2_score(testSetY, h_prediction)))
    # print('Models max error is ' + str(maxError))

    # # Plots
    # plt.plot(y_predXGB, label='Predicted Value')
    # plt.plot(testSetY, label='Actual Value')
    # plt.plot(loadTestDayMinus365, label=' 2018')
    # #
    # plt.title(str(filename))
    # plt.legend()
    # plt.show()




# Prediction engine for Case 2

def predictionEngineCase2(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365, loadTestDayTarget,
                     loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename):
    ########################################################################################################################

    # Training Sets

    # creating  Variables for TrainSets

    (loadTarget, loadLag1, loadLag2, loadLag3) = variablesCreation(loadTrainDayTarget, loadTrainDayMinus1,
                                                                   loadTrainDayMinus7, loadTrainDayMinus365)

    # Creating Days Of the Week reference

    (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTrainDayMinus1, loadTrainDayMinus7,
                                                                     loadTrainDayMinus365)

    # Creating Train sets
    trainSetX, trainSetY = setCreationCase2(loadTarget, loadLag1, loadLag2, loadLag3)

    ########################################################################################################################

    # Test Sets
    # creating  Variables for Test Sets

    (loadTarget, loadLag1, loadLag2, loadLag3) = variablesCreation(loadTestDayTarget, loadTestDayMinus1,
                                                                   loadTestDayMinus7, loadTestDayMinus365)

    # Creating Days Of the Week reference

    (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTestDayMinus1, loadTestDayMinus7,
                                                                     loadTestDayMinus365)

    # # Creating Test Sets

    testSetX, testSetY = setCreationCase2(loadTarget, loadLag1, loadLag2, loadLag3)

    ###########################################################

    # Scaling
    scaler = MinMaxScaler()
    scaler_coeff = 1

    # Scaling Train Sets
    trainSetX = scaler.fit_transform(trainSetX) * scaler_coeff
    trainSetY = scaler.fit_transform(trainSetY) * scaler_coeff

    # Scaling Test sets

    testSetX = scaler.fit_transform(testSetX) * scaler_coeff
    testSetY = scaler.fit_transform(testSetY) * scaler_coeff
    ###########################################################

    # running the MLP regression
    MLPreg = MLPRegressor().fit(trainSetX, trainSetY.ravel())

    ###########################################################

    # predicting next day's load

    h_prediction = MLPreg.predict(testSetX)

    # running xgboost predictor
    model = xgb.XGBRegressor(booster='gbtree')
    model.fit(trainSetX, trainSetY)

    # predicting next day's load

    y_predXGB = model.predict(testSetX)

    # revert scaling

    h_prediction = np.reshape(h_prediction, (-1, 1))
    y_predXGB = np.reshape(y_predXGB, (-1, 1))

    y_predXGB = scaler.inverse_transform(y_predXGB / scaler_coeff)
    h_prediction = scaler.inverse_transform(h_prediction / scaler_coeff)
    testSetY = scaler.inverse_transform(testSetY / scaler_coeff)
    #
    # # printing results
    #
    # print(h_prediction)
    # print(y_predXGB)
    # print(testSetY)
    #
    # calculating MAPE with sklearn
    mape = (mean_absolute_percentage_error(testSetY, h_prediction)) * 100
    maxError = metrics.max_error(testSetY, h_prediction)
    print('MAPE with mlp is ' + str(mape) + ' for ' + str(filename))
    mape2 = (mean_absolute_percentage_error(testSetY, y_predXGB)) * 100
    print('MAPE with xgb is ' + str(mape2) + ' for ' + str(filename))
    print('\n')

    # print('Model score by Metrics.R2 equals to ' + str(metrics.r2_score(testSetY, h_prediction)))
    # print('Models max error is ' + str(maxError))

    # # Plots
    # plt.plot(y_predXGB, label='Predicted Value')
    # plt.plot(testSetY, label='Actual Value')
    # plt.plot(loadTestDayMinus365, label=' 2018')
    # #
    # plt.title(str(filename))
    # plt.legend()
    # plt.show()



#######################################################################################################################
#Prediction Engine for case 3

def predictionEngineCase3(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
                              loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, temperTrainDayTarget,
                          temperTrainDayMinus1, temperTrainDayMinus2, temperTrainDayMinus365, temperTestDayTarget,
                          temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365, filename):
        ########################################################################################################################

        # Training Sets

        # creating  Variables for TrainSets

        (loadTarget, loadLag1, loadLag2, loadLag3, tempTarget, tempLag1, tempLag2, tempLag3) =\
            variablesCreationCase3(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
                                  temperTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus2, temperTrainDayMinus365)

        # Creating Days Of the Week reference

        (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTrainDayMinus1, loadTrainDayMinus7,
                                                                         loadTrainDayMinus365)

        # Creating Train sets
        trainSetX, trainSetY = setCreationCase3(loadTarget, loadLag1, loadLag2, loadLag3, tempTarget, tempLag1, tempLag2, tempLag3)

        ########################################################################################################################

        # Test Sets
        # creating  Variables for Test Sets

        (loadTarget, loadLag1, loadLag2, loadLag3,  tempTarget, tempLag1, tempLag2, tempLag3) = \
            variablesCreationCase3(loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, temperTestDayTarget,
                              temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365)

        # Creating Days Of the Week reference

        (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTestDayMinus1, loadTestDayMinus7,
                                                                         loadTestDayMinus365)

        # # Creating Test Sets

        testSetX, testSetY = setCreationCase3(loadTarget, loadLag1, loadLag2, loadLag3, tempTarget, tempLag1, tempLag2,
                                              tempLag3)

        ###########################################################

        # Scaling
        scaler = MinMaxScaler()
        scaler_coeff = 1

        # Scaling Train Sets
        trainSetX = scaler.fit_transform(trainSetX) * scaler_coeff
        trainSetY = scaler.fit_transform(trainSetY) * scaler_coeff

        # Scaling Test sets

        testSetX = scaler.fit_transform(testSetX) * scaler_coeff
        testSetY = scaler.fit_transform(testSetY) * scaler_coeff

        ###########################################################

        # running the MLP regression
        MLPreg = MLPRegressor().fit(trainSetX, trainSetY.ravel())

        ###########################################################

        # predicting next day's load

        h_prediction = MLPreg.predict(testSetX)

        # running xgboost predictor
        model = xgb.XGBRegressor(booster='dart')
        model.fit(trainSetX, trainSetY)

        # predicting next day's load

        y_predXGB = model.predict(testSetX)

        # revert scaling

        h_prediction = np.reshape(h_prediction, (-1, 1))
        y_predXGB = np.reshape(y_predXGB, (-1, 1))

        y_predXGB = scaler.inverse_transform(y_predXGB / scaler_coeff)
        h_prediction = scaler.inverse_transform(h_prediction / scaler_coeff)
        testSetY = scaler.inverse_transform(testSetY / scaler_coeff)
        #
        # # printing results
        #
        # print(h_prediction)
        # print(y_predXGB)
        # print(testSetY)
        #
        # calculating MAPE with sklearn
        mape = (mean_absolute_percentage_error(testSetY, h_prediction)) * 100
        maxError = metrics.max_error(testSetY, h_prediction)
        print('MAPE with mlp is ' + str(mape) + ' for ' + str(filename))
        mape2 = (mean_absolute_percentage_error(testSetY, y_predXGB)) * 100
        print('MAPE with xgb is ' + str(mape2) + ' for ' + str(filename))
        print('\n')

        # print('Model score by Metrics.R2 equals to ' + str(metrics.r2_score(testSetY, h_prediction)))
        # print('Models max error is ' + str(maxError))

        # # Plots
        # plt.plot(y_predXGB, label='Predicted Value')
        # plt.plot(testSetY, label='Actual Value')
        # plt.plot(loadTestDayMinus365, label=' 2018')
        # #
        # plt.title(str(filename))
        # plt.legend()
        # plt.show()


########################################################################################################################

                                         #Case 4

#Prediction Engine for case 4

def predictionEngineCase4(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
                              loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, temperTrainDayTarget,
                          temperTrainDayMinus1, temperTrainDayMinus2, temperTrainDayMinus365, temperTestDayTarget,
                          temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365, filename):
        ########################################################################################################################

        # Training Sets

        # creating  Variables for TrainSets

        (loadTarget, loadLag1, loadLag2, loadLag3, tempTarget, tempLag1, tempLag2, tempLag3) =\
            variablesCreationCase3(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
                                  temperTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus2, temperTrainDayMinus365)

        # Creating Days Of the Week reference

        (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTrainDayMinus1, loadTrainDayMinus7,
                                                                         loadTrainDayMinus365)

        # Creating Train sets
        trainSetX, trainSetY = setCreationCase4(loadTarget, loadLag1, weekDayLag1, loadLag2, weekDayLag2, loadLag3,
                                                weekDayLag3, tempTarget, tempLag1, tempLag2, tempLag3)

        ########################################################################################################################

        # Test Sets
        # creating  Variables for Test Sets

        (loadTarget, loadLag1, loadLag2, loadLag3,  tempTarget, tempLag1, tempLag2, tempLag3) = \
            variablesCreationCase3(loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, temperTestDayTarget,
                              temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365)

        # Creating Days Of the Week reference

        (weekDayLag1, weekDayLag2, weekDayLag3) = daysOfTheWeekReferance(loadTestDayMinus1, loadTestDayMinus7,
                                                                         loadTestDayMinus365)

        # # Creating Test Sets

        testSetX, testSetY = setCreationCase4(loadTarget, loadLag1, weekDayLag1, loadLag2, weekDayLag2, loadLag3,
                                                weekDayLag3, tempTarget, tempLag1, tempLag2, tempLag3)

        ###########################################################

        # Scaling
        scaler = MinMaxScaler()
        scaler_coeff = 1

        # Scaling Train Sets
        trainSetX = scaler.fit_transform(trainSetX) * scaler_coeff
        trainSetY = scaler.fit_transform(trainSetY) * scaler_coeff

        # Scaling Test sets

        testSetX = scaler.fit_transform(testSetX) * scaler_coeff
        testSetY = scaler.fit_transform(testSetY) * scaler_coeff

        ###########################################################

        # running the MLP regression
        MLPreg = MLPRegressor().fit(trainSetX, trainSetY.ravel())

        ###########################################################

        # predicting next day's load

        h_prediction = MLPreg.predict(testSetX)


        # running xgboost predictor
        model = xgb.XGBRegressor()
        model.fit(trainSetX, trainSetY)

        # predicting next day's load

        y_predXGB = model.predict(testSetX)


        # revert scaling

        h_prediction = np.reshape(h_prediction, (-1, 1))
        y_predXGB = np.reshape(y_predXGB, (-1, 1))

        y_predXGB = scaler.inverse_transform(y_predXGB / scaler_coeff)
        h_prediction = scaler.inverse_transform(h_prediction / scaler_coeff)
        testSetY = scaler.inverse_transform(testSetY / scaler_coeff)
        #
        # # printing results
        #
        # print(h_prediction)
        # print(y_predXGB)
        # print(testSetY)
        #
        # calculating MAPE with sklearn
        mape = (mean_absolute_percentage_error(testSetY, h_prediction)) * 100
        maxError = metrics.max_error(testSetY, h_prediction)
        print('MAPE with mlp is ' + str(mape) + ' for ' + str(filename))
        mape2 = (mean_absolute_percentage_error(testSetY, y_predXGB)) * 100
        print('MAPE with xgb is ' + str(mape2) + ' for ' + str(filename))
        print('\n')

        # print('Model score by Metrics.R2 equals to ' + str(metrics.r2_score(testSetY, h_prediction)))
        # print('Models max error is ' + str(maxError))

        #Plots
        # plt.plot(y_predXGB, label='Predicted Value')
        # plt.plot(testSetY, label='Actual Value')
        # plt.plot(loadTestDayMinus365, label=' 2018')
        # #
        # plt.title(str(filename))
        # plt.legend()
        # plt.show()