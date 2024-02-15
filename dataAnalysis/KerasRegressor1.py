# Example 11.17
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score, KFold
from keras.models import Sequential
#from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import numpy as np

linnerud = datasets.load_linnerud()
print(linnerud.DESCR)
print(linnerud.data.shape)
print(linnerud.feature_names)
print(linnerud.target_names)
print(linnerud.target)

# Use only one feature
#linnerud_X = linnerud.data[:, np.newaxis, 0]
X = linnerud.data
# Choose one target 0: 'Weight', 1: 'Waist', 2:'Pulse'
#y = linnerud.target[:,1]
y = linnerud.target

# Split the data into training/testing sets
X_train = X[:-10]
X_test = X[-10:]
# Split the targets into training/testing sets
y_train = y[:-10]
y_test = y[-10:]

def baseline_model():
    model = Sequential()
    model.add(Dense(10, input_dim=3, activation='relu'))
    model.add(Dense(3))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

    
seed = 1
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=100, verbose=False)
kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
results = cross_val_score(estimator, X, y, cv=kfold)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

estimator.fit(X, y)
prediction = estimator.predict(X)

import numpy as np
train_error =  np.abs(y - prediction)
print("Mean Prediction Error: ", np.mean(train_error))
