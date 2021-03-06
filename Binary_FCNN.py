import tflearn
import random
import pandas as pd
import numpy as np
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter
import NNFunctions as nnf
from sklearn import preprocessing

# Var name have been removed for data privacy
in_df = pd.read_excel("H:\folder")

def NeuralNetInit(NNbool, Input_ex, Learning_Rate):
    input_size = len(Input_ex)
    if NNbool:
#       by continually adding network to the argument of the next layer, you build up the network.
#       I.E. Input data initialises the NN
        network = input_data(shape=[None, input_size, 1], name='input')
        print(input_size,network)
#       Here you tell Network to incorporate the last intialisation and add a fully connected layer, the 'incoming' layer.
        network = fully_connected(network, 128, activation='sigmoid')
        network = dropout(network, 0.8)

        network = fully_connected(network, 256, activation='sigmoid')
        network = dropout(network, 0.8)

        network = fully_connected(network, 128, activation='sigmoid')
        network = dropout(network, 0.8)

#       Below is the output layer: sell large, sell low, nothing, buy low, buy high  
        network = fully_connected(network, 2, activation='softmax')
        network = regression(network, optimizer='adam', learning_rate=Learning_Rate, loss='categorical_crossentropy', name='targets')
        model = tflearn.DNN(network, tensorboard_dir='log')
        
        NNbool = False

    return model

def init(Input_ex,NNbool,Learning_Rate):
    model = NeuralNetInit(NNbool,Input_ex,Learning_Rate)
    
    return model

def train_model(training_data, model=False):

    # reshape actions to 1-D array
    X = np.array([i[0] for i in training_data]).reshape(-1,len(training_data[0][0]),1)
    # Reward does not need to be reshaped as it is already 1-D
    y = [i[1] for i in training_data]
    print(X[1],y[1])
    if not model:
        model = neural_network_model(input_size = len(X[0]))
    
    model.fit({'input': X}, {'targets': y}, n_epoch=10, snapshot_step=500, show_metric=True, run_id='openai_learning')
    return model


def Normaliser(array):
    
    minnum = min(array)
    output=[]
    
    for num in array:
        output.append(num-minnum)
    
    maxnum = max(output)
    
    for i,num in enumerate(output):
        output[i] = num/maxnum
        
    return output
    
print(Normaliser([-1,-2,0,2,10,-15]))
    

def df2input(df):
    data = []

    for col in df.columns.tolist():
        df[col] = df[col].astype(float)
        x = Normaliser(df[col].values)
        df[col] = x
        
    for i,row in df.iterrows():
        datum = [[row[X],row[X],row[X],row[X],row[X],row[X],row[X]],[row[Y],row[Y]]]
        data.append(datum)

        data.append(datum)
        
    return data


in_data = df2input(in_df)


print(in_data[0][0])

Learning_Rate = 0.0001
NNbool = True
Agent = init(in_data[0][0],NNbool,Learning_Rate)

Agent = train_model(in_data,model=Agent)

wrong_out = 0
correct_out = 0

for datum in in_data:
    inp = datum[0]
    pred_in=[]
    for i,point in enumerate(inp):
        pred_in.append([point])
    prediction = Agent.predict([pred_in])[0]
    
    if prediction[0]>0.54:
        prediction = [1.0,0.0]
    elif prediction[0]<0.46:
        prediction = [0.0,1.0]
        
        
    print(datum[1],prediction)
    if str(datum[1]) == str(prediction):
        print('Correct!')
        correct_out +=1
    else:
        print('Incorrect!')
        wrong_out +=1

print(correct_out/(correct_out+wrong_out)*100,'% correct.')