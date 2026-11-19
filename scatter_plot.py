
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
import plotly.express as px

# https://mrmint.fr/logistic-regression-machine-learning-introduction-simple
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')

print(dataset)

df = dataset[["Hogwarts House", "Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]]

fig = px.scatter_matrix(df,
    dimensions=[
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
    "Flying"],
    color="Hogwarts House")
fig.show()

""" import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# https://mrmint.fr/logistic-regression-machine-learning-introduction-simple
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')

print(dataset)

 """