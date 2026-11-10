import csv
from pprint import pprint
from math import sqrt

class Describe :

    statistics = dict()
    fieldnames = list()

    def mark_accumulator(self, field, mark):
        self.statistics[field]["Mean"] += float(mark)

    def min(self, field, mark):
        if (self.statistics[field]["Min"] is None or float(self.statistics[field]["Min"]) > float(mark)):
            self.statistics[field]["Min"] = mark 

    def max(self, field, mark):
        if (self.statistics[field]["Max"] is None or float(self.statistics[field]["Max"]) < float(mark)):
            self.statistics[field]["Max"] = mark 

    def collect_data(self, field, ligne):
        self.mark_accumulator(field, mark=ligne[field])
        self.min(field, ligne[field])
        self.max(field, ligne[field])
        self.statistics[field]["values"].append(float(ligne[field]))

    def std(self, mean, obs, card):
        acc = 0.0
        for value in obs:
            acc += (value - mean)**2
        return sqrt(acc / card)

    def display(self):
        header = "               "
        for matter in self.fieldnames:
            if(matter not in ["First Name", "Last Name", "Index", "Hogwarts House", "Birthday", "Best Hand"]):
                header += matter[:20] + (23 - len(matter[:20])) * " "
        print(header)

        stats = ["Count", "Mean",  "Std", "Min", "Min", "Quartile1", "Quartile2", "Quartile3", "Max"]
        for stat in stats:
            space = (15 - len(stat)) * " "
            statline = stat + space
            for matter in self.statistics:
                if(matter not in ["First Name", "Last Name", "Index", "Hogwarts House", "Birthday", "Best Hand"]):
                    statline += str(self.statistics[matter][stat]) + (23 - len(str(self.statistics[matter][stat]))) * " "
            print(statline)


    def read_csv(self):
        with open('dataset_train_batch.csv', 'r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f, delimiter=',')
            self.fieldnames = lecteur.fieldnames

            for field in self.fieldnames:
                self.statistics[field] = {
                        "Count" : 0,
                        "Mean": 0.0,
                        "Std" : 0.0,
                        "Max" : None,
                        "Quartile1": 0.0,
                        "Quartile2":0.0,
                        "Quartile3":0.0,
                        "Min":None,
                        "values":[]
                        }

            #pprint(self.statistics)

            for ligne in lecteur:
                #print("Nous consdierons cette ligne : ", ligne["First Name"])
                for field in self.fieldnames:
                    if ligne[field] != "":
                        self.statistics[field]["Count"] += 1
                        # print("value = ", ligne[field])
                        match field:
                            case "Index":
                                pass
                            case "Hogwarts House":
                                pass
                            case "First Name":
                                pass
                            case "Last Name":
                                pass
                            case "Birthday":
                                pass
                            case "Best Hand":
                                pass
                            case "Arithmancy":
                                self.collect_data(field, ligne)
                            case "Astronomy":
                                self.collect_data(field, ligne)
                            case "Herbology":
                                self.collect_data(field, ligne)
                            case "Defense Against the Dark Arts":
                                self.collect_data(field, ligne)
                            case "Divination":
                                self.collect_data(field, ligne)
                            case "Muggle Studies":
                                self.collect_data(field, ligne)
                            case "Ancient Runes":
                                self.collect_data(field, ligne)
                            case "History of Magic":
                                self.collect_data(field, ligne)
                            case "Transfiguration":
                                self.collect_data(field, ligne)
                            case "Potions":
                                self.collect_data(field, ligne)
                            case "Care of Magical Creatures":
                                self.collect_data(field, ligne)
                            case "Charms":
                                self.collect_data(field, ligne)
                            case "Flying":
                                self.collect_data(field, ligne)
                            case _:
                                pass


        for matter in self.statistics:
            if(matter not in ["First Name", "Last Name", "Index", "Hogwarts House", "Birthday", "Best Hand"]):
                self.statistics[matter]['Mean'] = self.statistics[matter]["Mean"] / self.statistics[matter]["Count"]
                self.statistics[matter]["values"].sort()
                print("index = ", int(self.statistics[matter]["Count"] / 4), " ", self.statistics[matter]["values"])
                self.statistics[matter]["Quartile1"] = self.statistics[matter]["values"][int(self.statistics[matter]["Count"] / 4)]
                self.statistics[matter]["Quartile2"] = self.statistics[matter]["values"][int(self.statistics[matter]["Count"] / 4) * 2]
                self.statistics[matter]["Quartile3"] = self.statistics[matter]["values"][int(self.statistics[matter]["Count"] / 4) * 3]
                self.statistics[matter]["Std"] = self.std(self.statistics[matter]["Mean"], self.statistics[matter]["values"], self.statistics[matter]["Count"])
                # print("matter ", matter, self.statistics[matter]["Mean"])
                # matter["Mean"] = matter["Mean"] / matter["Count"]
        pprint(self.statistics)


describe = Describe()

describe.read_csv()
describe.display()
