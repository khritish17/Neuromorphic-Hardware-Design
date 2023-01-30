# Importing the libraries
import numpy as np
import pandas as pd 

'''
TO-DO-LIST:
            1. Import the data
            2. Set the neural architecture
            3. Initialize the weight and biases
            4. Forward propagation
            5. Backpropagation
'''
'''
    Global variables are declared here, e.g., IP and OP datas, weights and biases 
'''


# IP:[0...34], OP:[35...61]
# print(training_data[0][35:62])
IP_data={}          # Dictionary to save the input training data
OP_data={}          # Dictionary to save the output training data
# IP_length=len(training_data)
# OP_length=IP_length

def obtain_data():
    training_data=np.loadtxt(open('TRAIN_1.csv','r'),delimiter=',',skiprows=1)
    # IP_train=training_data[]
    for i in range(1,27):
        IP_data[i]=training_data[i-1:i,:35]
        OP_data[i]=training_data[i-1:i,35:]
    print('I/P and O/P obtained!!!')

def neural_architecture(hidden_vec):
    inp_dim=len(IP_data[1][0])
    out_dim=len(OP_data[1][0])
    print("{}:{}".format(inp_dim,out_dim))

obtain_data()
neural_architecture([1,2])