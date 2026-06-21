with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# Substituir funcao aplicarTraducao por versao completa com TEXTOS
antigo = b'function aplicarTraducao(idioma){\n    const t=UI_TEXTOS[idioma]||UI_TEXTOS.pt;\n    const n=document.getElementById("nomeUsuario"); if(n)n.placeholder=t.nome||"O teu nome...";\n    const b=document.querySelector(\'button[onclick="conectarAoJogo()"]\')); if(b)b.textContent=t.jogar||"Procurar Oponente";\n}\nfunction selecionarIdioma(idioma,btn){\n    idiomaAtual=idioma;\n    document.querySelectorAll(".idioma-btn").forEach(b=>b.classList.remove("ativo"));\n    btn.classList.add("ativo");\n    aplicarTraducao(idioma);\n}'

idx = content.find(b'function aplicarTraducao')
print('Encontrado em:', idx)
print(content[idx:idx+400])
