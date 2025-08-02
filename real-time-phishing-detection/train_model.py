import pandas as pd
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import os

def clean_text(text):
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

df = pd.read_csv('data/phishing_dataset.csv')
df['cleaned'] = df['text'].apply(clean_text)

vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(df['cleaned'])
y = df['label']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/phishing_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')
print("✅ Model and vectorizer saved!")