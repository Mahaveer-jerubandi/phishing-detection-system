from flask import Flask, render_template, request, jsonify
from utils.email_analyzer import analyze_email_content
from utils.url_analyzer import analyze_url
from utils.virus_total import check_url_virustotal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    result = {}
    if data.get('email_content'):
        result['email'] = analyze_email_content(data['email_content'])
    if data.get('url'):
        result['url'] = analyze_url(data['url'])
        result['virustotal'] = check_url_virustotal(data['url'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)