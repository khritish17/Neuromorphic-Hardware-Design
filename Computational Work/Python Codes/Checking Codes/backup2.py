'''
    This program checks how many bit flips requires to change a character 
    to another, ex. A -> H
'''
import numpy as np
import pandas as pd 
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

def bit_flip(vecA,vecB):
    bit_flips=0
    for i in range(len(vecA)):
        if not vecA[i]==vecB[i]:
            bit_flips+=1
    return bit_flips


def check_letters():
    # First import all the datas into a dictionary
    # check with each alphabet
    # produce those are more similar to each other
    data=pd.read_csv('train.csv')
    letter_arr=np.ndarray((26,35))
    # print(data['x1'][25])
    # print(data['Label'][0])
    for i in range(26):
        arr=[]
        for j in range(1,36):
            arr.append(data['x{}'.format(j)][i])
        letter_arr[i]=arr
    
    # Now check for 
    # print(letter_arr[0])
    character=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    bit_tollerance=3
    similar_character={}
    for i in range(26):
        char_arr=[]
        for j in range(i+1,26):
            vecA=letter_arr[i]
            vecB=letter_arr[j]
            bit_change=bit_flip(vecA,vecB)
            if bit_change<=bit_tollerance:
                char_arr.append(character[j])
        similar_character[character[i]]=char_arr
    print(similar_character)





check_letters()
# print(cosine_similarity([1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0]))
# print(bit_flip([1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0]))