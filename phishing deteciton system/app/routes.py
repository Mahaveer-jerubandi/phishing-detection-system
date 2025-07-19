from flask import render_template, request
from app import app
from app.utils import analyze_email_content, check_url_with_virustotal, predict_phishing

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    email_content = request.form["email_content"]
    url = request.form["url"]

    content_flag = analyze_email_content(email_content)
    url_flag = check_url_with_virustotal(url)
    ml_prediction = predict_phishing(email_content, url)

    return render_template("index.html", content_flag=content_flag, url_flag=url_flag, ml_prediction=ml_prediction)
