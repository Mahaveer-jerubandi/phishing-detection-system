import requests
API_KEY = "YOUR_VIRUSTOTAL_API_KEY"

def check_url_virustotal(url):
    try:
        resp = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data={'apikey': API_KEY, 'url': url})
        return {'success': True, 'message': 'Submitted to VirusTotal.'}
    except:
        return {'success': False, 'message': 'API error.'}