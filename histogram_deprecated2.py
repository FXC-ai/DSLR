import seaborn as sns
import matplotlib
import pandas as pd
from sklearn.preprocessing import PowerTransformer

# pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
dataset = pd.read_csv('dataset_train.csv')
matters = [
    "Arithmancy",
    "Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]

dataset_matter = dataset[["Hogwarts House", "Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]]

print (dataset_matter)

sns.set_theme()

fig, graph_grid = matplotlib.pyplot.subplots(3, 5, figsize=(10, 8), layout="constrained")

for graph, matter in zip(graph_grid.flat, matters):
    print(graph, matter)
    sns.histplot(data=dataset_matter, x=matter, hue="Hogwarts House", ax=graph, legend=(matter == "Arithmancy"))
    # graph.set_title(f"{matter}")

empty_graph = graph_grid.flat[14]
empty_graph.axis("off")

sns.move_legend(
    graph_grid.flat[0],
    loc="center",
    bbox_to_anchor=(0.5, 0.5),  # Position au-dessus de la grille
    bbox_transform=empty_graph.transAxes,
    ncol=2   # Référentiel de la figure entière
      
)

matplotlib.pyplot.show()