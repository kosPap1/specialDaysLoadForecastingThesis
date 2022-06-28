# Importing core libraries
import numpy as np
from functions.dataInput import load2008,load2010, load2011, load2012, load2013, load2009, load2016, load2015, load2014, load2018, load2019, \
    temp2009, temp2011, temp2014, temp2015, temp2013, temp2016, temp2019
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
import time

start_time = time.time()

loadTrainLagTarget = load2009['2009-10-28']
loadTrainLagMinus1 = load2009['2009-10-27']
loadTrainLagMinus7 = load2009['2009-10-21']
loadTrainLagMinus365 = load2008['2008-10-28']
tempTrainDayTarget = temp2009['2009-10-28']

loadTestLagTarget = load2019['2019-10-28']
loadTestLagMinus1 = load2019['2019-10-27']
loadTestLagMinus7 = load2019['2019-10-21']
loadTestLagMinus365 = load2018['2018-10-28']
tempTestDayTarget = temp2019['2019-10-28']

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
model = xgb.XGBRegressor( booster='gbtree')

# Creating the search parameters
search_spaces = {'learning_rate': Real(0.01, 2.0, 'uniform'),
                 'max_depth': Integer(1, 9),
                 'reg_lambda': Real(0.1, 50., 'uniform'),       # L2 regularization
                 'reg_alpha': Real(0, 1, 'uniform'),       # L1 regularization
                 'n_estimators': Integer(20, 1000),
                 'base_score': Real(0.1, 5),
                 'max_delta_step': Integer(1, 10)
   }

optimizer = BayesSearchCV(estimator=model,
                    search_spaces=search_spaces,
                    n_iter=128,
                    n_points=2,
                    n_jobs=4,
                    iid=True,
                    return_train_score=True,
                    refit=True,
                    optimizer_kwargs={},
                    random_state=0,
                    verbose=2)

optimizer.fit(trainX, trainY)

print(optimizer.best_params_)
print(optimizer.best_score_)
print(optimizer.best_index_)
print(optimizer.score(testX, testY))
print("--- %s seconds ---" % (time.time() - start_time))
