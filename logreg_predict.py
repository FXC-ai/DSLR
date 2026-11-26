import pandas as pd
from math import log
from math import exp
import numpy as np

thetas = np.array(
    [
        0.17702106,
        -0.79490125,
        0.57079987,
        0.79490125,
        0.47317897,
        1.48024781,
        1.12981636,
        0.08037559,
        0.1248873,
        0.02466188,
        0.01231237,
        1.16439635,
        0.02531483,
    ]
)

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

dataset = pd.read_csv('dataset_train.csv').dropna()

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

mapping = {"Slytherin" : 0, "Gryffindor":0, "Hufflepuff":0, "Ravenclaw":1}
dataset_y = dataset_y.replace(mapping)
dataset_y = dataset_y.to_numpy()

dataset_features_z = (dataset_features[feature_cols] - dataset_features[feature_cols].mean()) / dataset_features[feature_cols].std()
dataset_features_z = dataset_features_z.to_numpy()

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


i = 0
p_p = 0
n_n = 0
p_n = 0
n_p = 0
for student in dataset_features_z:
    r= predict(student, thetas)
    if r <= 0.5:
        if dataset.iloc[i, dataset.columns.get_loc('Hogwarts House')] != "Ravenclaw":
            print(r, "\033[94m", "=> Something", dataset.iloc[i, dataset.columns.get_loc('Hogwarts House')], "\033[0m")
            n_n += 1
        else:
            print(r, "\033[94m", "=> Something", dataset.iloc[i, dataset.columns.get_loc('Hogwarts House')], "\033[0m")

            p_n +=1
    else:
        if dataset.iloc[i, dataset.columns.get_loc('Hogwarts House')] != "Ravenclaw":
            print(r,"\033[91m", "=> Ravenclaw","\033[0m", dataset.iloc[i, dataset.columns.get_loc('Hogwarts House')], "\033[0m")
            n_p += 1
        else:
            print(r,"\033[94m", "=> Ravenclaw","\033[0m", dataset.iloc[i, dataset.columns.get_loc('Hogwarts House')], "\033[0m")
            p_p +=1
    i+=1

print (p_p, n_n, p_n, n_p)
print(p_p + n_n, p_n + n_p)
print((p_p + n_n) / (p_p + n_n + p_n + n_p))

