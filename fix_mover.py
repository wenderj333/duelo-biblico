with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'rb') as f:
    content = f.read()

# Remover do lugar errado (dentro do centro do jogo)
bloco_errado = b'    <div class="section-title" style="margin-top:14px;">&#x1F465; <span id="label-jogadores-online">Jogadores Online</span></div>\n    <div id="lista-online-jogadores" style="margin-bottom:8px;">\n      <div class="sem-dados">Nenhum jogador online</div>\n    </div>\n'
content = content.replace(bloco_errado, b'')

# Inserir no sidebar depois de conquistas-lista
bloco_certo = b'<div id="conquistas-lista">\r\n        <div class="sem-dados">Joga para ganhar conquistas!</div>\r\n    </div>'
bloco_novo = bloco_certo + b'\r\n\r\n    <div class="section-title" style="margin-top:14px;">&#x1F465; <span id="label-jogadores-online">Jogadores Online</span></div>\r\n    <div id="lista-online-jogadores" style="margin-bottom:8px;">\r\n      <div class="sem-dados">Nenhum jogador online</div>\r\n    </div>'

content = content.replace(bloco_certo, bloco_novo, 1)

with open(r'C:\Users\wender\Desktop\duelo-biblico\index.html', 'wb') as f:
    f.write(content)
print('Movido!' if bloco_errado not in content else 'ERRO - ainda no lugar errado')
