import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# X1 = scaler.transform([X.loc[0]])
# print(model.predict(X1))
def Get_Data(l):
    l = list(l.values())[:-1]
    l = np.array(l).astype(float)
    return l


def Scale(l):
    l = [l]
    scaler = MinMaxScaler()
    df = pd.read_csv("./Datasets/fetal_health (2).csv")
    X = df.drop("fetal_health", axis=1)
    Y = df["fetal_health"]
    features = [0, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 16, 19]
    X = X[X.columns[features]]
    X_scale = scaler.fit_transform(X.values)

    l = scaler.transform(l)
    return l

model = pkl.load(open("./Model/FETAL_HEALTH_AI_RF.sav", "rb"))
