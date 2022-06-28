import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
import xgboost as xgb
from functions.dataInput import load2014, load2015, load2018, load2019, temp2015, temp2019
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

# Lags creation
loadTrainLagTarget = load2015['2015-01-06']
loadTrainLagMinus1 = load2015['2015-01-05']
loadTrainLagMinus7 = load2014['2014-12-31']
loadTrainLagMinus365 = load2014['2014-01-06']
tempTrainDayTarget = temp2015['2015-01-06']

loadTestLagTarget = load2019['2019-01-06']
loadTestLagMinus1 = load2019['2019-01-05']
loadTestLagMinus7 = load2018['2018-12-31']
loadTestLagMinus365 = load2018['2018-01-06']
tempTestDayTarget = temp2019['2019-01-06']

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
####################################################################################################################

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
####################################################################################################################

# Creating Test Sets
data = []
data2 = []

for i in range(0, 24):
    temp3 = [loadTestLagMinus1[i], loadTestLagMinus7[i], loadTestLagMinus365[i]]
    data.append(temp3)
data = np.reshape(data, (24, len(temp3)))

for i in range(0, 24):
    temp4 = loadTestLagTarget[i]
    data2.append(temp4)
data2 = np.reshape(data2, (-1, 1))
testX = data
testY = data2

####################################################################################################################

# Scaling
scaler = StandardScaler()

trainX = scaler.fit_transform(trainX)
trainY = scaler.fit_transform(trainY)

testX = scaler.fit_transform(testX)

testY = scaler.fit_transform(testY)

####################################################################################################################

# Model training
model = xgb.XGBRegressor(n_estimators=72, learning_rate=1.46, max_depth=3, base_score=0.96, booster='dart',
                         reg_alpha=0.01, reg_lambda=61.797, subsample=0.83, colsample_bytree=0.898)



###################################################################################################################
# Predicting Next Days load
model.fit(trainX, trainY)
y_pred = model.predict(testX)

####################################################################################################################
MLPreg = MLPRegressor(hidden_layer_sizes=(55, 61, 24), activation="relu", solver='adam', random_state=1,
                          max_iter=1000, learning_rate='adaptive', verbose=False).fit(trainX, trainY.ravel())

y_pred_MLP = MLPreg.predict(testX)
# Inverse transform
y_pred = np.reshape(y_pred, (-1, 1))
y_pred_MLP = np.reshape(y_pred_MLP, (-1, 1))

y_pred = scaler.inverse_transform(y_pred)
y_pred_MLP = scaler.inverse_transform(y_pred_MLP)
testY = scaler.inverse_transform(testY)

print('MAPE for Theofania with XGBoost is ' + str(mean_absolute_percentage_error(y_pred, testY) * 100))
print('MAPE for Theofania with MLP is ' + str(mean_absolute_percentage_error(y_pred_MLP, testY) * 100))

plt.plot(testY, label='actual value')
plt.plot(y_pred, label='prediction')
plt.legend()
plt.show()

plt.plot(y_pred_MLP, label = 'MLP')
plt.plot(testY, label = 'actual')
plt.legend()
plt.show()








