import joblib
import re

model = joblib.load('../models/phishing_model.pkl')
vectorizer = joblib.load('../models/vectorizer.pkl')

def analyze_email_content(content):
    cleaned = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', content)
    cleaned = re.sub(r'[^a-zA-Z\s]', '', cleaned).lower()
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0].max()
    return {
        'is_phishing': bool(pred),
        'risk_score': round(prob * 100, 2),
        'warning': "🚨 Phishing Email!" if pred else "✅ Safe Email",
        'suggestions': ["Do not click links.", "Verify sender."] if pred else ["No threat detected."]
    }