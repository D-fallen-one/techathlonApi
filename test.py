import pandas as pd
from api.models import Books
def fun():
    rawdata = pd.read_csv("booksRated.csv")
    rawdata.shape
    for i in range(102705, rawdata.shape[0]):
        od = rawdata.iloc[i].values
        b = Books(od[0],od[1],od[2],od[3],od[4],od[5],od[6],od[7],od[8],od[9])
        b.save()
        print(i)
