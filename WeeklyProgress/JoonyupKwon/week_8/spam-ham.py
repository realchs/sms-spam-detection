import csv
import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
import random

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

def plot_normalized_data(x1,x2,x3,num):
    fig, ax = plt.subplots()
    temp = []
    for i in range(num):
        temp.append(i)
    ax.scatter(temp, x1, color='red', marker='o', label='Ham-Ham')
    ax.scatter(temp, x2, color='green', marker='s', label='Spam-Spam')
    ax.scatter(temp, x3, color='blue', marker='^', label='Ham-Spam')
    ax.set_title('Min-Max Normalized Data')
    ax.set_xlabel('Data index')
    ax.set_ylabel('Normalized Value')
    ax.legend()
    
    plt.show()


def test1(num1,num2,similarity1):
    filename_1 = "train_" + str(num1) + ".csv"
    filename_2 = "valid_" + str(num2) + ".csv"
    #filename_3 = str(num2) + ".csv"
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
    similarity1.append(temp)

def test2(num1,num2,similarity2):
    filename_1 = str(num1) + ".csv"
    filename_2 = str(num2) + ".csv"
    row1 = []
    row2 = []
    with open(filename_1, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row1.append(row[0])
    with open(filename_2, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row2.append(row[0])
    file.close()

    temp = jaccard_similarity(row1, row2)
    similarity2.append(temp)


def test3(num1,num2,similarity3):
    filename_1 = "train_" + str(num1) + ".csv"
    filename_2 = "valid_" + str(num1) + ".csv"
    filename_3 = str(num2) + ".csv"
    row1 = []
    row2 = []
    with open(filename_1, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row1.append(row[1])
    with open(filename_2, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row1.append(row[1])
    file.close()
    with open(filename_3, 'rt', encoding='UTF8') as file:
        reader = csv.reader(file)
        for row in reader:
            row2.append(row[0])

    temp = jaccard_similarity(row1, row2)
    similarity3.append(temp)


def init_run():
    similarity1 = []
    similarity2 = []
    similarity3 = []

    a_start = 1
    a_end = 9
    b_start = 1
    b_end = 9
    c_start = 1
    c_end = 133


    count = 1
    for i in range( a_start, (a_end+1) ):
        for j in range( b_start, (b_end+1) ):
            print("------------------Progress 1-",str(count),"-----------------")
            print("i : ", str(i))
            print("j : ", str(j))
            test1(i,j,similarity1)
            count = count + 1

    count = 1
    for x in range( c_start, (c_end+1) ):
        for y in range( (x+1), (c_end+1) ):
            print("------------------Progress 2-",str(count),"-----------------")
            print("x : ", str(x))
            print("y : ", str(y))
            test2(x,y,similarity2)
            count = count + 1

    count = 1
    for a in range( a_start, (a_end+1) ):
        for c in range( c_start, (c_end+1) ):
            print("------------------Progress 3-",str(count),"-----------------")
            print("a : ", str(a))
            print("c : ", str(c))
            test3(a,c,similarity3)
            count = count + 1

    num = 81
    similarity1 = random.sample(similarity1, num)
    similarity2 = random.sample(similarity2, num)
    similarity3 = random.sample(similarity3, num)

    norm_similarity = []
    norm_similarity.extend(similarity1)
    norm_similarity.extend(similarity2)
    norm_similarity.extend(similarity3)

    x = min_max_normalization_numpy(norm_similarity)
    x1 = x[0:(num)]
    x2 = x[num:((num*2))]
    x3 = x[(num*2):]

    print("-------------------Result-------------------")
    print("Jaccard Similarity1 : ", similarity1)
    print("Jaccard Similarity1_norm : ", x1)
    print("--------------------------------------------")
    print("Jaccard Similarity2 : ", similarity2)
    print("Jaccard Similarity2_norm : ", x2)
    print("--------------------------------------------")
    print("Jaccard Similarity3 : ", similarity3)
    print("Jaccard Similarity3_norm : ", x3)
    print("--------------------------------------------")


    plot_normalized_data(x1,x2,x3,num)



init_run()
