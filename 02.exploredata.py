import pandas as pd

fullDataSet = pd.read_csv("Natural-Language-Processing/data/SMSSpamCollection.tsv", sep="\t", header=None)
fullDataSet.columns = ["label", "text"]

print(fullDataSet.head())

print("Input data has {} rows and {} columns".format(fullDataSet.shape[0], fullDataSet.shape[1]))
print("Out of {} rows, {} are labeled as spam and {} are ham".format(fullDataSet.shape[0], fullDataSet[fullDataSet["label"] == "spam"].shape[0], fullDataSet[fullDataSet["label"] == "ham"].shape[0]))
print("Number of null data is {}".format(fullDataSet["text"].isnull().sum()))