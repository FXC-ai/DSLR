import seaborn as sns
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')

hogwarts_house_list = []
matters_list = []
values = []
diff = []

dataset_house_matter = dataset[["Hogwarts House", "Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]]

hogwarts_house = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
matters = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]

resultat = dataset_house_matter.groupby("Hogwarts House")[
    ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
].std()

# print(resultat)

for matter in matters:
    resultat[matter] = resultat[matter]  / resultat[matter].abs().max()

for matter in matters:
    tmp = []
    for house in hogwarts_house:
        hogwarts_house_list.append(house)
        matters_list.append(matter)
        values.append(resultat.at[house, matter])
        tmp.append(resultat.at[house, matter])
    diff.append((matter, float(max(tmp) - min(tmp))))

data_diff = df = pd.DataFrame(diff, columns=['Matter', 'Score'])

data = {
    "Categorie": hogwarts_house_list,
    "SousCategorie": matters_list,
    "Valeur": values
}

df = pd.DataFrame(data)
#df["Valeur"] = df["Valeur"] / df["Valeur"].abs().max()
# df["Valeur"] = (df["Valeur"] - df["Valeur"].min()) / (df["Valeur"].max() - df["Valeur"])

# print(df)

sns.set_theme()

plt.figure()
sns.barplot(
    data=df,
    x="SousCategorie",
    y="Valeur",
    hue="Categorie"
)

plt.figure()
sns.barplot(
    data=data_diff,
    x="Matter",
    y="Score",
)


matplotlib.pyplot.show()