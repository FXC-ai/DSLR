import csv
from pprint import pprint

class Describe :

    statistics = dict()
    fields_name = list()

    def dict_statistic(self):
        return {"Count" : 0, "Mean": 0.0, "Std" : 0.0, "Max" : 0.0, "Quartile1": 0.0, "Quartile2":0.0, "Quartile3":0.0, "Min":0.0}

    def read_csv(self):
        with open('dataset_train.csv', 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f, delimiter=',')
            fieldnames = lecteur.fieldnames


            index = list()
            hogwarts_house = list()
            first_name = list()
            last_name = list()
            birthday = list()
            best_hand = list()
            arithmancy = list()
            astronomy = list()
            herbology = list()
            divination = list()
            muggle_studies = list()
            ancient_runes = list()
            history_of_magic = list()
            transfiguration = list()
            potions = list()
            care_of_magical_creatures = list()
            charms = list()
            flying = list()

            for field in fieldnames:
                self.statistics[field] = {"Count" : 0, "Mean": 0.0, "Std" : 0.0, "Max" : 0.0, "Quartile1": 0.0, "Quartile2":0.0, "Quartile3":0.0, "Min":0.0}

            pprint(self.statistics)

            for ligne in lecteur:
                for field in fieldnames:
                    if ligne[field] != "":
                        self.statistics[field]["Count"] += 1
                
                index.append(ligne["Index"])
                hogwarts_house.append(ligne["Hogwarts House"])
                first_name.append(ligne["First Name"])
                last_name.append(ligne["Last Name"])
                birthday.append(ligne["Birthday"])
                best_hand.append(ligne["Best Hand"])
                arithmancy.append(ligne["Arithmancy"])
                astronomy.append(ligne["Astronomy"])
                herbology.append(ligne["Herbology"])
                divination.append(ligne["Divination"])
                muggle_studies.append(ligne["Muggle Studies"])
                ancient_runes.append(ligne["Ancient Runes"])
                history_of_magic.append(ligne["History of Magic"])
                transfiguration.append(ligne["Transfiguration"])
                potions.append(ligne["Potions"])
                care_of_magical_creatures.append(ligne["Care of Magical Creatures"])
                charms.append(ligne["Charms"])
                flying.append(ligne["Flying"])
                if (ligne["Divination"] == ""):
                    print("Maquant = ", ligne["Index"])
                    print(ligne)

            print(len(charms))
            print(len(index))

describe = Describe()

describe.read_csv()