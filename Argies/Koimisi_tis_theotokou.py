import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error, accuracy_score
import xgboost as xgb
from functions.dataInput import load2011, load2010, load2018, load2019, temp2011, temp2019
from sklearn.preprocessing import  StandardScaler
from sklearn.neural_network import MLPRegressor

import time
start_time = time.time()


# Lags creation
loadTrainLagTarget = load2011['2011-08-15']
loadTrainLagMinus1 = load2011['2011-08-14']
loadTrainLagMinus7 = load2011['2011-08-08']
loadTrainLagMinus365 = load2010['2010-08-15']
tempTrainDayTarget = temp2011['2011-08-15']

loadTestLagTarget = load2019['2019-08-15']
loadTestLagMinus1 = load2019['2019-08-14']
loadTestLagMinus7 = load2019['2019-08-08']
loadTestLagMinus365 = load2018['2018-08-15']
tempTestDayTarget = temp2019['2019-08-15']

# Transforming to numpy arrays
loadTrainLagTarget = loadTrainLagTarget.to_numpy()
loadTrainLagMinus1 = loadTrainLagMinus1.to_numpy()
loadTrainLagMinus7 = loadTrainLagMinus7.to_numpy()
loadTrainLagMinus365 = loadTrainLagMinus365.to_numpy()
tempTrainDayTarget = tempTrainDayTarget.to_numpy()

loadTestLagTarget = loadTestLagTarget.to_numpy()
loadTestLagMinus1 = loadTestLagMinus1.to_numpy()
loadTestLagMinus7 = loadTestLagMinus7.to_numpy()
loadTestLagMinus365 = loadTestLagMinus365.to_numpy()
tempTestDayTarget = tempTestDayTarget.to_numpy()
#######################################################################################################################

# Creating Train Sets
data = []
data2 = []

for i in range(0, 24):
    temp1 = [loadTrainLagMinus1[i], loadTrainLagMinus7[i], loadTrainLagMinus365[i]]
    data.append(temp1)
data = np.reshape(data, (24, len(temp1)))

for i in range(0, 24):
    temp2 = loadTrainLagTarget[i]
    data2.append(temp2)
data2 = np.reshape(data2, (-1, 1))

trainX = data
trainY = data2
#######################################################################################################################

# Creating Test Sets
data = []
data2 = []

for i in range(0, 24):
    temp3 = [loadTestLagMinus1[i], loadTestLagMinus7[i], loadTestLagMinus365[i]]
    data.append(temp3)
data = np.reshape(data, (24, len(temp1)))

for i in range(0, 24):
    temp4 = loadTestLagTarget[i]
    data2.append(temp4)
data2 = np.reshape(data2, (-1, 1))
testX = data
testY = data2

#######################################################################################################################
# Scaling
scaler = StandardScaler()

trainX = scaler.fit_transform(trainX)
trainY = scaler.fit_transform(trainY)

testX = scaler.fit_transform(testX)
testY = scaler.fit_transform(testY)
########################################################################################################################
########################################################################################################################

# Model training
model = xgb.XGBRegressor(booster='dart',base_score = 4.614116315396939,
             learning_rate = 0.452317439843678336,
             max_depth = 3,
             n_estimators = 500,
             reg_alpha =0.05982,
             reg_lambda = 45.0)
model.fit(trainX, trainY)

# Predicting Next Days load
y_pred = model.predict(testX)
#
# #######################################################################################################################
MLPreg = MLPRegressor(hidden_layer_sizes=(256, 125), random_state=1, solver='adam').fit(trainX, trainY.ravel())

y_pred_MLP = MLPreg.predict(testX)
# Inverse transform
y_pred = np.reshape(y_pred, (-1, 1))

y_pred_MLP = np.reshape(y_pred_MLP, (-1, 1))

y_pred = scaler.inverse_transform(y_pred)
y_pred_MLP = scaler.inverse_transform(y_pred_MLP)
testY = scaler.inverse_transform(testY)

print('MAPE for Assumption_of_Mary with XGBoost is ' + str(mean_absolute_percentage_error(y_pred, testY) * 100))
print('MAPE for  Assumption_of_Mary with MLP is ' + str(mean_absolute_percentage_error(y_pred_MLP, testY) * 100))


plt.plot(testY, label='actual value')
plt.plot(y_pred, label='prediction')
plt.legend()
plt.show()

plt.plot(y_pred_MLP, label = 'MLP')
plt.plot(testY, label = 'actual')
plt.legend()
plt.show()






