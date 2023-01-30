import numpy as np 
import pandas as pd 
def cosine_similarity(vecA,vecB):
    # vecA, vecB are here 35 dimension vector
    mod_A=0.0
    mod_B=0.0
    dot_product=0.0
    for i in range(len(vecA)):
        mod_A+=vecA[i]**2
        mod_B+=vecB[i]**2
        dot_product+=vecA[i]*vecB[i]
    cosine=(dot_product)/(np.sqrt(mod_A)*np.sqrt(mod_B))
    theta=round(np.arccos(round(cosine,3))*(180/np.pi),3)
    # return theta
    return cosine

# Read one test data and compare with all of the training data, and report the most similar one
test_data=[1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1] # M
train_dataframe=pd.read_csv('train.csv')
train_data={}
character=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for j in range(26):
    arr=[]
    for i in range(1,36):
        arr.append(train_dataframe['x{}'.format(i)][j])
    train_data[character[j]]=arr

testing_data_sheet={}
for key, value in train_data.items():
    vecA=value
    vecB=test_data
    testing_data_sheet[key]=cosine_similarity(vecA,vecB)

print(testing_data_sheet)
