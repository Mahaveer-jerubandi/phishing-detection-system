import tldextract
import re

def analyze_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"

    score = 0
    if 'login' in url.lower() or 'verify' in url.lower(): score += 20
    if len(url) > 75: score += 15
    if not url.startswith('https'): score += 25
    if any(s in url for s in ['bit.ly', 'goo.gl']): score += 30
    if re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', url): score += 30

    risk_score = min(score, 100)
    is_phishing = risk_score > 50
    return {
        'is_phishing': is_phishing,
        'risk_score': risk_score,
        'warning': "🚨 Suspicious URL!" if is_phishing else "✅ Safe URL",
        'suggestions': ["Avoid entering info.", "Check domain."] if is_phishing else ["URL appears safe."]
    }