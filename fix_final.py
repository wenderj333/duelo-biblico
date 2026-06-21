with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

antigo = b'function aplicarTraducao(idioma){\r\n    const t=UI_TEXTOS[idioma]||UI_TEXTOS.pt;\r\n    const n=document.getElementById("nomeUsuario"); if(n)n.placeholder=t.nome||"O teu nome...";\r\n    const b=document.querySelector(\'button[onclick="conectarAoJogo()"]\'); if(b)b.textContent=t.jogar||"Procurar Oponente";\r\n}\r\nfunction selecionarIdioma(idioma,btn){\r\n    idiomaAtual=idioma;\r\n    document.querySelectorAll(".idioma-btn").forEach(b=>b.classList.remove("ativo"));\r\n    btn.classList.add("ativo");\r\n    aplicarTraducao(idioma);\r\n}'

novo = b'function aplicarTraducoes(){\r\n    const tx=UI_TEXTOS[idiomaAtual]||UI_TEXTOS.pt;\r\n    const s=(id,v)=>{const e=document.getElementById(id);if(e)e.textContent=v;};\r\n    s("btn-procurar",tx.procurar||"Procurar Oponente");\r\n    s("btn-jogar-nov",tx.jogarNov||"Jogar Novamente");\r\n    s("txt-fim-duelo",tx.fimDuelo||"Fim do Duelo!");\r\n    s("label-jogadores-online",tx.jogadoresOnline||"Jogadores Online");\r\n    const ch=document.querySelector(".chat-header");if(ch)ch.textContent="\\u{1F4AC} "+(tx.chatHeader||"Chat");\r\n    const btns=document.querySelectorAll(".msg-rapida");\r\n    const msgs=[tx.amen,tx.boaP,tx.bomJ,tx.gloria];\r\n    btns.forEach((b,i)=>{if(msgs[i])b.textContent=msgs[i];});\r\n}\r\nfunction selecionarIdioma(idioma,btn){\r\n    idiomaAtual=idioma;\r\n    localStorage.setItem("duelo_lang",idioma);\r\n    document.querySelectorAll(".idioma-btn").forEach(b=>b.classList.remove("ativo"));\r\n    btn.classList.add("ativo");\r\n    aplicarTraducoes();\r\n}'

if antigo in content:
    content = content.replace(antigo, novo)
    print('OK!')
else:
    print('ERRO - nao encontrado')

# Adicionar IDs e mais chaves ao UI_TEXTOS
content = content.replace(
    b'    pt:{procurando:"Aguardando um irmao para o duelo...",oponente:"Oponente",desafiar:"Desafiar",desafioEnviado:"Desafio enviado!",desafioRec:"te desafia!",aceitar:"Aceitar",recusar:"Recusar",jogadoresOnline:"Jogadores Online"},',
    b'    pt:{procurando:"Aguardando um irmao para o duelo...",oponente:"Oponente",desafiar:"Desafiar",desafioEnviado:"Desafio enviado!",desafioRec:"te desafia!",aceitar:"Aceitar",recusar:"Recusar",jogadoresOnline:"Jogadores Online",procurar:"Procurar Oponente",jogarNov:"Jogar Novamente",fimDuelo:"Fim do Duelo!",chatHeader:"Chat com oponente",amen:"Amem!",boaP:"Boa pergunta!",bomJ:"Bom jogo!",gloria:"Gloria a Deus!"},'
)
content = content.replace(
    b'    en:{procurando:"Waiting for an opponent...",oponente:"Opponent",desafiar:"Challenge",desafioEnviado:"Challenge sent!",desafioRec:"challenges you!",aceitar:"Accept",recusar:"Decline",jogadoresOnline:"Online Players"},',
    b'    en:{procurando:"Waiting for an opponent...",oponente:"Opponent",desafiar:"Challenge",desafioEnviado:"Challenge sent!",desafioRec:"challenges you!",aceitar:"Accept",recusar:"Decline",jogadoresOnline:"Online Players",procurar:"Find Opponent",jogarNov:"Play Again",fimDuelo:"End of Duel!",chatHeader:"Chat with opponent",amen:"Amen!",boaP:"Good question!",bomJ:"Good game!",gloria:"Glory to God!"},'
)
content = content.replace(
    b'    de:{procurando:"Warte auf einen Gegner...",oponente:"Gegner",desafiar:"Herausfordern",desafioEnviado:"Herausforderung gesendet!",desafioRec:"fordert dich heraus!",aceitar:"Annehmen",recusar:"Ablehnen",jogadoresOnline:"Spieler Online"},',
    b'    de:{procurando:"Warte auf einen Gegner...",oponente:"Gegner",desafiar:"Herausfordern",desafioEnviado:"Herausforderung gesendet!",desafioRec:"fordert dich heraus!",aceitar:"Annehmen",recusar:"Ablehnen",jogadoresOnline:"Spieler Online",procurar:"Gegner suchen",jogarNov:"Nochmal spielen",fimDuelo:"Ende des Duells!",chatHeader:"Chat mit Gegner",amen:"Amen!",boaP:"Gute Frage!",bomJ:"Gutes Spiel!",gloria:"Ehre sei Gott!"},'
)
content = content.replace(
    b'    es:{procurando:"Esperando un oponente...",oponente:"Oponente",desafiar:"Desafiar",desafioEnviado:"Desafio enviado!",desafioRec:"te desafia!",aceitar:"Aceptar",recusar:"Rechazar",jogadoresOnline:"Jugadores en Linea"},',
    b'    es:{procurando:"Esperando un oponente...",oponente:"Oponente",desafiar:"Desafiar",desafioEnviado:"Desafio enviado!",desafioRec:"te desafia!",aceitar:"Aceptar",recusar:"Rechazar",jogadoresOnline:"Jugadores en Linea",procurar:"Buscar Oponente",jogarNov:"Jugar de Nuevo",fimDuelo:"Fin del Duelo!",chatHeader:"Chat con oponente",amen:"Amen!",boaP:"Buena pregunta!",bomJ:"Buen juego!",gloria:"Gloria a Dios!"},'
)
content = content.replace(
    b'    fr:{procurando:"En attente d un adversaire...",oponente:"Adversaire",desafiar:"Defier",desafioEnviado:"Defi envoye!",desafioRec:"vous defie!",aceitar:"Accepter",recusar:"Refuser",jogadoresOnline:"Joueurs en Ligne"},',
    b'    fr:{procurando:"En attente d un adversaire...",oponente:"Adversaire",desafiar:"Defier",desafioEnviado:"Defi envoye!",desafioRec:"vous defie!",aceitar:"Accepter",recusar:"Refuser",jogadoresOnline:"Joueurs en Ligne",procurar:"Trouver Adversaire",jogarNov:"Rejouer",fimDuelo:"Fin du Duel!",chatHeader:"Chat avec adversaire",amen:"Amen!",boaP:"Bonne question!",bomJ:"Bon jeu!",gloria:"Gloire a Dieu!"},'
)
content = content.replace(
    b'    it:{procurando:"Aspettando un avversario...",oponente:"Avversario",desafiar:"Sfidare",desafioEnviado:"Sfida inviata!",desafioRec:"ti sfida!",aceitar:"Accetta",recusar:"Rifiuta",jogadoresOnline:"Giocatori Online"},',
    b'    it:{procurando:"Aspettando un avversario...",oponente:"Avversario",desafiar:"Sfidare",desafioEnviado:"Sfida inviata!",desafioRec:"ti sfida!",aceitar:"Accetta",recusar:"Rifiuta",jogadoresOnline:"Giocatori Online",procurar:"Trova Avversario",jogarNov:"Gioca ancora",fimDuelo:"Fine del Duello!",chatHeader:"Chat con avversario",amen:"Amen!",boaP:"Buona domanda!",bomJ:"Buona partita!",gloria:"Gloria a Dio!"},'
)
content = content.replace(
    b'    ro:{procurando:"Asteptand un adversar...",oponente:"Adversar",desafiar:"Provoaca",desafioEnviado:"Provocare trimisa!",desafioRec:"te provoaca!",aceitar:"Accepta",recusar:"Refuza",jogadoresOnline:"Jucatori Online"}',
    b'    ro:{procurando:"Asteptand un adversar...",oponente:"Adversar",desafiar:"Provoaca",desafioEnviado:"Provocare trimisa!",desafioRec:"te provoaca!",aceitar:"Accepta",recusar:"Refuza",jogadoresOnline:"Jucatori Online",procurar:"Cauta Adversar",jogarNov:"Joaca din nou",fimDuelo:"Sfarsitul Duelului!",chatHeader:"Chat cu adversarul",amen:"Amin!",boaP:"Intrebare buna!",bomJ:"Joc bun!",gloria:"Slava lui Dumnezeu!"}'
)

# Adicionar IDs aos elementos
content = content.replace(b'<button class="btn" onclick="conectarAoJogo()">Procurar Oponente</button>', b'<button class="btn" id="btn-procurar" onclick="conectarAoJogo()">Procurar Oponente</button>')
content = content.replace(b'<button class="btn" style="margin-top:14px;" onclick="window.location.reload()">Jogar Novamente</button>', b'<button class="btn" id="btn-jogar-nov" style="margin-top:14px;" onclick="window.location.reload()">Jogar Novamente</button>')
content = content.replace(b'<h2 style="text-align:center;font-size:20px;margin-bottom:14px;color:#f0c040;">Fim do Duelo!</h2>', b'<h2 id="txt-fim-duelo" style="text-align:center;font-size:20px;margin-bottom:14px;color:#f0c040;">Fim do Duelo!</h2>')

# Chamar aplicarTraducoes no arranque
content = content.replace(b'atualizarJogadoresOnline();\n// ===== RANKING =====', b'atualizarJogadoresOnline();\naplicarTraducoes();\n// ===== RANKING =====')

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Verificacao:')
print('aplicarTraducoes:', b'aplicarTraducoes' in open(r'C:\Users\wender\Desktop\duelo-biblico\index.html','rb').read())
print('DE traducao:', b'Gegner suchen' in open(r'C:\Users\wender\Desktop\duelo-biblico\index.html','rb').read())
