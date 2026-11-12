import seaborn as sns
import matplotlib
import pandas as pd


dataset = pd.read_csv('dataset_train.csv')

print(dataset)

dataset_house_matter = dataset[["Hogwarts House", "Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]]

resultat = dataset_house_matter.groupby('Hogwarts House')[["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]].std()

print(resultat.head(), type(resultat))


data = {
    "Categorie": ["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"],
    "SousCategorie": ["S1", "S2", "S3", "S4", "S1", "S2", "S3", "S4", "S1", "S2", "S3", "S4"],
    "Valeur": [10, 15, 8, 12, 5, 20, 14, 9, 18, 12, 16, 11]
}

df = pd.DataFrame(data)

print(df)

sns.set_theme()

sns.barplot(
    data=df,
    x="Categorie",
    y="Valeur",
    hue="SousCategorie"
)

matplotlib.pyplot.show()