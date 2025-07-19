import joblib

model = joblib.load("app/ml_model.pkl")

PHISHING_KEYWORDS = ["urgent", "password", "verify", "login", "account", "click", "confirm"]

def analyze_email_content(content):
    content = content.lower()
    for keyword in PHISHING_KEYWORDS:
        if keyword in content:
            return "Suspicious Content Found"
    return "Content Looks Clean"

def check_url_with_virustotal(url):
    if "phish" in url:
        return "Suspicious URL Found"
    return "URL Looks Clean"

def predict_phishing(email_content, url):
    features = [len(email_content), len(url)]
    prediction = model.predict([features])[0]
    return "Phishing Detected" if prediction == 1 else "Legitimate"
