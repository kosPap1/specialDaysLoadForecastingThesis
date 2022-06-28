# Importing core libraries
import numpy as np
from functions.dataInput import load2008,load2010, load2011, load2012, load2013, load2009, load2016, load2015, load2014, load2018, load2019, \
    temp2009, temp2011, temp2014, temp2015, temp2013, temp2016, temp2019
from sklearn.preprocessing import  StandardScaler
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.neural_network import MLPRegressor

import time
start_time = time.time()

loadTrainLagTarget = load2011['2011-03-25']
loadTrainLagMinus1 = load2011['2011-03-24']
loadTrainLagMinus7 = load2011['2011-03-18']
loadTrainLagMinus365 = load2010['2010-03-25']
tempTrainDayTarget = temp2011['2011-03-25']

loadTestLagTarget = load2019['2019-03-25']
loadTestLagMinus1 = load2019['2019-03-24']
loadTestLagMinus7 = load2019['2019-03-18']
loadTestLagMinus365 = load2018['2018-03-25']
tempTestDayTarget = temp2019['2019-03-25']

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

# Creating a Wrapper to work around the layers problem

class MLPWrapper(BaseEstimator, ClassifierMixin):
    def __init__(self, layer1=10, layer2=10, layer3=10 ):
        self.layer1 = layer1
        self.layer2 = layer2
        self.layer3 = layer3



    def fit(self, X, y):
        model = MLPRegressor(
            hidden_layer_sizes=[self.layer1, self.layer2, self.layer3],
        max_iter=2000)
        model.fit(X, y)
        self.model = model
        return self

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)


opt = BayesSearchCV(
    estimator=MLPWrapper(),
    search_spaces={
        'layer1': Integer(12, 256),
        'layer2': Integer(12, 256),
        'layer3': Integer(12, 256),



    },
    n_iter=128, verbose=2
)


opt.fit(trainX, trainY.ravel())
best_params = opt.best_params_
print(best_params)
print(opt.score(testX, testY))
print("--- %s seconds ---" % (time.time() - start_time))