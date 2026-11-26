import pandas as pd
from math import log
from math import exp
import numpy as np

feature_cols = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]

dataset = pd.read_csv('dataset_train.csv')

dataset_features = dataset[
        [
            "Arithmancy",
            "Astronomy",
            "Herbology",
            "Defense Against the Dark Arts",
            "Divination",
            "Muggle Studies",
            "Ancient Runes",
            "History of Magic",
            "Transfiguration",
            "Potions",
            "Care of Magical Creatures",
            "Charms",
            "Flying"
        ]
    ]

dataset_y = dataset["Hogwarts House"]

mapping = {"Slytherin" : 0,"Gryffindor":0, "Hufflepuff":0, "Ravenclaw":1}
print(dataset_y)

dataset_y = dataset_y.replace(mapping)

dataset_features_z = (dataset_features[feature_cols] - dataset_features[feature_cols].mean()) / dataset_features[feature_cols].std()
print(dataset_y)
print(dataset_features_z)

datas = np.array(
    [
         #arithman  #charms    #defense
        [-1.245520, -1.014194, 0.878628], # harry Potter
        [-1.055434, -1.137535, 1.365690], # Hermione Granger
        [-1.554729, -0.780078, 1.261379], # Ron Weasley
        [-1.040544, -1.533799, 1.830165]  # Neuville Londubat
    ])

# print(" nb line ", np.shape(datas)[0], " nb col ", np.shape(datas)[1])

thetas = np.array([4, 5, 6])

y = np.array([0,0,0,1])

def sigmoid (x):
    return 1/ (1 + exp(-x))

def scalar_product(data, thetas):
    if data.ndim != 1 or thetas.ndim !=1 :
        raise TypeError("scalar_product : vectors invalid")
    n_features = np.shape(data)[0]
    n_thetas = np.shape(thetas)[0]

    if n_features != n_thetas :
        raise TypeError(f"scalar product: le nombre de features ({n_features}) ne correspond pas au nombre de thetas ({n_thetas})")
    return np.dot(data, thetas)

def predict(data, thetas):
    return sigmoid(scalar_product(data, thetas))

def loss(datas, thetas, y):
    if y.ndim != 1 or thetas.ndim != 1:
        raise TypeError("loss: invalid vectors")

    n_line_datas = np.shape(datas)[0]
    n_result = np.shape(y)[0]
    n_features = np.shape(datas)[1]
    n_thetas = np.shape(thetas)[0]

    if n_line_datas !=n_result:
        raise TypeError(f"loss: le nombre d observation ({n_line_datas}) ne correspond pas au nombre de prediction ({n_result})")
    
    if n_features != n_thetas:
        raise ValueError(f"loss: le nombre de features ({n_features}) ne correspond pas au nombre de thetas ({n_thetas})")     

    cost = 0
    i = 0
    for i in range(n_line_datas):
        cost += log(predict(datas[i,:], thetas)) * y[i] + log(1-predict(datas[i,:], thetas)) * (1 - y[i])

    return (-cost) / n_line_datas

def train (datas, thetas, y, learning_rate):

    if y.ndim != 1 or thetas.ndim != 1:
        raise TypeError("loss: invalid vectors")
    
    n_line_datas = np.shape(datas)[0]
    n_result = np.shape(y)[0]
    n_features = np.shape(datas)[1]
    n_thetas = np.shape(thetas)[0]

    if n_line_datas !=n_result:
        raise TypeError(f"loss: le nombre d observation ({n_line_datas}) ne correspond pas au nombre de prediction ({n_result})")
    
    if n_features != n_thetas:
        raise ValueError(f"loss: le nombre de features ({n_features}) ne correspond pas au nombre de thetas ({n_thetas})")   

    new_theta = [0] * n_features

    # on va s occuper de la mise a jour de chaque theta un par un
    i_features = 0
    for i_features in range(n_features):
        i_line = 0
        errors = 0
        for i_line in range(n_line_datas):
            #print("line = ", i_line, "col = " ,i_features, " ", datas[i_line][i_features])
            errors += (predict(datas[i_line], thetas) - y[i_line]) * datas[i_line][i_features] 

        errors = errors / n_line_datas

        new_theta [i_features] = thetas[i_features] - learning_rate * errors

    print(new_theta)

#print(loss(datas, thetas, y))

train(datas, thetas, y, 0.01)


# print ("model\n", model(df_bidon, weights_bidon),"\n")

# def sigmoid (observations, weights):
#    return 1 / (1 + np.exp(model(observations, weights)))
    
# print("sigmoid\n", sigmoid(df_bidon, weights_bidon), "\n")

# def loss(observations, weights, result):
#    return np.sum( ((np.log(sigmoid(observations, weights))) * data_bidon_r) + (  (1 - (np.log(sigmoid(observations, weights)))) * (1 - result)   ) ) / (observations.shape[0])
    
# print(loss(df_bidon, weights_bidon, data_bidon_r))

#print(np.log(sigmoid(observations, weights)))





