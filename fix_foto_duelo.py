with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Guardar foto do oponente quando jogo inicia
old = 'window.fotosJogadores[window.meuNomeGlobal] = fotoBase64||null;\n        salaAtual=dados.salaId;'
new = 'window.fotosJogadores[window.meuNomeGlobal] = fotoBase64||null;\n        if(dados.fotoOponente) window.fotosJogadores[dados.oponente] = dados.fotoOponente;\n        salaAtual=dados.salaId;'
if old in c:
    c = c.replace(old, new)
    print("OK: foto oponente guardada")
else:
    print("ERRO 1: nao encontrado")

# 2. Remover banners PIX duplicados (deixar so o aviso-pix)
old2 = '''        <div style="margin-top:12px;padding:10px 14px;border-radius:10px;background:rgba(240,192,64,0.1);border:1px solid rgba(240,192,64,0.3);text-align:center;font-size:12px;color:rgba(255,255,255,0.7);">
            Para concorrer ao <strong style="color:#f0c040;">Premio PIX</strong> entra na
            <a href="https://sigo-com-fe.vercel.app" target="_blank" style="color:#f0c040;font-weight:700;">Sigo com Fe</a>
        </div>
        <div style="margin-top:12px;padding:10px 14px;border-radius:10px;background:rgba(240,192,64,0.1);border:1px solid rgba(240,192,64,0.3);text-align:center;font-size:12px;color:rgba(255,255,255,0.7);">
            Para concorrer ao <strong style="color:#f0c040;">Premio PIX</strong> entra na
            <a href="https://sigo-com-fe.vercel.app" target="_blank" style="color:#f0c040;font-weight:700;">Sigo com Fe</a>
        </div>'''
new2 = ''
if old2 in c:
    c = c.replace(old2, new2)
    print("OK: banners duplicados removidos")
else:
    print("ERRO 2: banners nao encontrados")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)