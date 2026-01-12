import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.DataFrame([
    [45,28.4,130,160,85,1],
    [30,22.1,120,110,72,0]
], columns=["age","bmi","bp","glucose","heart_rate","risk"])

X = data.drop("risk", axis=1)
y = data["risk"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl","wb"))
print("Model saved")

