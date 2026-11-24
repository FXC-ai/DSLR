
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
import plotly.express as px

import plotly.graph_objects as go

# https://mrmint.fr/logistic-regression-machine-learning-introduction-simple
# https://www.datacamp.com/fr/tutorial/understanding-logistic-regression-python
# https://www.ibm.com/fr-fr/think/topics/logistic-regression
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')



df = dataset[
    [
        "Hogwarts House",
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination","Muggle Studies",
        "Ancient Runes","History of Magic",
        "Transfiguration","Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"]
    ]

"""

df = df['Hogwarts House'].replace(hogwarts_house_color)

"""
hogwarts_house = ["Hufflepuff", "Gryffindor", "Ravenclaw", "Slytherin"]
hogwarts_house_color = dict(Hufflepuff="#f1f422", Gryffindor="#c7462f", Ravenclaw="#3333af", Slytherin="#294103")

index_vals = df['Hogwarts House'].replace(hogwarts_house_color)

print(type(index_vals), index_vals)

fig = go.Figure(data=go.Splom(
                dimensions = [
                    dict(label='Arithmancy'[:12], values=df['Arithmancy']),
                    dict(label='Astronomy'[:12], values=df['Astronomy']),
                    dict(label='Herbology'[:12], values=df['Herbology']),
                    dict(label='Defense Against the Dark Arts'[:12], values=df['Defense Against the Dark Arts']),
                    dict(label='Divination'[:12], values=df['Divination']),
                    dict(label='Muggle Studies'[:12], values=df['Muggle Studies']),
                    dict(label='Ancient Runes'[:12], values=df['Ancient Runes']),
                    dict(label='History of Magic'[:12], values=df['History of Magic']),
                    dict(label='Transfiguration'[:12], values=df['Transfiguration']),
                    dict(label='Potions'[:12], values=df['Potions']),
                    dict(label='Care of Magical Creatures'[:12], values=df['Care of Magical Creatures']),
                    dict(label='Charms'[:12], values=df['Charms']),
                    dict(label='Flying'[:12], values=df['Flying'])
                ],
                diagonal_visible=False,
                showupperhalf=False,
                text=df['Hogwarts House'],
                marker=dict(color=index_vals,
                            showscale=False, # colors encode categorical variables
                            line_color='white',
                            line_width=0.5)
                ))


fig.update_layout(
    margin=dict(l=200),  # Augmente l'espace à gauche (valeur par défaut : 80)
    height=1400,
    title=dict(text='Pair of marks for each matter'),
)

fig.show()



