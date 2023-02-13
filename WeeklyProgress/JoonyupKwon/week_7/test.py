import csv
import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    intersection = len(s1.intersection(s2))
    union = (len(s1) + len(s2)) - intersection
    return float(intersection / union)

def min_max_normalization_numpy(data):
    data_min = np.min(data)
    data_max = np.max(data)
    normalized_data = (data - data_min) / (data_max - data_min)
    return normalized_data

def plot_normalized_data(normalized_data):
    plt.plot(range(len(normalized_data)), normalized_data, 'ro')
    plt.title('Min-Max Normalized Data')
    plt.xlabel('Data index')
    plt.ylabel('Normalized Value')
    plt.show()

def test(num1,num2,similarity):
    filename_1 = "train_" + str(num1) + ".csv"
    filename_2 = "valid_" + str(num2) + ".csv"
    row1 = []
    row2 = []
    with open(filename_1, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row1.append(row[1])
    with open(filename_2, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row2.append(row[1])
    file.close()

    temp = jaccard_similarity(row1, row2)
    similarity.append(temp)
    return temp

def init_run():
    similarity = []
    a_start = 1
    a_end = 9 
    b_start = 1
    b_end = 9

    count = 1
    check = []
    for i in range( a_start, (a_end+1) ):
        for j in range( b_start, (b_end+1) ):
            print("------------------Progress",str(count),"-----------------")
            print("i : ", str(i))
            print("j : ", str(j))
            temp = test(i,j,similarity)
            if(i==j):
                check.append(temp)
            count = count + 1

    x = min_max_normalization_numpy(similarity)

    plot_normalized_data(x)
    for i in range(len(similarity)):
        for j in range(len(check)):
            if(i == j):
                similarity[i] = " < " + str(check) + " > "

    print("-------------------Result-------------------")
    print("Jaccard Similarity: ", similarity)
    print("--------------------------------------------")

init_run()