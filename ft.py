with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# 1. Adicionar ID ao botao Procurar
content = content.replace(
    b'<button class="btn" onclick="conectarAoJogo()">Procurar Oponente</button>',
    b'<button class="btn" id="btn-procurar" onclick="conectarAoJogo()">Procurar Oponente</button>'
)

# 2. Adicionar ID ao botao Jogar Novamente
content = content.replace(
    b'<button class="btn" style="margin-top:14px;" onclick="window.location.reload()">Jogar Novamente</button>',
    b'<button class="btn" id="btn-jogar-nov" style="margin-top:14px;" onclick="window.location.reload()">Jogar Novamente</button>'
)

# 3. Substituir aplicarTraducao por aplicarTraducoes com TEXTOS completos
content = content.replace(
    b'function selecionarIdioma(idioma,btn){\r\n    idiomaAtual=idioma;\r\n    document.querySelectorAll(".idioma-btn").forEach(b=>b.classList.remove("ativo"));\r\n    btn.classList.add("ativo");\r\n    aplicarTraducao(idioma);\r\n}',
    b'const TEXTOS={\r\n    pt:{procurar:"Procurar Oponente",jogarNov:"Jogar Novamente"},\r\n    en:{procurar:"Find Opponent",jogarNov:"Play Again"},\r\n    es:{procurar:"Buscar Oponente",jogarNov:"Jugar de Nuevo"},\r\n    fr:{procurar:"Trouver Adversaire",jogarNov:"Rejouer"},\r\n    de:{procurar:"Gegner suchen",jogarNov:"Nochmal spielen"},\r\n    it:{procurar:"Trova Avversario",jogarNov:"Gioca ancora"},\r\n    ro:{procurar:"Cauta Adversar",jogarNov:"Joaca din nou"}\r\n};\r\nfunction aplicarTraducoes(){\r\n    const tx=TEXTOS[idiomaAtual]||TEXTOS.pt;\r\n    const e1=document.getElementById("btn-procurar");if(e1)e1.textContent=tx.procurar;\r\n    const e2=document.getElementById("btn-jogar-nov");if(e2)e2.textContent=tx.jogarNov;\r\n}\r\nfunction selecionarIdioma(idioma,btn){\r\n    idiomaAtual=idioma;\r\n    localStorage.setItem("duelo_lang",idioma);\r\n    document.querySelectorAll(".idioma-btn").forEach(b=>b.classList.remove("ativo"));\r\n    btn.classList.add("ativo");\r\n    aplicarTraducoes();\r\n}'
)

# 4. Chamar aplicarTraducoes no arranque
content = content.replace(
    b'atualizarJogadoresOnline();\n// ===== RANKING =====',
    b'atualizarJogadoresOnline();\naplicarTraducoes();\n// ===== RANKING ====='
)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)

print('IDs:', b'btn-procurar' in open(r'C:\Users\wender\Desktop\duelo-biblico\index.html','rb').read())
print('TEXTOS:', b'const TEXTOS=' in open(r'C:\Users\wender\Desktop\duelo-biblico\index.html','rb').read())
print('Feito!')
