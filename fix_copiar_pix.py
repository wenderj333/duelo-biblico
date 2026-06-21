with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Adicionar id ao botao copiar
c = c.replace(
    'onclick="copiarLink()" id="btn-copiar"',
    'onclick="copiarLink()" id="btn-copiar"'
)

# Adicionar id ao texto PIX
c = c.replace(
    '<div id="aviso-pix"',
    '<div id="aviso-pix-div"'
)
c = c.replace(
    'Para concorrer ao <strong style="color:#f0c040;">Premio PIX</strong> entra na',
    '<span id="txt-pix">Para concorrer ao</span> <strong style="color:#f0c040;">Premio PIX</strong> <span id="txt-pix2">entra na</span>'
)

# Actualizar aplicarTraducao para traduzir copiar e pix
old = '    const cv=document.getElementById("txt-convidar"); if(cv)cv.textContent=t.convidar||"Convida um amigo:";'
new = '''    const cv=document.getElementById("txt-convidar"); if(cv)cv.textContent=t.convidar||"Convida um amigo:";
    const cp=document.getElementById("btn-copiar"); if(cp&&!cp.textContent.includes(t.copiado||"Copiado"))cp.textContent=t.copiar||"Copiar";
    const px=document.getElementById("txt-pix"); if(px)px.textContent=t.pix||"Para concorrer ao";
    const px2=document.getElementById("txt-pix2"); if(px2)px2.textContent="entra na";'''

if old in c:
    c = c.replace(old, new)
    print("OK: pix e copiar adicionados")
else:
    print("ERRO")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)