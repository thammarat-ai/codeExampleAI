# Example 11.18
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score, KFold
from keras.models import Sequential
#from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import numpy as np
import matplotlib.cm as cm

linnerud = datasets.load_linnerud()
#print(linnerud.DESCR)
#print(linnerud.data.shape)
#print(linnerud.feature_names)
#print(linnerud.target_names)
#print(linnerud.target)

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


# define the model
def larger_model():
	# create model
	model = Sequential()
	model.add(Dense(20, input_dim=3,  activation='relu'))
	model.add(Dense(10,  activation='relu'))
	model.add(Dense(6,  activation='relu'))
	model.add(Dense(3))
	# Compile model
	model.compile(loss='mean_squared_error', optimizer='adam')
	return model

    
seed = 1
np.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=larger_model, epochs=50, batch_size=5, verbose=0)))
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10, random_state=seed, shuffle=True)
results = cross_val_score(pipeline, X, y, cv=kfold, n_jobs=1)
print("Larger: %.2f (%.2f) MSE" % (results.mean(), results.std()))


pipeline.fit(X, y)
prediction = pipeline.predict(X)

import numpy as np
train_error =  np.abs(y - prediction)
print("Mean Prediction Error: ", np.mean(train_error))
#print(np.min(train_error))
#print(np.max(train_error))
#print(np.std(train_error))

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2,1,1)

ys = [i for i in range(3)]
colors = cm.rainbow(np.linspace(0, 1, len(ys)))
for i, c in zip(ys, colors):
    plt.scatter(y[:,i], prediction[:,i], color=c)
    
#plt.scatter(y,prediction)
plt.title('Prediction')
plt.subplot(2,1,2)
plt.scatter(y,train_error)
plt.title('Error')
plt.show()
