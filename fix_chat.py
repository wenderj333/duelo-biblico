with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Adicionar CSS do chat
old_css = "        #jogo { display: none; }"
new_css = """        #jogo { display: none; }
        .chat-jogo { margin-top:10px; border-top:1px solid rgba(255,255,255,0.1); padding-top:10px; }
        .chat-msgs { max-height:80px; overflow-y:auto; margin-bottom:6px; }
        .chat-msg { font-size:11px; padding:3px 8px; border-radius:8px; margin-bottom:3px; display:inline-block; max-width:90%; }
        .chat-msg.eu { background:rgba(240,192,64,0.2); color:#f0c040; float:right; clear:both; }
        .chat-msg.oponente { background:rgba(255,255,255,0.1); color:white; float:left; clear:both; }
        .chat-rapido { display:flex; flex-wrap:wrap; gap:4px; }
        .chat-rapido button { padding:4px 8px; border-radius:12px; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.08); color:white; font-size:10px; cursor:pointer; }
        .chat-rapido button:hover { background:rgba(240,192,64,0.2); border-color:#f0c040; }"""
c = c.replace(old_css, new_css)

# Adicionar HTML do chat dentro do jogo
old_jogo = '<p class="notif-oponente" id="notifOponente">Oponente ja respondeu!</p>'
new_jogo = '''<p class="notif-oponente" id="notifOponente">Oponente ja respondeu!</p>
        <div class="chat-jogo" id="chat-jogo" style="display:none;">
            <div class="chat-msgs" id="chat-msgs"></div>
            <div class="chat-rapido" id="chat-rapido"></div>
        </div>'''
c = c.replace(old_jogo, new_jogo)

# Adicionar mensagens rapidas ao UI_TEXTOS
old_ui = 'ro:{procurando:"Asteptand un adversar...",oponente:"Adversar"'
new_ui = 'ro:{procurando:"Asteptand un adversar...",oponente:"Adversar",chat:["Buna intrebare!","Ai fost rapid!","Noroc!","Haide!","Bravo!"]'
c = c.replace(old_ui, new_ui)

old_pt = 'pt:{procurando:"Aguardando um irmao para o duelo...",oponente:"Oponente"'
new_pt = 'pt:{procurando:"Aguardando um irmao para o duelo...",oponente:"Oponente",chat:["Boa pergunta!","Foste rapido!","Boa sorte!","Vai la!","Parabens!"]'
c = c.replace(old_pt, new_pt)

old_en = 'en:{procurando:"Waiting for an opponent...",oponente:"Opponent"'
new_en = 'en:{procurando:"Waiting for an opponent...",oponente:"Opponent",chat:["Good question!","You were fast!","Good luck!","Go for it!","Well done!"]'
c = c.replace(old_en, new_en)

old_es = 'es:{procurando:"Esperando un oponente...",oponente:"Oponente"'
new_es = 'es:{procurando:"Esperando un oponente...",oponente:"Oponente",chat:["Buena pregunta!","Fuiste rapido!","Buena suerte!","Vamos!","Bien hecho!"]'
c = c.replace(old_es, new_es)

old_fr = 'fr:{procurando:"En attente d un adversaire...",oponente:"Adversaire"'
new_fr = 'fr:{procurando:"En attente d un adversaire...",oponente:"Adversaire",chat:["Bonne question!","Tu etais rapide!","Bonne chance!","Allez!","Bravo!"]'
c = c.replace(old_fr, new_fr)

old_de = 'de:{procurando:"Warte auf einen Gegner...",oponente:"Gegner"'
new_de = 'de:{procurando:"Warte auf einen Gegner...",oponente:"Gegner",chat:["Gute Frage!","Du warst schnell!","Viel Glueck!","Los geht s!","Gut gemacht!"]'
c = c.replace(old_de, new_de)

old_it = 'it:{procurando:"Aspettando un avversario...",oponente:"Avversario"'
new_it = 'it:{procurando:"Aspettando un avversario...",oponente:"Avversario",chat:["Bella domanda!","Sei stato veloce!","In bocca al lupo!","Dai!","Bravo!"]'
c = c.replace(old_it, new_it)

# Adicionar funcoes de chat
old_func = "function bloquearAlternativas()"
new_func = """function enviarMsgChat(msg){
    if(!socket||!salaAtual) return;
    socket.emit("chatDuelo",{salaId:salaAtual,msg,nome:window.meuNomeGlobal});
    adicionarMsgChat(msg, "eu");
}
function adicionarMsgChat(msg, tipo){
    const div=document.getElementById("chat-msgs");
    if(!div) return;
    const m=document.createElement("div");
    m.className="chat-msg "+tipo;
    m.textContent=msg;
    div.appendChild(m);
    div.scrollTop=div.scrollHeight;
}
function iniciarChat(){
    const t=UI_TEXTOS[idiomaAtual]||UI_TEXTOS.pt;
    const msgs=t.chat||["Boa!","Rapido!","Sorte!","Vai!","Parabens!"];
    const div=document.getElementById("chat-rapido");
    if(!div) return;
    div.innerHTML=msgs.map(m=>'<button onclick="enviarMsgChat(\\'' + m + '\\'")>'+m+'</button>').join("");
    document.getElementById("chat-jogo").style.display="block";
}
function bloquearAlternativas()"""
c = c.replace(old_func, new_func)

# Mostrar chat quando jogo inicia
old_inicio = "renderizarRodada(dados.pergunta);"
new_inicio = "renderizarRodada(dados.pergunta); iniciarChat();"
c = c.replace(old_inicio, new_inicio, 1)

# Receber mensagens do oponente
old_socket = 'socket.on("oponenteSaiu"'
new_socket = '''socket.on("chatDuelo",d=>{ adicionarMsgChat(d.msg,"oponente"); });
    socket.on("oponenteSaiu"'''
c = c.replace(old_socket, new_socket)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK: chat adicionado")