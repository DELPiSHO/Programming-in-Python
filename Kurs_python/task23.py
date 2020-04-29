import os
import operator
with open('dataset_3363_3.txt') as input,open('answer.txt','w') as output:
    dict = {}
    for word in input.read().split():
        if (word not in dict):
            dict[word] = 1
        else:
            dict[word]+=1
    maximum = max(dict,key=dict.get)
    print(maximum,dict[maximum])
    for word,count in dict.items():
        print(word,count)