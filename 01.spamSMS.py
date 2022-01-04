import nltk     as nltk # ga guna sih pake as, biar keliatan rapi aja haha
import numpy    as np
import pandas   as pd

dataset = open("Natural-Language-Processing/data/SMSSpamCollection.tsv", "r").read()
parsedData = dataset.replace('\t', '\n').split('\n')

dataLabel = parsedData[0::2]
dataText = parsedData[1::2]

tableData = pd.DataFrame (
    {
        'label' : dataLabel[:-1],
        'text'  : dataText
    }
)

print(tableData.head())