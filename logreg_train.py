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

dataset_features_z = (dataset_features[feature_cols] - dataset_features[feature_cols].mean()) / dataset_features[feature_cols].std()
#print(dataset_features)
# print(dataset_features_z)

data_bidon = {
    "Arithmancy": [-1.24552,  -1.014194,  0.878628],
    "Astronomy" : [-1.055434, -1.137535,  1.365690],
    "Herbology" : [-1.554729, -0.780078,  1.261379 ],
    "Charms"    : [-1.040544, -1.533799,  1.830165]
}

weights_bidon = np.array([1.1, 0.9, .07, 1.4])

data_bidon_r = np.array([0,0,1])


df_bidon = pd.DataFrame(data_bidon).to_numpy()

def model(dataset, weights ):
    return np.sum(dataset * weights, axis = 1)

print ("model\n", model(df_bidon, weights_bidon),"\n")

def sigmoid (observations, weights):
    return 1 / (1 + np.exp(model(observations, weights)))
    
print("sigmoid\n", sigmoid(df_bidon, weights_bidon), "\n")

def loss(observations, weights, result):
    return np.sum( ((np.log(sigmoid(observations, weights))) * data_bidon_r) + (  (1 - (np.log(sigmoid(observations, weights)))) * (1 - result)   ) ) / (observations.shape[0])
    
print(loss(df_bidon, weights_bidon, data_bidon_r))

#print(np.log(sigmoid(observations, weights)))





