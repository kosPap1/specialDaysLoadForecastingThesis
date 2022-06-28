import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
import xgboost as xgb
from functions.dataInput import load2013, load2014, load2018, load2019, temp2014, temp2019
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor


# Lags creation
loadTrainLagTarget = load2014['2014-01-01']
loadTrainLagMinus1 = load2013['2013-12-31']
loadTrainLagMinus7 = load2013['2013-12-25']
loadTrainLagMinus365 = load2013['2013-01-01']
tempTrainDayTarget = temp2014['2014-01-01']

loadTestLagTarget = load2019['2019-01-01']
loadTestLagMinus1 = load2018['2018-12-31']
loadTestLagMinus7 = load2018['2018-12-25']
loadTestLagMinus365 = load2018['2018-01-01']
tempTestDayTarget = temp2019['2019-01-01']

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

#######################################################################################################################

# Model training
model = xgb.XGBRegressor(base_score= 2.6248611982166223,
             colsample_bytree = 0.3294976947281426,
             learning_rate = 1.2712184143934175,
             max_depth = 4,
             n_estimators = 133,
             reg_alpha = 0.3692521974457114,
             reg_lambda = 14.59809995142499,
             booster='gbtree')

model.fit(trainX, trainY)
y_pred = model.predict(testX)
###########################################################

MLPreg = MLPRegressor(hidden_layer_sizes=(23, 150), random_state=0, max_iter=2000).fit(trainX, trainY.ravel())

y_pred_MLP = MLPreg.predict(testX)
# Inverse transform
y_pred = np.reshape(y_pred, (-1, 1))
y_pred_MLP = np.reshape(y_pred_MLP, (-1, 1))

y_pred = scaler.inverse_transform(y_pred)
y_pred_MLP = scaler.inverse_transform(y_pred_MLP)
testY = scaler.inverse_transform(testY)

print('MAPE for New Year with XGBoost is ' + str(mean_absolute_percentage_error(y_pred, testY) * 100))
print('MAPE for New Year with MLP is ' + str(mean_absolute_percentage_error(y_pred_MLP, testY) * 100))

plt.plot(testY, label='actual value')
plt.plot(y_pred, label='prediction')
plt.legend()
plt.show()

plt.plot(y_pred_MLP, label = 'MLP')
plt.plot(testY, label = 'actual')
plt.legend()
plt.show()









