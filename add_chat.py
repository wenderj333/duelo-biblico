with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# CSS do chat
css_chat = b"""
        .chat-bolha {
            position: fixed; bottom: 20px; right: 20px; z-index: 1000;
        }
        .chat-toggle {
            width: 50px; height: 50px; border-radius: 50%;
            background: linear-gradient(135deg,#f6d860,#e5b800);
            border: none; cursor: pointer; font-size: 22px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            display: flex; align-items: center; justify-content: center;
        }
        .chat-box {
            display: none; position: absolute; bottom: 60px; right: 0;
            width: 280px; background: #1a0a3e;
            border: 1px solid rgba(246,216,96,0.3);
            border-radius: 14px; overflow: hidden;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        }
        .chat-header {
            padding: 10px 14px; background: linear-gradient(135deg,#3d1a7a,#6c47d4);
            font-size: 13px; font-weight: 700; color: #f6d860;
        }
        .chat-msgs {
            height: 200px; overflow-y: auto; padding: 10px;
            display: flex; flex-direction: column; gap: 6px;
        }
        .chat-msg { font-size: 12px; padding: 6px 10px; border-radius: 10px; max-width: 85%; }
        .chat-msg.eu { background: rgba(246,216,96,0.2); color: white; align-self: flex-end; }
        .chat-msg.op { background: rgba(255,255,255,0.1); color: white; align-self: flex-start; }
        .chat-input-row { display: flex; gap: 6px; padding: 8px; border-top: 1px solid rgba(255,255,255,0.1); }
        .chat-input { flex: 1; padding: 7px 10px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.07); color: white; font-size: 12px; }
        .chat-send { padding: 7px 12px; border-radius: 8px; border: none; background: #f6d860; color: #1a0a3e; font-weight: 700; cursor: pointer; font-size: 12px; }
        .chat-msgs-rapidas { display: flex; flex-wrap: wrap; gap: 4px; padding: 6px 8px; border-top: 1px solid rgba(255,255,255,0.08); }
        .msg-rapida { padding: 3px 8px; border-radius: 10px; border: 1px solid rgba(246,216,96,0.3); background: transparent; color: #f6d860; font-size: 10px; cursor: pointer; }
"""
content = content.replace(b'/* Ranking lista */', css_chat + b'/* Ranking lista */', 1)

# HTML do chat
html_chat = b"""
<!-- CHAT BOLHA -->
<div class="chat-bolha" id="chat-bolha" style="display:none;">
    <div class="chat-box" id="chat-box">
        <div class="chat-header">&#x1F4AC; Chat com oponente</div>
        <div class="chat-msgs" id="chat-msgs"></div>
        <div class="chat-msgs-rapidas" id="msgs-rapidas">
            <button class="msg-rapida" onclick="enviarMsgRapida('Amem!')">Amem!</button>
            <button class="msg-rapida" onclick="enviarMsgRapida('Boa pergunta!')">Boa pergunta!</button>
            <button class="msg-rapida" onclick="enviarMsgRapida('Bom jogo!')">Bom jogo!</button>
            <button class="msg-rapida" onclick="enviarMsgRapida('Gloria a Deus!')">Gloria a Deus!</button>
        </div>
        <div class="chat-input-row">
            <input class="chat-input" id="chat-input" placeholder="Mensagem..." onkeydown="if(event.key==='Enter')enviarChat()">
            <button class="chat-send" onclick="enviarChat()">&#x27A4;</button>
        </div>
    </div>
    <button class="chat-toggle" onclick="toggleChat()" id="chat-btn">&#x1F4AC;</button>
</div>
"""
content = content.replace(b'</body>', html_chat + b'</body>', 1)

# JS do chat
js_chat = b"""
// ===== CHAT =====
let chatAberto = false;
let chatNovaMensagem = false;

function toggleChat(){
    chatAberto = !chatAberto;
    document.getElementById("chat-box").style.display = chatAberto ? "block" : "none";
    if(chatAberto){ chatNovaMensagem=false; document.getElementById("chat-btn").innerText="x"; }
    else { document.getElementById("chat-btn").innerHTML="&#x1F4AC;"; }
}

function enviarChat(){
    const input = document.getElementById("chat-input");
    const msg = input.value.trim();
    if(!msg || !socket || !salaAtual) return;
    socket.emit("chatMsg", {salaId: salaAtual, msg: msg, nome: window.meuNomeGlobal});
    adicionarMsgChat(window.meuNomeGlobal, msg, true);
    input.value = "";
}

function enviarMsgRapida(msg){
    if(!socket || !salaAtual) return;
    socket.emit("chatMsg", {salaId: salaAtual, msg: msg, nome: window.meuNomeGlobal});
    adicionarMsgChat(window.meuNomeGlobal, msg, true);
}

function adicionarMsgChat(nome, msg, eu){
    const div = document.getElementById("chat-msgs");
    const el = document.createElement("div");
    el.className = "chat-msg " + (eu ? "eu" : "op");
    el.textContent = eu ? msg : nome+": "+msg;
    div.appendChild(el);
    div.scrollTop = div.scrollHeight;
    if(!eu && !chatAberto){
        document.getElementById("chat-btn").innerHTML="&#x1F4AC; &#x1F534;";
    }
}
"""
content = content.replace(b'// ===== RANKING =====', js_chat + b'// ===== RANKING =====', 1)

# Socket para receber chat
socket_chat = b"""
    socket.on("chatMsg", function(d){
        if(d.nome !== window.meuNomeGlobal) adicionarMsgChat(d.nome, d.msg, false);
    });
"""
content = content.replace(b'socket.on("desafioRecebido"', socket_chat + b'socket.on("desafioRecebido"', 1)

# Mostrar chat quando jogo comecar
content = content.replace(
    b'document.getElementById("jogo").style.display="block";',
    b'document.getElementById("jogo").style.display="block";\n        document.getElementById("chat-bolha").style.display="block";\n        document.getElementById("chat-msgs").innerHTML="";'
)

# Esconder chat quando jogo acabar
content = content.replace(
    b'document.getElementById("resultado").style.display="block";',
    b'document.getElementById("resultado").style.display="block";\n        document.getElementById("chat-bolha").style.display="none";'
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Chat adicionado!')
