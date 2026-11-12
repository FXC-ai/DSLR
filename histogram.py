import seaborn as sns
import matplotlib
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')


dataset_house_matter = dataset[["Hogwarts House", "Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]]

matters = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]

resultat = dataset_house_matter.groupby("Hogwarts House")[
    [
        "Arithmancy",
    ]
].sum()

resultat = resultat.T

resultat = resultat.reset_index()

print(resultat)


resultat = resultat.melt()

print(resultat.head(25))

resultat.rename(columns={'Hogwarts House' : 'value'}, inplace=True)

# resultat.plot(kind='bar')

""" data = {
    "Categorie": ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"],
    "SousCategorie": ["S1", "S2", "S3", "S4", "S1", "S2", "S3", "S4", "S1", "S2", "S3", "S4"],
    "Valeur": [10, 15, 8, 12, 5, 20, 14, 9, 18, 12, 16, 11]
}

df = pd.DataFrame(data)


sns.set_theme()

sns.barplot(
    data=df,
    x="Categorie",
    y="Valeur",
    hue="SousCategorie"
)
"""
matplotlib.pyplot.show()