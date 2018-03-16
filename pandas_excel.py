import pandas as pd
data=pd.read_csv("Accidents_2015.csv",low_memory="False")
print("total number of rows:{0}".format(len(data)))
print(list(data))  