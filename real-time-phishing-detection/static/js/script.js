function analyze() {
  const email = document.getElementById('emailContent').value.trim();
  const url = document.getElementById('url').value.trim();
  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = '<p>🔍 Analyzing...</p>';

  fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email_content: email, url: url })
  })
  .then(res => res.json())
  .then(data => {
    let html = '';

    if (data.email) {
      const cls = data.email.is_phishing ? 'phishing' : 'safe';
      html += `
        <div class="result-box ${cls}">
          <h3>📧 Email Analysis</h3>
          <p><strong>Status:</strong> ${data.email.warning}</p>
          <p><strong>Risk Score:</strong> ${data.email.risk_score}%</p>
          <h4>Suggestions:</h4>
          <ul>${data.email.suggestions.map(s => `<li>${s}</li>`).join('')}</ul>
        </div>`;
    }

    if (data.url) {
      const cls = data.url.is_phishing ? 'phishing' : 'safe';
      html += `
        <div class="result-box ${cls}">
          <h3>🌐 URL Analysis</h3>
          <p><strong>Status:</strong> ${data.url.warning}</p>
          <p><strong>Risk Score:</strong> ${data.url.risk_score}%</p>
          <h4>Suggestions:</h4>
          <ul>${data.url.suggestions.map(s => `<li>${s}</li>`).join('')}</ul>
        </div>`;
    }

    if (data.virustotal && data.virustotal.success) {
      html += `<div class="result-box" style="background:#eef;">
        <p>📤 ${data.virustotal.message}</p>
      </div>`;
    }

    resultsDiv.innerHTML = html;
  })
  .catch(err => {
    resultsDiv