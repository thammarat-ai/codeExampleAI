# Example 11.10 Stock Prediction with LSTM
# Modified from
# https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


def create_dataset(dataset, xback=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-xback-1):
        a = dataset[i:(i+xback), 0]
        dataX.append(a)
        dataY.append(dataset[i + xback, 0])
    return numpy.array(dataX), numpy.array(dataY)
def getData(file, col):
    # load the dataset
    dataframe = read_csv(file,usecols=[col], engine='python')
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    # normalize the dataset
    dataset = scaler.fit_transform(dataset)
    # split into train and test sets
    train_size = int(len(dataset) * ratio)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

    trainX, trainY = create_dataset(train, xback)
    testX, testY = create_dataset(test, xback)
    # reshape input to be [samples, time steps, features]
    trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
    testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 1))
    return trainX, trainY,testX, testY, dataset

def train(trainX, trainY,testX, testY):
    # create and fit the LSTM network
    model = Sequential()
    model.add(LSTM(4, input_shape=(xback, 1)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=10, batch_size=1, verbose=2)
    return model

def predict(model, trainX, trainY,testX, testY, dataset):
    # make predictions
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    # invert predictions
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])
    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))
    # shift train predictions for plotting
    trainPredictPlot = numpy.empty_like(dataset)
    trainPredictPlot[:, :] = numpy.nan
    trainPredictPlot[xback:len(trainPredict)+xback, :] = trainPredict
    # shift test predictions for plotting
    testPredictPlot = numpy.empty_like(dataset)
    testPredictPlot[:, :] = numpy.nan
    testPredictPlot[len(trainPredict)+(xback*2)+1:len(dataset)-1, :] = testPredict
    # plot baseline and predictions
    plt.plot(scaler.inverse_transform(dataset),'o',label='origial data')
    plt.plot(trainPredictPlot,label='predict train')
    plt.plot(testPredictPlot,label='predict test')
    plt.legend()
    plt.show()


# reshape into X=5 and Y=5+1
xback = 5
#numpy.random.seed(7)
scaler = MinMaxScaler(feature_range=(0, 1))
ratio = 0.9
file = 'AAPL.csv'
col = 4

trainX, trainY,testX, testY, dataset = getData(file,col)
model = train(trainX, trainY,testX, testY)
predict(model, trainX, trainY,testX, testY, dataset)
