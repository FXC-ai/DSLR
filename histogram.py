import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# https://mrmint.fr/logistic-regression-machine-learning-introduction-simple
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')

print(dataset)
matters = [
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
    "Flying"]


hogwarts_house = ["Hufflepuff", "Gryffindor","Slytherin","Ravenclaw"]
hogwarts_house_colors = {"Hufflepuff":"#ECD75B", "Gryffindor":"#AA0001","Slytherin":"#3B0B65","Ravenclaw":"#144B09"}
nb_row = 4
nb_col = 4


dataset_matter = dataset[["Hogwarts House", "Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]]



fig = make_subplots(
    rows=nb_row, 
    cols=nb_col, 
    subplot_titles=matters)

for idx, matter in enumerate(matters):
    row = (idx // nb_row) + 1
    col_pos = (idx % nb_col) + 1

    for house in hogwarts_house:
        subset = dataset_matter[dataset_matter["Hogwarts House"] == house]

        fig.add_trace(
            go.Histogram
            (
                x=subset[matter],
                name=house,
                showlegend=(idx == 0),
                marker_color=hogwarts_house_colors.get(house),
                opacity=0.75,
                nbinsx=30
            ),
            row=row, 
            col=col_pos
        ) 

fig.update_layout(
    barmode="overlay",
    height=1400,
    width=1200,
    title_text="Distribution des notes par maison de Poudlard"
)

fig.show()