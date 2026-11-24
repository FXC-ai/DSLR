from sklearn.linear_model import LogisticRegression
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
#print(dataset_features_z)


data_bidon = {
    "Arithmancy": [18.0, 2.0, 16.0],
    "Astronomy" : [7, 12, 14],
    "Herbology" : [2, 20, 4],
    "Charms"    : [17, 10, 9]
}

weights_bidon = np.array([1000, 100, 10, 1])

df_bidon = pd.DataFrame(data_bidon)
print(df_bidon.to_numpy())

print(df_bidon)
print("\n")
print(weights_bidon)
print("\n")

def model(dataset, weights : pd.Series):
    return np.sum(dataset * weights, axis = 1)
    
print(model(df_bidon, weights_bidon))

def sigmoid (observation : pd.Series, weights : pd.Series):
    return 1 / (1 + exp(model(observation=observation, weights=weights)))

def loss(dataset : pd.DataFrame ,house_hogwart : int, observation : pd.Series, weights : pd.Series):
    
    for index, row in dataset.iterrows():
        print(index, row["colonne_a"])
    #dataset * weights
    #return [log(sigmoid(observation, weights)) * house_hogwart ] + [(1 - house_hogwart) * log(1 - sigmoid(observation, weights))]

