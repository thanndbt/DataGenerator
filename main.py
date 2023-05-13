import pandas as pd
import random

######## FUNCTIONS ########
def valueSelector(col):
    return str(random.choice(list(filter(('').__ne__, col.to_list()))))

def mergeField(*cols):
    data = str()
    for col in cols:
        data = str(data + ' ' + str(valueSelector(col)).strip())
    return data

def generateName(amount, *inp):
    for n in range(amount):
        print(mergeField(inp))

######## LOADING FILES ########
names = pd.read_csv('./data/nl/names.csv', na_filter=False)

######## MAIN ########

generateName(5, names["first_names"], names["affixes"], names["surnames"])
