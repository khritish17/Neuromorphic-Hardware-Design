'''
    This code is to predict the original character from a perturbed character 
'''
import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv 

train_dict={}
test_dict={}
similarity_dict={}
error_dict={}
test_file='noisy_test.csv'
def full_data():
    train_data=pd.read_csv('train.csv')
    for i in range(1,27):
        arr=[]
        for j in range(1,36):
            arr.append(train_data['x{}'.format(j)][i-1])
        train_dict[i]=arr
    
    # Testing Data
    test_data=pd.read_csv(test_file)
    test_length=len(test_data['x1'])
    for i in range(test_length):
        arr=[]
        for j in range(1,36):
            arr.append(test_data['x{}'.format(j)][i])
        test_dict['{}{}'.format(test_data['Label'][i],i)]=arr
    




def read_data():
    train_data=pd.read_csv('train.csv')
    for i in range(1,27):
        arr=[]
        for j in range(1,36):
            arr.append(train_data['x{}'.format(j)][i-1])
        train_dict[i]=arr
    
    test_data=pd.read_csv(test_file)
    for i in range(1,8):
        arr=[]
        for j in range(1,36):
            arr.append(test_data['x{}'.format(j)][i-1])
        test_dict[i]=arr  


def cosine_similarity(vecA,vecB):
    # vecA, vecB are here 35 dimension vector
    sum_sqrdA=0
    sum_sqrdB=0
    cosine_value=0
    for i in range(len(vecA)):
        sum_sqrdA+=vecA[i]**2
        sum_sqrdB+=vecB[i]**2
        cosine_value+=vecA[i]*vecB[i]
    cosine_value=cosine_value/(np.sqrt(sum_sqrdA)*np.sqrt(sum_sqrdB))
    return cosine_value

def print_similarity_dict():
    file=open('similarity.txt','w')
    for key,value in similarity_dict.items():
        file.write("{}:{}\n".format(key,value))
    file.close 
    print("Similarity dictioanry successfuly printed!!")
    
    # print(error_dict)
    file1=open('error.txt','w')
    for key,value in error_dict.items():
        file1.write("{}:{}\n".format(key,value))
    file1.close 
    print("Error dictioanry successfuly printed!!")
    

def analyze():
    total_count=0
    true_count=0
    for key,value in similarity_dict.items():
        total_count+=1
        if key[0]==value:
            true_count+=1
        else:
            error_dict[key]=value
    print("Correct prob.:{}({}/{}), Wrong Prob.:{}({}/{})".format(true_count/total_count,true_count,total_count,1-true_count/total_count,total_count-true_count,total_count))

def check_similarity():
    # read_data()
    full_data()
    character=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for ts_key,ts_value in test_dict.items():
        similarity=0
        similar_with=0
        for tr_key,tr_value in train_dict.items():
            sim=cosine_similarity(ts_value,tr_value)
            if sim>similarity:
                similar_with=tr_key
                similarity=sim
        similarity_dict[ts_key]=character[similar_with-1]
    # print(similarity_dict)
    analyze()# Make sure to call analyze function before calling print_similarity_dict(), otherwise no error_dict will print
    print_similarity_dict()
    

check_similarity()
# full_data()