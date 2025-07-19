import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    "email_length": [100, 500, 150, 300],
    "url_length": [20, 50, 15, 60],
    "label": [0, 1, 0, 1]
})

X = data[["email_length", "url_length"]]
y = data["label"]

clf = RandomForestClassifier()
clf.fit(X, y)

joblib.dump(clf, "app/ml_model.pkl")
