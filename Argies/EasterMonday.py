import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
import xgboost as xgb
from functions.dataInput import load2014, load2015, load2018, load2019, temp2015, temp2019
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

# Lags creation
loadTrainLagTarget = load2015['2015-04-13']
loadTrainLagMinus1 = load2015['2015-04-12']
loadTrainLagMinus7 = load2015['2015-04-06']
loadTrainLagMinus365 = load2014['2014-04-21']
tempTrainDayTarget = temp2015['2015-04-13']

loadTestLagTarget = load2019['2019-04-29']
loadTestLagMinus1 = load2019['2019-04-28']
loadTestLagMinus7 = load2019['2019-04-22']
loadTestLagMinus365 = load2018['2018-04-09']
tempTestDayTarget = temp2019['2019-04-29']

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
    temp1 = [loadTestLagMinus1[i], loadTestLagMinus7[i], loadTestLagMinus365[i]]
    data.append(temp1)
data = np.reshape(data, (24, len(temp1)))

for i in range(0, 24):
    temp2 = loadTestLagTarget[i]
    data2.append(temp2)
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

#######################################################################################################################

# Model training
model = xgb.XGBRegressor(base_score = 0.9322533260536534,
             learning_rate = 0.969683007936686,
             max_depth = 1,
             n_estimators = 320,
             reg_alpha =0.03,
             reg_lambda = 43.45958556954177, booster='dart')
model.fit(trainX, trainY)

# Predicting Next Days load
y_pred = model.predict(testX)

#######################################################################################################################

MLPreg = MLPRegressor(hidden_layer_sizes=(106, 12), random_state=0, solver='lbfgs',
                      max_iter=2000).fit(trainX, trainY.ravel())

y_pred_MLP = MLPreg.predict(testX)
# Inverse transform
y_pred = np.reshape(y_pred, (-1, 1))

y_pred_MLP = np.reshape(y_pred_MLP, (-1, 1))

y_pred = scaler.inverse_transform(y_pred)
y_pred_MLP = scaler.inverse_transform(y_pred_MLP)
testY = scaler.inverse_transform(testY)

print('MAPE for Easter Monday with XGBoost is ' + str(mean_absolute_percentage_error(y_pred, testY) * 100))
print('MAPE for Easter Monday with MLP is ' + str(mean_absolute_percentage_error(y_pred_MLP, testY) * 100))

plt.plot(testY, label='actual value')
plt.plot(y_pred, label='prediction')
plt.legend()
plt.show()

plt.plot(y_pred_MLP, label = 'MLP')
plt.plot(testY, label = 'actual')
plt.legend()
plt.show()






